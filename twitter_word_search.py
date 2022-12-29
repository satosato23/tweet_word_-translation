import tweepy
import os
import time

from deep_translator import GoogleTranslator
from dotenv import load_dotenv
from os.path import join, dirname

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

bearer_token=os.environ.get("BEARER_TOKEN")
consumer_key=os.environ.get("CONSUMER_KEY")
consumer_secret=os.environ.get("CONSUMER_SECRET")
access_key=os.environ.get("ACCESS_TOKEN")
access_secret=os.environ.get("ACCESS_TOKEN_SECRET")


client = tweepy.Client(
    bearer_token,
    consumer_key,
    consumer_secret,
    access_key,
    access_secret
)
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_key, access_secret
)
api = tweepy.API(auth)

#search_query setting
word='chatgpt -is:retweet -has:mentions'
tweets = client.search_recent_tweets(query=word,max_results=100)

def main():
    
    if tweets is not None:
        for tweet in tweets[0]:
            tweet_id=tweet.id
            tweet = api.get_status(tweet_id, tweet_mode='extended')
            try:
                if tweet.favorite_count >5:
                    username = tweet.user.screen_name
            
                    text = tweet.full_text
                    translated = GoogleTranslator(source='auto',target='ja').translate(text)
                    
                    url="https://twitter.com/"+username+"/status/"+str(tweet_id)
                    tweet_text=translated+"\n\n"+url
                    print(tweet_text)
                    client.create_tweet(text=tweet_text)

                
                    time.sleep(60)
                else:
                    continue
            except tweepy.errors.BadRequest as error:
                pass

            
main()