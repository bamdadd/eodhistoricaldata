import requests
import os

from eod_csv_prices import EODCSVPrices
from urls import BASE_API_URL


class Stock:
    def __init__(self, symbol, exchange='US'):
        self.symbol = symbol
        self.exchange = exchange
        self.api_token = os.environ['EOD_API_TOKEN']
        assert self.api_token

    def get_eod_prices(self):
        return EODCSVPrices(requests.get(
            f'{BASE_API_URL}/eod/{self.symbol.upper()}.{self.exchange}?api_token='))

    def get_live_price(self):
        result = requests.get(
            f'{BASE_API_URL}/real-time/{self.symbol.upper()}.{self.exchange}?api_token={self.api_token}&fmt=json').json()
        return result

    def get_option_chain(self):
        result = requests.get(
            f'{BASE_API_URL}/options/{self.symbol.upper()}.{self.exchange}?api_token={self.api_token}').json()
        return result