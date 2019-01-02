import requests
import pandas as pd
import json
import time


def stream():

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 7988784158b97bb23e2c31e1c3c2963b-6760148dd294e502680d2eb6e94b0235',
    }

    # 101-004-9972545-001
    response = requests.get(
        'https://api-fxpractice.oanda.com/v3/accounts/101-004-9972545-001/pricing?instruments=USD_JPY',
        headers=headers)





    return response.json()


if __name__ == "__main__":

    while True:
        df = stream()
        # bids = df['prices'][0]['bids'][0]['price']
        # # asks = df['prices'][0]['asks'][0]['price']
        # time1 = df['time']
        print('asks: {}'.format(df['prices'][0]['asks'][0]['price']))
        print('time: {}'.format(df['time']))
        print('bids: {}'.format(df['prices'][0]['bids'][0]['price']))
        # # # updatedataframe(newdata)
        # time.sleep(1)
