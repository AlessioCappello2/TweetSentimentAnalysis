# Imports
import twikit
import time
from datetime import datetime
import pandas as pd
from configparser import ConfigParser
from random import randint
import asyncio
import sys

# Search criteria
#QUERY = '(from:elonmusk) lang:en until:2020-01-01 since:2018-01-01' # example of query that can be passed as input
QUERY = sys.argv[1]
REQUIRED_TWEETS = int(sys.argv[2])

# Login credentials
config = ConfigParser()
config.read('config.ini')
username = config['X']['username']
email = config['X']['email']
password = config['X']['password']

# Define client
client = twikit.Client(language='en-US')

# Async function for login (sync method deprecated with twikit upgrades)
async def login():
    try:
        client.load_cookies('cookies.json')
        print(f"Welcome back {username}!")
    except FileNotFoundError:
        await client.login(auth_info_1=username, auth_info_2=email, password=password)
        print("Successfully logged in!")
        client.save_cookies('cookies.json')

# Tweets retrieval function
async def get_tweets():
    count = 0
    tweets = None

    while count < REQUIRED_TWEETS:
        try:
            if not tweets:
                tweets = await client.search_tweet(QUERY, product='Latest')
            else:
                tweets = await tweets.next()
            waiting = randint(5, 10)  
            time.sleep(waiting)  # used to emulate a human behavior 
        except twikit.TooManyRequests as e:
            rate_limit_reset = datetime.fromtimestamp(e.rate_limit_reset)
            print(f'{datetime.now()} - Rate limit reached. Waiting until {rate_limit_reset}')
            wait_time = rate_limit_reset - datetime.now()
            time.sleep(wait_time.total_seconds())
            continue
        
        if not tweets:
            print(f'{datetime.now()} - No more tweets found')
            break

        for tweet in tweets:
            count += 1
            tweet_data = [count, tweet.user.name, tweet.text, tweet.created_at, tweet.retweet_count, tweet.favorite_count]

            row = pd.DataFrame([tweet_data], columns=['Count', 'Username', 'Text', 'Created At', 'Retweets', 'Likes'])
            row.to_csv('tweets/tweets.csv', mode='a', header=False, index=False, encoding="utf-8")
            
            if count == REQUIRED_TWEETS:
                break

        print(f'{datetime.now()} - Got {count} tweets')
    
    print(f'{datetime.now()} - Done! Got {count} tweets')


# Launch login function in an async event loop
asyncio.run(login())

columns = ['Count', 'Username', 'Text', 'Created At', 'Retweets', 'Likes']
df = pd.DataFrame(columns=columns)
df.to_csv('tweets/tweets.csv', index=False)

# Launch tweets retrieval in an async event loop
asyncio.run(get_tweets())