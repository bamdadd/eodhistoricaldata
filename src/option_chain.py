class OptionChain:
    def __init__(self, chain_dict):
        self.chain_dict = chain_dict
        self.code = self.chain_dict['code']
        self.data = self.chain_dict['data']
        self.exchange = self.chain_dict['exchange']
        self.stock_price = self.chain_dict['lastTradePrice']

    def get_monthly(self):
        return list(
            filter(lambda x: x['options']['CALL'][0]['contractPeriod'] == 'MONTHLY', self.data))

    def get_monthly_iv(self):
        result = {}
        for m in self.get_monthly():
            result[m['expirationDate']] = m['impliedVolatility']

        return result