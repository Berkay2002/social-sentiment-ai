import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification
from tensorflow.keras.optimizers import Adam
import json
import os

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    texts = [tweet['text'] for tweet in data]
    labels = [tweet.get('label', 0) for tweet in data]  # Assuming labels are provided in the data
    return texts, labels

def train_sentiment_model(train_texts, train_labels, epochs=2, batch_size=16):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased')

    train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=128)

    train_dataset = tf.data.Dataset.from_tensor_slices((
        dict(train_encodings),
        train_labels
    )).batch(batch_size)

    optimizer = Adam(learning_rate=3e-5)
    model.compile(optimizer=optimizer, loss=model.compute_loss, metrics=['accuracy'])
    
    model.fit(train_dataset, epochs=epochs)
    return model

if __name__ == "__main__":
    TRAIN_DATA_FILE = os.path.join('data', 'preprocessed_data', 'preprocessed_tweets.json')
    MODEL_SAVE_PATH = os.path.join('models', 'sentiment_model.h5')

    train_texts, train_labels = load_data(TRAIN_DATA_FILE)
    model = train_sentiment_model(train_texts, train_labels)

    os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)
    model.save(MODEL_SAVE_PATH)

