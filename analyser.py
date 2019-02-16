import time
import datetime
import pandas as pd
import tools
import requests


class twitterquery:

    def get_twitter_response(self):
        api = tools.TwitterClient()
        tweets = api.get_tweets(query='trump', count=250)
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        ptweetsperc = (100 * len(ptweets) / len(tweets))
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        ntweetsperc = (100 * len(ntweets) / len(tweets))
        neuttweetperc = (100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets))
        testtime = datetime.datetime.now()
        return (ptweetsperc, ntweetsperc, neuttweetperc, testtime)


class oandaquery:
    def stream(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 7988784158b97bb23e2c31e1c3c2963b-6760148dd294e502680d2eb6e94b0235',
        }

        response = requests.get(
            'https://api-fxpractice.oanda.com/v3/accounts/101-004-9972545-001/pricing?instruments=USD_JPY',
            headers=headers)
        prices = response.json()
        bids = prices['prices'][0]['asks'][0]['price']
        asks = prices['prices'][0]['bids'][0]['price']
        return (bids, asks)

    # if __name__ == "__main__":
#
#     for x in range(0, 600):
#         print('working{}'.format(x))
#         newDF = pd.DataFrame()
#         testtime = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
#
#         for j in range(0, 200):
#             df = pd.DataFrame()
#             df['time'] = datetime.datetime.now()
#             df = df.append(df['time'])
#             vals = get_twitter_response()
#             prices = stream()
#             print(prices)
#             df['asks'] = prices['prices'][0]['asks'][0]['price']
#             df['bids'] = prices['prices'][0]['bids'][0]['price']
#             df['positive'] = vals[0]
#             df['negative'] = vals[1]
#             df['neutral'] = vals[2]
#             df['time'] = datetime.datetime.now()
#             newDF = newDF.append(df)
#             time.sleep(20)
#             j += 1
#
#         newDF.to_csv("out{}.csv".format(testtime), index=False)
#
#     x += 1
