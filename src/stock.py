import datetime
import json

import requests
import requests_cache
import os

from eod_csv_prices import EODCSVPrices
from option_chains import OptionChains
from urls import BASE_API_URL


class Stock:
    def __init__(self, symbol, exchange='US'):
        self.symbol = symbol
        self.exchange = exchange
        self.api_token = os.environ['EOD_API_TOKEN']
        assert self.api_token

    def get_eod_prices(self, from_date=None, to_date=None):
        expire_after = datetime.timedelta(days=1)
        session = requests_cache.CachedSession(cache_name='cache', backend='sqlite',
                                               expire_after=expire_after)
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

    def get_option_chains(self, from_date=None, to_date=None):
        print(from_date, to_date)
        expire_after = datetime.timedelta(days=1)
        session = requests_cache.CachedSession(cache_name='cache', backend='sqlite',
                                               expire_after=expire_after)
        result = session.get(
            f'{BASE_API_URL}/options/{self.symbol.upper()}.{self.exchange}',
            params={
                'api_token': self.api_token,
                "from": from_date,
                "to": to_date
            }
        ).json()
        return OptionChains(result)

    def get_fundamentals(self):
        expire_after = datetime.timedelta(days=1)
        session = requests_cache.CachedSession(cache_name='cache', backend='sqlite',
                                               expire_after=expire_after)
        result = session.get(
            f'{BASE_API_URL}/fundamentals/{self.symbol.upper()}.{self.exchange}?api_token={self.api_token}').json()
        return result

    def get_iv_rank(self):
        # WRONG!
        from_date = (datetime.datetime.now() - datetime.timedelta(days=365)).strftime("%Y-%m-%d")
        to_date = (datetime.datetime.now() + datetime.timedelta(days=45)).strftime("%Y-%m-%d")
        ivs = self.get_option_chains(from_date, to_date).get_ivs()
        print(ivs)
        all_ivs = list(ivs.values())

        return all_ivs[-1] / max(all_ivs) * 100

    def get_expected_move(self):
        # straddle price * 0.85
        atm_contracts = self.get_option_chains().get_at_the_money_contracts()
        straddle_price = atm_contracts['CALL'][0]['bid'] + atm_contracts['PUT'][0]['bid']
        expiry = atm_contracts['CALL'][0]['expirationDate']
        return straddle_price * 0.85, expiry
