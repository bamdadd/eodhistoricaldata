import datetime
import json

import requests
import requests_cache
import os

from eod_csv_prices import EODCSVPrices
from option_chain import OptionChain
from urls import BASE_API_URL


class Stock:
    def __init__(self, symbol, exchange='US'):
        self.symbol = symbol
        self.exchange = exchange
        self.api_token = os.environ['EOD_API_TOKEN']
        assert self.api_token

    def get_eod_prices(self, from_date=None, to_date=None):
        expire_after = datetime.timedelta(days=1)
        session = requests_cache.CachedSession(cache_name='cache', backend ='sqlite', expire_after = expire_after)
        response = session.get(
            f'{BASE_API_URL}/eod/{self.symbol.upper()}.{self.exchange}', params={
                'api_token': self.api_token,
                'order': 'd',
                "from": from_date,
                "to": to_date
            })
        return EODCSVPrices(response)

    def get_live_price(self):
        result = requests.get(
            f'{BASE_API_URL}/real-time/{self.symbol.upper()}.{self.exchange}?api_token={self.api_token}&fmt=json').json()
        return result

    def get_option_chain(self):
        result = requests.get(
            f'{BASE_API_URL}/options/{self.symbol.upper()}.{self.exchange}?api_token={self.api_token}').json()
        return OptionChain(result)

    def get_fundamentals(self):
        result = requests.get(
            f'{BASE_API_URL}/fundamentals/{self.symbol.upper()}.{self.exchange}?api_token={self.api_token}').json()
        return result

    def get_iv_rank(self):
        self