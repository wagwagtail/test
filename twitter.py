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