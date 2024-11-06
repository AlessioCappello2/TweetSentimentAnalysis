import re
import csv
import os
from tqdm import tqdm
from deep_translator import GoogleTranslator
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def translate_text(text, target_language="en"):
    return GoogleTranslator(source='auto', target=target_language).translate(text)

column_name = "Text"  # Header of the csv column of interest

with open("tweets.csv", mode="r", newline="", encoding="utf-8") as readfile, \
    open("tweets_tmp.csv", mode="w", newline="", encoding="utf-8") as writefile:
    reader = csv.DictReader(readfile)
    writer = csv.DictWriter(writefile, fieldnames=reader.fieldnames)

    writer.writeheader()
    
    # English stopwords (needed to apply stopwords removal)
    stop_words = set(stopwords.words('english'))

    print("Text pre-processing and translation...")
    for row in tqdm(reader, desc="Progress"):
        # Raw tweet text
        text = row[column_name]

        # URLs and usernames removal
        text = re.sub(r'https?://[^ ]+', '', text)
        text = re.sub(r'@[^ ]+', '', text)
        
        # Translate text to english
        text = translate_text(text)

        # Tokenize text to apply stopword removal
        tokens = word_tokenize(text)

        # Stopwords removal by checking if present in stop_words
        filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

        # Join the filtered tokens back into a string
        filtered_text = ' '.join(filtered_tokens)

        # Replace with processed and translated text
        row[column_name] = translate_text(text)
        writer.writerow(row)

os.replace("tweets_tmp.csv", "tweets.csv")