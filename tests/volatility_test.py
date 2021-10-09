import unittest

from stock import Stock, EODCSVPrices
from volatility import Volatility


class TestStock(unittest.TestCase):

    def test_volatility(self):
        volatility = Volatility()
        self.assertEqual(float, type(volatility.get_volatility()))

    def test_volatility_rank(self):
        volatility = Volatility()

        volatility_rank = volatility.get_volatility_rank()
        print(volatility_rank, volatility.get_volatility_rank(30))
        self.assertEqual(float, type(volatility_rank))
