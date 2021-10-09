import unittest

from stock import Stock, EODCSVPrices


class TestStock(unittest.TestCase):

    def test_stock_test(self):
        stock = Stock('TSLA')
        self.assertEqual('TSLA', stock.symbol)


    def test_stock_test(self):
        stock = Stock('TSLA')
        self.assertEqual(EODCSVPrices, stock.get_eod_prices().__class__)