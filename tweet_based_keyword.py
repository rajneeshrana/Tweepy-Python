import tweepy
from pprint import pprint

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

keyword = 'ssr'
for tweet in api.search(q=keyword, lang = 'en', rpp=10):
    tweet.text = tweet.text
    tweet.user.name = tweet.user.name
    pprint(f'{tweet.user.name}:{tweet.text}')