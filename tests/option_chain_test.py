import json
import unittest

from option_chain import OptionChain


class TestOptionChain(unittest.TestCase):

    def setUp(self) -> None:
        with open('fixtures/chain_fixture.json', 'r') as f:
            self.chain = chain = OptionChain(json.loads(f.read()))

    def test_options_chain_test(self):
        self.assertEqual(OptionChain, self.chain.__class__)
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
