class Dividends:
    def __init__(self, data):
        self.data = data

    def get_next_ex_dividend(self):
        return self.data['ExDividendDate']
