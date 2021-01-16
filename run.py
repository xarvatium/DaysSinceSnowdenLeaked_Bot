import tweepy
import time

# Authentication
auth = tweepy.OAuthHandler("API_KEY", "API_SECRET")
auth.set_access_token("ACCES_TOKEN", "ACCESS_SECRET")

# Accessing Twitter API
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# POSTing Tweet to Twitter's API
daysSince = 2781
amountTweet = 1
while True:
    api.update_status(f'Days since Edward Snowden leaked government records: {daysSince}')
    daysSince += 1
    print(f'Tweet #{amountTweet} has been posted')
    amountTweet += 1
    time.sleep(86400)
