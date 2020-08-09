import tweepy
from pprint import pprint

consumer_key = ''
consumer_secret = ''
access_token = '-'
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# api = tweepy.API(auth, wait_on_rate_limit=True)
#
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

####### post a tweet #############

# api.update_status('This Tweet is testing tweep')


######### get user related info #######
'''
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

'''
########## display tweet text based on keyword #########

'''keyword = 'ssr'
for tweet in api.search(q=keyword, lang = 'en', rpp=10):
    tweet.text = tweet.text
    tweet.user.name = tweet.user.name
    pprint(f'{tweet.user.name}:{tweet.text}')'''

########## The followers() method #########
'''
screen_name = "imrajneesh_rana"
for follower in api.followers(screen_name):
    print(follower.screen_name)'''

# user = api.get_user('imrajneesh_rana')
# user_id = user.id
# timeline = api.user_timeline(user_id=user_id, count=200)
# pprint(timeline)

# api.media_upload("temple.jpg")




