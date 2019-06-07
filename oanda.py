import time
import datetime
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from config import GetDetails
from sql.sql import SqlTable

class oandaquery:
    def __init__(self):
        self.response = None
        self.time = None
        self.ask = None
        self.bids = None
        self.stock_dataframe = None
        self.stock_prices = None

    def get_oanda_response(self):
        config = GetDetails()
        key = config.get_api_key()

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(key),
        }

        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        self.response = session.get(
            'https://api-fxpractice.oanda.com/v3/accounts/101-004-9972545-001/pricing?instruments=USD_JPY',
            headers=headers).json()

        self.stock_prices = pd.DataFrame(data=self.response['prices'])

        self.time = self.stock_prices['time'][0]
        self.ask = float(self.stock_prices['asks'].values[0][0].get('price'))
        self.bids = float(self.stock_prices['bids'].values[0][0].get('price'))

    def load_data_frame(self):
        self.df = self.df.append(self.stock_prices)
        self.stats = self.df.tail(1)




if __name__ == "__main__":

    connection = SqlTable()
    while True:
            test = oandaquery()
            test.get_oanda_response()
            print(test.time)
            connection.write(time=test.time, ask=test.ask, bid=test.bids)
            time.sleep(1)