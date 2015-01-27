Region-Oriented Tweet Crawl Toolkit
=========
This toolkit is used to crawl tweet data using two Twitter REST APIs: GET search/tweets and GET users/search.

**_This toolkit assumes the following:_**

* You know how OAuth works for Twitter APIs
* You are using Python 2.7
* You have rights and know how to install Python libraries.

## Installation

First, clone this repository to your local machine:

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

First, set the required OAuth credentials for your Twitter App:

    CONSUMER_KEY = '[Consumer Key]'
    CONSUMER_SECRET = '[Consumer Secret]'
    OAUTH_TOKEN = '[OAuth Token]'
    OAUTH_TOKEN_SECRET = '[OAuth Token Secret]'

Next, set the region (or city) from which you are crawling tweet data. This configuration varies when using different Twitter REST APIs:

**GET search/tweets**

The parameter "geoccode" should be assigned correctly in the script _tweets_search.py_:

```
geocode = "[latitude, longitude, radius]"
```
**GET users/search**

The following two query lists should be assigned correctly in the script _users_tweets.py_:

```
  # City name, suburb towns and villages. Here is the example for Albany, NY
  query_list_1 = ["Albany", "Delmar", "Colonie", "East Greenbush", "Guilderland", "Glenmont",\
                  "Latham", "Loudonville", "Niskayuna", "Rensselaer", "Slingerlands", "Troy",\
                  "Voorheesville", "Waterford"]
    
  # State name and its abbreviation. Here is the example for the state of New York            
  query_list_2 = ["", " New York", " NY", " N.Y."]
```

Finally, set the name of the file to store the crawled tweet data:

```
fo = open("[city name]_users_tweets.txt", "w+")
```

## Running the Toolkit

The script _tweets_search.py_ is using _GET search/tweets_ to crawl tweet data. You can run it using the following execution command:

```
python tweets_search.py
```

The script _users_tweets.py_ is using _GET users/search_ to crawl tweet data. You can run it using the following execution command:

```
python users_tweets.py
```

## Ongoing Work

1. Use MongoDB instead of files to store crawled tweet data
2. Script consolidation

## Credits

This toolkit is maintained by [Rui Yang](https://github.com/KyleRui0202).

## License

Distributed under the MIT License:

The MIT License (MIT)

Copyright (c) 2009-2013 University of Washington

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


