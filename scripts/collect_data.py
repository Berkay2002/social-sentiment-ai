import tweepy
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def collect_tweets(api_key, api_secret_key, access_token, access_token_secret, query, max_tweets, output_file):
    # Authenticate to the Twitter API
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # List to store collected tweets
    tweets = []
    
    # Collect tweets
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items(max_tweets):
        tweets.append(tweet._json)

    # Save collected tweets to a JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(tweets, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # Load credentials from environment variables
    API_KEY = os.getenv('API_KEY')
    API_SECRET_KEY = os.getenv('API_SECRET_KEY')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
    QUERY = '#example'
    MAX_TWEETS = 100
    OUTPUT_FILE = os.path.join('data', 'raw_data', 'tweets.json')

    # Create the output directory if it does not exist
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # Collect tweets and save to the specified output file
    collect_tweets(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, QUERY, MAX_TWEETS, OUTPUT_FILE)
