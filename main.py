# https://coinmarketcap.com/robots.txt

from scraper import Scraper
from datamodel import Token

TOKENS = ["bitcoin","ethereum","cardano","nervos-network","snek"]

scraper = Scraper()

token_collection: list[Token] = []

for token in TOKENS:
    token_model = scraper.fetch(token)
    token_collection.append(token_model)

    print(token_model.name)
    print(token_model.symbol)
    print(token_model.price)
