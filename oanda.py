import time
import datetime
import pandas as pd
import requests
import config

class oandaquery:
    def __init__(self):
        self.response = None
        self.ask = None
        self.bids = None
        self.stock_dataframe = None
        self.stock_prices = None

    def get_oanda_response(self):

        key = config.get_api_key()

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(key),
        }

        self.response = requests.get(
            'https://api-fxpractice.oanda.com/v3/accounts/101-004-9972545-001/pricing?instruments=USD_JPY',
            headers=headers).json()

        self.stock_prices = pd.DataFrame(data=self.response['prices'])



        self.time = self.stock_prices['time']
        self.ask = float(self.stock_prices['closeoutAsk'])
        self.bids = float(self.stock_prices['closeoutBid'])

    def load_data_frame(self):
        self.df = self.df.append(self.stock_prices)
        self.stats = self.df.tail(1)




if __name__ == "__main__":

    test = oandaquery()
    test.get_oanda_response()

    time.sleep(1)