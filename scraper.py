from bs4 import BeautifulSoup
import requests
from datamodel import Token

URL = "https://coinmarketcap.com/currencies/"
HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "nl,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "Priority": "u=0, i",
        "Sec-Ch-Ua": "\"Microsoft Edge\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    }

class Scraper:

    def __init__(self) -> None:
        self.url = URL

    def fetch(self, token: str) -> Token:
        response = requests.get(url=f"{self.url}{token}", headers=HEADERS)

        soup = BeautifulSoup(response.text, "html.parser")

        raw_name = soup.find(name="span", attrs={"data-role": "coin-name"})
        raw_symbol = soup.find(name="span", attrs={"data-role": "coin-symbol"})
        raw_price = soup.find(name="span", attrs={"data-test": "text-cdp-price-display"})

        try:
            token_name = raw_name.get_text().split()[0]
            token_symbol = raw_symbol.get_text()
            token_price = raw_price.get_text().split("$")[1]
        except AttributeError:
            token_name = "N/A"
            token_symbol = "N/A"
            token_price = 0.00
            
            print("Token not found")

        return Token(token_name, token_symbol, token_price)
