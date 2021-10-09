from io import StringIO
import csv
import pandas as pd


class EODCSVPrices:
    def __init__(self, response):
        self.response = response
        assert self.response.status_code == 200

    def to_pandas(self):
        content = StringIO(self.response.text)

        df = pd.read_csv(content,
                         skipfooter=1, parse_dates=[0], index_col=0, engine='python')
        return df
