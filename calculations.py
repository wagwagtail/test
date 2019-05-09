import pandas as pd
import numpy as np
import datetime as dt


def average(self):
    average = 0
    return average

def parser(stock):

    df = pd.DataFrame(dt.datetime.now())
    df['sell'] = float(stock["response"]['prices'][0]['asks'][0]['price'])
    df['buy'] = float(stock["response"]['prices'][0]['bids'][0]['price'])
    df.set_index('time')
    return df

def stats(stats_input):
    average_buy = float(stats_input['buy'].mean())
    average_sell = float(stats_input['sell'].mean())
    return average_buy, average_sell
