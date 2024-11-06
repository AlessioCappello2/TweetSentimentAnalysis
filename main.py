import subprocess
import sys
import argparse

venv = str(sys.executable) # used to launch a subprocess

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
    '--reqs',
    action='store_true',
    help='Optional flag to indicate whether it is necessary to download dependencies and nltk resources (default: True, use --no-reqs to skip).'
)

args = parser.parse_args()

if args.reqs:
    subprocess.run([venv, 'src/requirements.py'], check=True)
    subprocess.run([venv, 'src/nltk_reqs.py'], check=True)

subprocess.run([venv, 'src/tweets_retrieval.py', args.topic, str(args.count)], check=True)
subprocess.run([venv, 'src/preprocess_tweets.py'], check=True)
subprocess.run([venv, 'src/sentiment_analysis.py'], check=True)