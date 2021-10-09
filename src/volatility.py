import datetime
from stock import Stock


class Volatility:
    def __init__(self):
        self.stock = Stock('VIX', exchange='INDX')

    def get_volatility(self):
        return self.stock.get_live_price()['close']

    def get_volatility_rank(self, days=365):
        from_date = (datetime.datetime.now() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
        to_date = (datetime.datetime.now()).strftime("%Y-%m-%d")
        prices = self.stock.get_eod_prices(from_date=from_date, to_date=to_date).to_pandas()
        current = self.stock.get_live_price()['close']
        high = float(prices['High'].max())
        low = float(prices['Low'].min())
        return ((high-current)/low) * 100