import tweepy
from dotenv import load_dotenv
import os
import json
load_dotenv()
# Authenticate with the Twitter API using your API keys
auth = tweepy.OAuthHandler(os.getenv('TWITTER_API_KEY'), os.getenv('TWITTER_API_SECRET'))
auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
# print(os.getenv('TWITTER_ACCESS_TOKEN'))
# auth = tweepy.OAuth2BearerHandler(os.getenv('TWITTER_ACCESS_TOKEN'))
api = tweepy.API(auth)

# Collect tweets containing a specific keyword
tweets = api.search_tweets(q='Infosys', count=100)
with open('tweets.json', 'w') as f:
    for tweet in tweets:
        f.write(json.dumps(tweet._json))
        f.write('\n')
        # print(json.dumps(tweet.__json, indent=4))
