import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import time
import datetime
import pandas as pd
import requests

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''

    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'SwDA0B5NpMZSWbH0ornhaGsk0'
        consumer_secret = 'mlgQlhRpBbDdByPVkT74TGWnWaO8IPvTeGTK2zfFAEx7itaB3k'
        access_token = '4915964742-gkkiEvCYXCBJts7HygRe9QDoHe8xQBiB560Lzzb'
        access_token_secret = 'nRueljIPDV9wz2zS1IOEPXFpicazuZDZQ2dEDAVaIhzHe'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
            Utility function to clean tweet text by removing links, special characters
            using simple regex statements.
            '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count=10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q=query, count=count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))


def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query='USDJPY', count=250)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ptweetsperc = (100 * len(ptweets) / len(tweets))
    # percentage of positive tweets
    # print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    ntweetsperc = (100 * len(ntweets) / len(tweets))
    # print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
    # percentage of neutral tweets

    neuttweetperc = (100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets))
    # print("Neutral tweets percentage: {} %".format(100 * (len(tweets) - len(ntweets) - len(ptweets))/ len(tweets)))

    return (ptweetsperc, ntweetsperc, neuttweetperc)


def stream():

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 7988784158b97bb23e2c31e1c3c2963b-6760148dd294e502680d2eb6e94b0235',
    }

    response = requests.get(
        'https://api-fxpractice.oanda.com/v3/accounts/101-004-9972545-001/pricing?instruments=USD_JPY',
        headers=headers)

    return response.json()

if __name__ == "__main__":


    for x in range(0, 30):

        newDF = pd.DataFrame()
        testtime = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")

        for j in range(0, 600):
            df = pd.DataFrame()
            df['time'] = datetime.datetime.now()
            df = df.append(df['time'])
            vals = main()
            prices = stream()
            df['asks'] = prices['prices'][0]['asks'][0]['price']
            df['bids'] = prices['prices'][0]['bids'][0]['price']
            df['positive'] = vals[0]
            df['negative'] = vals[1]
            df['neutral'] = vals[2]
            df['time'] = datetime.datetime.now()
            newDF = newDF.append(df)
            time.sleep(20)
            j += 1

        newDF.to_csv("out{}.csv".format(testtime), index=False)

    x += 1