import tweepy
import json
import os

def collect_tweets(api_key, api_secret_key, access_token, access_token_secret, query, max_tweets, output_file):
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    tweets = []
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items(max_tweets):
        tweets.append(tweet._json)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(tweets, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # Replace these with your actual credentials and query parameters
    API_KEY = 'your_api_key'
    API_SECRET_KEY = 'your_api_secret_key'
    ACCESS_TOKEN = 'your_access_token'
    ACCESS_TOKEN_SECRET = 'your_access_token_secret'
    QUERY = 'example query'
    MAX_TWEETS = 100
    OUTPUT_FILE = os.path.join('data', 'raw_data', 'tweets.json')

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    collect_tweets(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, QUERY, MAX_TWEETS, OUTPUT_FILE)

