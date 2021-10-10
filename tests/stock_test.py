import unittest

from option_chains import OptionChains
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

    def test_options_chain_test(self):
        stock = Stock('TSLA')
        chain = stock.get_option_chains()
        self.assertEqual(OptionChains, chain.__class__)
        self.assertTrue(chain.code)
        self.assertTrue(chain.exchange)
        self.assertTrue(chain.data)
        self.assertTrue('expirationDate' in chain.data[0])
        self.assertTrue('options' in chain.data[0])
        self.assertTrue('CALL' in chain.data[0]['options'])
        self.assertTrue('PUT' in chain.data[0]['options'])
        self.assertTrue('contractName' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('contractSize' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('currency' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('type' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('inTheMoney' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('lastTradeDateTime' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('expirationDate' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('strike' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('lastPrice' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('bid' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('ask' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('change' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('changePercent' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('volume' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('openInterest' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('impliedVolatility' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('delta' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('gamma' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('theta' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('vega' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('rho' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('theoretical' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('intrinsicValue' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('timeValue' in chain.data[0]['options']['CALL'][0])
        self.assertTrue('updatedAt' in chain.data[0]['options']['CALL'][0])


    def test_stock_fundamental(self):
        stock = Stock('TSLA')
        self.assertTrue('General' in stock.get_fundamentals())
        self.assertTrue('Highlights' in stock.get_fundamentals())
        self.assertTrue('Earnings' in stock.get_fundamentals())
        self.assertTrue('Financials' in stock.get_fundamentals())

    def test_get_iv_rank(self):
        stock = Stock('SPY', exchange='US')
        self.assertEqual(43, stock.get_iv_rank())

    def test_get_expected_move(self):
        stock = Stock('SPY', exchange='US')
        self.assertEqual((16.0225, '2021-11-19'), stock.get_expected_move())