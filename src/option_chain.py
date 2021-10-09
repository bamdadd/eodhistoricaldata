class OptionChain:
    def __init__(self, chain_dict):
        self.chain_dict = chain_dict
        self.code = self.chain_dict['code']
        self.data =self.chain_dict['data']
        self.exchange =self.chain_dict['exchange']

    def get_monthly(self):
        return list(filter(lambda x: x['options']['CALL'][0]['contractPeriod'] == 'MONTHLY', self.data))
