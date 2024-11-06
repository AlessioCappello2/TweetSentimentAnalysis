import re
import pandas as pd
from tqdm import tqdm
from deep_translator import GoogleTranslator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Wrapper for the GoogleTranslator function
def translate_text(text, target_language="en"):
    return GoogleTranslator(source='auto', target=target_language).translate(text)

column_name = "Text"
df = pd.read_csv("tweets/tweets.csv", encoding="utf-8")

# English stopwords (needed for stopwords removal)
stop_words = set(stopwords.words('english'))

def process_text(text):
    # URLs and usernames removal
    text = re.sub(r'https?://[^ ]+', '', text)
    text = re.sub(r'@[^ ]+', '', text)
    
    # Translate text to English
    text = translate_text(text)

    # Tokenize text to apply stopword removal
    tokens = word_tokenize(text)

    # Stopwords removal by checking if present in stop_words
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

    # Join the filtered tokens back into a string
    return ' '.join(filtered_tokens)


print("Text pre-processing and translation...")
for idx, row in tqdm(df.iterrows(), total=df.shape[0], desc="Processing tweets"):
    df.at[idx, column_name] = process_text(row[column_name])

# Save the outcome in a new csv file
df.to_csv("tweets/tweets_processed.csv", index=False, encoding="utf-8")