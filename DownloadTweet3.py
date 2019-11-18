import os
import tweepy as tw
import pandas as pd

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = '#archaeology'
date_since = '2018-11-15'

# Collect tweets
tweets = tw.Cursor(api.search,
                   q= search_words,
                   lang = "en",
                   since=date_since).items(5)

#Iterate and print tweets
#for tweet in tweets:
 #   print(tweet.text)

# Collect a list of tweets
[tweet.text for tweet in tweets]

