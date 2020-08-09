import tweepy
from pprint import pprint

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user('imrajneesh_rana')
user_id = user.id
location = user.location
description = user.description
name = user.name
follower = user.followers_count
following = user.friends_count

print("user location : " + location )
print("user description : " + description)
print("user id : " + str(user_id))
print("user name : " + name)
print("user follower : "  + str(follower))
print("user following : "  + str(following))