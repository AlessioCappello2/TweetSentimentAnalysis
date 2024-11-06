import subprocess
import sys
import argparse

venv = sys.executable

parser = argparse.ArgumentParser(description="Script to retrieve tweets related to a topic and analyze the authors' sentiments")

parser.add_argument(
    '--topic',  
    type=str,   
    required=True,  
    help='The topic to retrieve tweets about and perform sentiment analysis (required - you can also submit a Twitter query).'
)

parser.add_argument(
    '--count',
    type=int,
    default=20,
    help='Number of tweets to retrieve (default: 20). WARNING: an excessive number of tweets may lead to long waiting times.'
)

parser.add_argument(
    '--nltkreqs',
    action='store_true',
    help='Optional flag to indicate whether it is necessary to download nltk resources (default: True, use --no-nltkreqs to skip).'
)

args = parser.parse_args()

if args.nltkreqs:
    subprocess.run([str(venv), 'nltk_reqs.py'], check=True)

subprocess.run([str(venv), 'tweets_retrieval.py', args.topic, str(args.count)], check=True)
subprocess.run([str(venv), 'preprocess_and_translate.py'], check=True)
subprocess.run([str(venv), 'sentiment_analysis.py'], check=True)