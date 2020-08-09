import tweepy
from pprint import pprint

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

screen_name = "imrajneesh_rana"
for follower in api.followers(screen_name):
    print(follower.screen_name)