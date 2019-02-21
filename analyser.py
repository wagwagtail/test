import time
import datetime
import pandas as pd
import tools
import requests
from calculations import parser, stats


class twitterquery:

    def get_twitter_response():
        # try:
        #     api = tools.TwitterClient()
        #     tweets = api.get_tweets(query='ftse', count=25000)
        #     ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        #     ptweetsperc = (100 * len(ptweets) / len(tweets))
        #     ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        #     ntweetsperc = (100 * len(ntweets) / len(tweets))
        #     neuttweetperc = (100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets))
        #     testtime = datetime.datetime.now()
        # except:
        ptweetsperc = 50
        ntweetsperc = 50
        neuttweetperc = 50
        testtime = datetime.datetime.now()
        return (ptweetsperc, ntweetsperc, neuttweetperc, testtime)


class oandaquery:
    def stream():
        stock = {}
        stock['pythontime'] = datetime.datetime.now()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 7988784158b97bb23e2c31e1c3c2963b-6760148dd294e502680d2eb6e94b0235',
        }

        response = requests.get(
            'https://api-fxpractice.oanda.com/v3/accounts/101-004-9972545-001/pricing?instruments=USD_JPY',
            headers=headers)
        stock['response'] = response.json()

        return stock


if __name__ == "__main__":
    time_at_program_run = datetime.datetime.now()
    newDF = pd.DataFrame()
    while True:
        time_difference = (datetime.datetime.now() - time_at_program_run).seconds
        if time_difference < 3.:
            print('smaller than 20')
        else:
            stock = oandaquery.stream()
            df = parser(stock)
            newDF = newDF.append(df)
            newDF['stats'] = (datetime.datetime.now() - newDF['time']) < datetime.timedelta(seconds=30.)
            stats_input = newDF.loc[newDF['stats'] == True]
            df_stats = stats(stats_input)
            print(df_stats)

        # try:

        #     print(newDF)
        #     time.sleep(2)
        # except:
        #     print("This is an error message!")
