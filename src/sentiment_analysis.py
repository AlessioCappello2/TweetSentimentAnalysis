import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the model and tokenizer
model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# twitter-roberta labels configuration
labels = ["Negative", "Neutral", "Positive"]

def analyze_sentiment(text):
    # Tokenize the text and prepare it as a PyTorch tensor
    inputs = tokenizer(text, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    scores = outputs.logits[0]
    predicted_class = torch.argmax(scores).item()
    
    sentiment = labels[predicted_class]
    return sentiment

# Add a column with the sentiment for each tweet
tweets = pd.read_csv('tweets/tweets_processed.csv')
tweets["Sentiment"] = [analyze_sentiment(text) for text in tweets["Text"]]
tweets.to_csv('tweets/tweets_processed.csv', index=False)