import json
import re
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(tokens)

def preprocess_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    preprocessed_data = []
    for tweet in data:
        if 'text' in tweet:
            tweet['text'] = preprocess_text(tweet['text'])
            preprocessed_data.append(tweet)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(preprocessed_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    INPUT_FILE = os.path.join('data', 'raw_data', 'tweets.json')
    OUTPUT_FILE = os.path.join('data', 'preprocessed_data', 'preprocessed_tweets.json')

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    preprocess_data(INPUT_FILE, OUTPUT_FILE)

