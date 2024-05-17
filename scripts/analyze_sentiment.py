import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification
import os

def analyze_sentiment(model, texts):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    encodings = tokenizer(texts, truncation=True, padding=True, max_length=128)
    inputs = dict(encodings)
    
    predictions = model.predict(inputs)
    return tf.argmax(predictions.logits, axis=1).numpy()

if __name__ == "__main__":
    MODEL_PATH = os.path.join('models', 'sentiment_model.h5')
    model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased')
    model.load_weights(MODEL_PATH)

    sample_texts = [
        "I love this product! It's amazing.",
        "This is the worst service ever.",
        "I'm not sure how I feel about this."
    ]

    sentiments = analyze_sentiment(model, sample_texts)
    for text, sentiment in zip(sample_texts, sentiments):
        print(f"Text: {text} => Sentiment: {sentiment}")

