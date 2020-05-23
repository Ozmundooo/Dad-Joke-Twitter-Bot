import tweepy
import time
from joke.jokes import icanhazdad

api_key = "API_KEY"
api_secret_key = "API_SECRET_KEY"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Tweet Dadjoke
timer = 15 * 60 # Turn to seconds (15 mins)
while True:
    joke = icanhazdad()
    api.update_status(joke)
    print(joke)
    time.sleep(timer)
