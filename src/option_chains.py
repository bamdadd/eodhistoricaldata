class OptionChains:
    def __init__(self, chain_dict):
        self.chain_dict = chain_dict
        self.code = self.chain_dict['code']
        self.data = self.chain_dict['data']
        self.exchange = self.chain_dict['exchange']
        self.stock_price = self.chain_dict['lastTradePrice']

    def get_monthly(self):
        return list(
            filter(lambda x: x['options']['CALL'][0]['contractPeriod'] == 'MONTHLY', self.data))

    def get_ivs(self):
        result = {}
        for m in self.data:
            result[m['expirationDate']] = m['impliedVolatility']
        return result

    def get_contracts_by_dte(self, start_dte, end_dte):
        return list(
            filter(lambda x: start_dte < x['options']['CALL'][0]['daysBeforeExpiration'] < end_dte,
                   self.get_monthly()))

    def get_at_the_money_contracts(self):
        contracts = self.get_contracts_by_dte(21, 45)
        threshold = 0.001
        if self.stock_price < 50:
            threshold = 0.05
        calls = list(
            filter(lambda x: self.stock_price - (self.stock_price * threshold) < x['strike'] < self.stock_price + (self.stock_price * threshold),
                   contracts[0]['options']['CALL']))
        puts = list(
            filter(lambda x: self.stock_price - (self.stock_price * threshold) < x[
                'strike'] < self.stock_price + (self.stock_price * threshold),
                   contracts[0]['options']['PUT']))
        return {"CALL": calls, "PUT": puts}

