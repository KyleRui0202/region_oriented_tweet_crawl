Region-Oriented Tweet Crawl Toolkit
=========
This toolkit is used to crawl tweet data using two Twitter REST APIs: GET search/tweets and GET users/search.

**_This toolkit assumes the following:_**

* You know how OAuth works for Twitter APIs
* You are using Python 2.7
* You have rights and know how to install Python libraries.

## Installation

First, clone this repo to your local machine:

```
git clone https://github.com/KyleRui0202/region_oriented_tweet_crawl.git
```

Next, make sure to install the required Python package "twitter". We use pip to install it:

```
pip install twitter
```

You may also install it from its GitGub repository: https://github.com/sixohsix/twitter.git. You can learn more about pip [here](https://pypi.python.org/pypi/pip).

## Configuration

Before running the tookit you have to configure it properly:

First, set up the required OAuth credentials for your Twitter App:

    CONSUMER_KEY = '[Consumer Key]'
    CONSUMER_SECRET = '[Consumer Secret]'
    OAUTH_TOKEN = '[OAuth Token]'
    OAUTH_TOKEN_SECRET = '[OAuth Token Secret]'

Next, set the region (or city) you are crawling tweet data from. This configuration varies when using different Twitter REST APIs:

**GET search/tweets**
The parameter "geoccode" should be set up correctly:

```
geocode = "[latitude, longitude, radius]"
```
**GET users/search**
The following two query lists should be set up correctly:

```
  # 
  query_list_1 = ["Albany", "Delmar", "Colonie", "East Greenbush", "Guilderland", "Glenmont",\
                  "Latham", "Loudonville", "Niskayuna", "Rensselaer", "Slingerlands", "Troy",\
                  "Voorheesville", "Waterford"]
                
  query_list_2 = ["", " New York", " NY", " N.Y."]
```
