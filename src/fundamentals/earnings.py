from pprint import pprint
import datetime

class Earnings(object):
    def __init__(self, data):
        self.data = data
        # pprint(data)

    def get_history(self):
        history = self.data['History']
        return history

    def get_future_earnings(self, days=90):
        history = self.get_history()
        future_earnings= {}
        for d in history:
            date = datetime.datetime.strptime(history[d]['reportDate'], '%Y-%m-%d')
            if  datetime.datetime.now() <date<  (datetime.datetime.now() + datetime.timedelta(days=days)):
                future_earnings[d] = history[d]
        return future_earnings

    def get_next_earning(self, days=90):
        future_earnings = self.get_future_earnings(days=days)
        next_date = list(future_earnings.keys())[0]
        return future_earnings[next_date]['reportDate']
