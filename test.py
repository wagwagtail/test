import requests
import pandas as pd
import json
import time


# currentDT = datetime.datetime.now()
# print(str(currentDT))


def stream():
    headers = {
        'Authorization': 'Bearer 7988784158b97bb23e2c31e1c3c2963b-6760148dd294e502680d2eb6e94b0235',
    }

    response = requests.get(
        'https://stream-fxpractice.oanda.com/v3/accounts/101-004-9972545-001/pricing/stream?instruments=EUR_USD%2CUSD_CAD',
        headers=headers)

    # NB. Original query string below. It seems impossible to parse and
    # reproduce query strings 100% accurately so the one below is given
    # in case the reproduced version is not "correct".
    # response = requests.get('https://stream-fxtrade.oanda.com/v3/accounts/101-004-9972545-001/pricing/stream?instruments=EUR_USD%2CUSD_CAD', headers=headers)

    # headers = {
    #     # 'Content-Type': 'application/json',
    #     'Authorization': 'Bearer 7988784158b97bb23e2c31e1c3c2963b-6760148dd294e502680d2eb6e94b0235',
    # }
    #
    # # 101-004-9972545-001
    # response = requests.get(
    #     'https://api-fxpractice.oanda.com/v3/accounts/101-004-9972545-001/pricing?instruments=EUR_USD',
    #     stream=True,
    #     headers=headers)
    # # parsed_json = json.loads(response.json())

    response = response.json()
    # df = pd.DataFrame.from_dict(response)
    #
    # #

    return response


if __name__ == "__main__":
    while True:
        df = stream()
        print(df)
        # # updatedataframe(newdata)
        # time.sleep(2)
