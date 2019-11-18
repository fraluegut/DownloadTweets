import os
import tweepy as tw
import pandas as pd

consumer_key = '5BsVH34drjDKfVOfXxxVjXmkc'
consumer_secret = 'I5d1MNWSVJdDIItXOLbwwOl8WfFYJmMKWH7ZXMTxT9sr9wei40'
access_token = '606273133-w8CuPN7bBHFQeMROCNGEmcT7RKzbi0yQHTxLdRF5'
access_token_secret = '5392MwzuGmysgxSiPruTKKhWtIL2CIkb9KUVbScZvMzbJ'


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

