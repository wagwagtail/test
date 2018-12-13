import requests
import pandas as pd
import numpy as np

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 7988784158b97bb23e2c31e1c3c2963b-6760148dd294e502680d2eb6e94b0235',
}

# 101-004-9972545-001
response = requests.get('https://api-fxpractice.oanda.com/v3/accounts/101-004-9972545-001', headers=headers)

data = response.json()

df = pd.DataFrame.from_dict(data)
# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://api-fxtrade.oanda.com/v3/instruments/USD_CAD/candles?price=BA&from=2016-10-17T15%3A00%3A00.000000000Z&granularity=M1', headers=headers)
