import tweepy
from pprint import pprint
import time

consumer_key = ''
consumer_secret = ''
access_token = '-'
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

FILE_NAME = "last_seen.txt"


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


# pprint(tweets[0].text)
def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#rajji' in tweet.full_text.lower():
            print(str(tweet.id) + '-' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + " Bot work properly with like: ", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)


while True:
    reply()
    time.sleep(15)


