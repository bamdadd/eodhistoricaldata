import unittest

from stock import Stock, EODCSVPrices


class TestStock(unittest.TestCase):

    def test_stock_test(self):
        stock = Stock('TSLA')
        self.assertEqual('TSLA', stock.symbol)


    def test_stock_eod_price_test(self):
        stock = Stock('TSLA')
        self.assertEqual(EODCSVPrices, stock.get_eod_prices().__class__)

    def test_stock_live_price_test(self):
        stock = Stock('TSLA')
        live_prices = stock.get_live_price()
        self.assertEqual(dict, live_prices.__class__)
        self.assertTrue('code' in live_prices)
        self.assertTrue('timestamp' in live_prices)
        self.assertTrue('gmtoffset' in live_prices)
        self.assertTrue('open' in live_prices)
        self.assertTrue('high' in live_prices)
        self.assertTrue('low' in live_prices)
        self.assertTrue('close' in live_prices)
        self.assertTrue('volume' in live_prices)
        self.assertTrue('previousClose' in live_prices)
        self.assertTrue('change' in live_prices)
        self.assertTrue('change_p' in live_prices)
