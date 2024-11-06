# Tweet Sentiment Analysis
Tiny application that allows you to retrieve tweets about a specific topic to see how people are feeling about it.

## Dependencies
The application is based on open source packages to retrieve tweets, preprocess them and output the sentiment. It works, but you never know due to X (formerly Twitter) policies and unofficial API instability. 😔

The dependencies can be installed by launching the application with the argument ```--reqs```.

### [twikit](https://github.com/d60/twikit)
Twikit is an open source library that allows interaction with the Twitter API.
```
pip install twikit
```

### [nltk](https://github.com/nltk/nltk)
Natural Language ToolKit (shortly, nltk) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing.
```
pip install nltk
```
The application needs additional resources, that can be installed by launching it with the argument ```--reqs```.

### [transformers](https://github.com/huggingface/transformers)
Transformers provides thousands of pretrained models to perform tasks on different modalities such as text, vision, and audio.
```
pip install transformers
```

### [deep_translator](https://github.com/nidhaloff/deep-translator)
Deep_translator is a flexible tool that can translate between different languages in a simple way using multiple translators.
```
pip install deep-translator
```

## Configure user credentials
Modify ```config.ini``` in order to run the application properly: put your username, email and password (run it locally, do not share it with anyone). I suggest using a secondary account since X may track the activity related to the account as suspicious and ban it.

## Usage
To launch the application, activate your virtual environment and launch on the command line:
```
python main.py --topic TOPIC [--count COUNT] [--reqs]
```
where ```TOPIC``` is the topic to retrieve tweets about (you can also input a Twitter Query), ```COUNT``` refer to the desired number of tweets to retrieve (if fewer tweets are available, fewer will be returned), and ```--reqs``` is a flag used to indicate whether it is necessary to download the dependencies and the additional nltk resources. Use ```-h``` or ```--help``` to verify the meaning of each argument on the fly.

#### Example of usage
```
python main.py --topic "Donald Trump America USA elections"
```

At the end, two csv files will be created inside the ```tweets``` folder:
* ```tweets.csv```: it contains the tweets text and some information (author, date, likes, retweets)
* ```tweets_processed.csv```: it's a copy of the previous one but it contains the processed text (English translation, stopwords removed) and an additional column reporting the sentiment labeled by the model.
