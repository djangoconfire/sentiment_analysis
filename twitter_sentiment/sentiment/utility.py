import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import re


api_key='FCAvoUl0FrcJbMq7XuuipM3i2'
api_secret='9mhkDaNOrHV1niThhFnHnoJ2mnXPZTv7Z8uL8COcKb8CCqTTGi'
access_token_key= '3702383240-lnuXWb2EIKqMqbyhrISeyh1JtiX5fp7bR8QZ8AR'
access_token_secret_key='ltH243fpcyzTN04RpiASi7Wd4Ulc1thTsryUwT90mHN11'




class TwitterClient(object):
    def __init__(self, query, retweets_only=False, with_sentiment=False):
        # keys and tokens from the Twitter Dev Console
        consumer_key = api_key
        consumer_secret = api_secret
        access_token = access_token_key
        access_token_secret = access_token_secret_key
        # Attempt authentication
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.query = query
            self.retweets_only = retweets_only
            self.with_sentiment = with_sentiment
            self.api = tweepy.API(self.auth)
            self.tweet_count_max =50  # To prevent Rate Limiting
        except:
            print("Error: Authentication Failed")

    def set_query(self, query=''):
        self.query = query

    def set_retweet_checking(self, retweets_only='false'):
        self.retweets_only = retweets_only

    def set_with_sentiment(self, with_sentiment='false'):
        self.with_sentiment = with_sentiment

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self):
        tweets = []

        try:
            tweet_list = self.api.search(q=self.query,
                                          count=self.tweet_count_max)
            if not tweet_list:
                pass
            for tweet in tweet_list:
                parsed_tweet = {}

                parsed_tweet['text'] = tweet.text
                parsed_tweet['user'] = tweet.user.screen_name
                
                if self.with_sentiment == 1:
                    parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
                else:
                    parsed_tweet['sentiment'] = 'unavailable'

                if tweet.retweet_count > 0 and self.retweets_only == 1:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                elif not self.retweets_only:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)

            return tweets

        except tweepy.TweepError as e:
            print("Error : " + str(e))
