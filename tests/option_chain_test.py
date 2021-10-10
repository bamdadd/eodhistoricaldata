import json
import unittest

from option_chains import OptionChains


class TestOptionChain(unittest.TestCase):

    def setUp(self) -> None:
        with open('fixtures/chain_fixture.json', 'r') as f:
            self.chain = chain = OptionChains(json.loads(f.read()))

    def test_options_chain_test(self):
        self.assertEqual(OptionChains, self.chain.__class__)
        self.assertTrue(self.chain.code)
        self.assertTrue(self.chain.exchange)
        self.assertTrue(self.chain.data)
        self.assertTrue('expirationDate' in self.chain.data[0])
        self.assertTrue('options' in self.chain.data[0])
        self.assertTrue('CALL' in self.chain.data[0]['options'])
        self.assertTrue('PUT' in self.chain.data[0]['options'])
        self.assertTrue('contractName' in self.chain.data[0]['options']['CALL'][0])

    def test_get_monthly_chains(self):
        monthly = self.chain.get_monthly()
        self.assertEqual('MONTHLY', monthly[0]['options']['CALL'][0]['contractPeriod'])

    def test_get_monthly_iv(self):
        ivs = self.chain.get_ivs()
        self.assertEqual({'2021-10-15': 77.9106, '2021-11-19': 75.0463, '2022-01-21': 69.6724}, ivs)

    def test_get_stock_price(self):
        self.assertEqual(26.3, self.chain.stock_price)

    def test_get_at_the_money_contracts(self):
        self.assertEqual({'CALL': [{'ask': 3.6,
                                    'bid': 2.4,
                                    'change': 0,
                                    'changePercent': None,
                                    'contractName': 'TWKS211119C00025000',
                                    'contractPeriod': 'MONTHLY',
                                    'contractSize': 'REGULAR',
                                    'currency': 'USD',
                                    'daysBeforeExpiration': 41,
                                    'delta': 0.6325,
                                    'expirationDate': '2021-11-19',
                                    'gamma': 0.0639,
                                    'impliedVolatility': 66.1357,
                                    'inTheMoney': 'TRUE',
                                    'intrinsicValue': 0,
                                    'lastPrice': 0,
                                    'lastTradeDateTime': '0000-00-00 00:00:00',
                                    'openInterest': None,
                                    'rho': 0.0157,
                                    'strike': 25,
                                    'theoretical': 3,
                                    'theta': -0.0265,
                                    'timeValue': 0,
                                    'type': 'CALL',
                                    'updatedAt': '2021-10-08 19:08:13',
                                    'vega': 0.0336,
                                    'volume': None}],
                          'PUT': [{'ask': 2.6,
                                   'bid': 1.75,
                                   'change': 0,
                                   'changePercent': None,
                                   'contractName': 'TWKS211119P00025000',
                                   'contractPeriod': 'MONTHLY',
                                   'contractSize': 'REGULAR',
                                   'currency': 'USD',
                                   'daysBeforeExpiration': 41,
                                   'delta': -0.3735,
                                   'expirationDate': '2021-11-19',
                                   'gamma': 0.0529,
                                   'impliedVolatility': 80.2907,
                                   'inTheMoney': 'FALSE',
                                   'intrinsicValue': 0,
                                   'lastPrice': 0,
                                   'lastTradeDateTime': '0000-00-00 00:00:00',
                                   'openInterest': None,
                                   'rho': -0.0123,
                                   'strike': 25,
                                   'theoretical': 2.175,
                                   'theta': -0.0323,
                                   'timeValue': 0,
                                   'type': 'PUT',
                                   'updatedAt': '2021-10-08 19:08:13',
                                   'vega': 0.0338,
                                   'volume': None}]}, self.chain.get_at_the_money_contracts())
