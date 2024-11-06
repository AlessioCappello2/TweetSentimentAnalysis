import csv
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the model and tokenizer
model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Define labels based on the model's configuration
labels = ["Negative", "Neutral", "Positive"]

def analyze_sentiment(text):
    # Tokenize the text and prepare it as a PyTorch tensor
    inputs = tokenizer(text, return_tensors="pt")
    
    # Get the model's prediction
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Extract the predicted class
    scores = outputs.logits[0]
    predicted_class = torch.argmax(scores).item()
    
    # Map the predicted class to the corresponding sentiment
    sentiment = labels[predicted_class]
    return sentiment, scores


with open("tweets.csv", mode='r', newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    column_name = "Text"

    for row in reader:
        text = row[column_name]
        sentiment, scores = analyze_sentiment(text)
        print(f"{row['Count']} - Sentiment: {sentiment}, Scores: {scores} - Text: {text}")

'''import csv
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def is_positive(tweet: str):
    return "Positive" if sia.polarity_scores(tweet)["compound"] > 0 else "Negative"

column_data = []
column_name = "Text"  # Replace with the header of the column

with open("tweets.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        column_data.append(row[column_name])

for tweet in column_data:
    print(">", is_positive(tweet), tweet)'''