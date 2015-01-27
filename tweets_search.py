##############################################################################
# Crawl region-oriented tweet data using Twitter REST API: Get search/tweets #
##############################################################################

import twitter
import json
from twitter_request import make_twitter_request

def oauth_login():
# XXX: Go to http://twitter.com/apps/new to create an app and get values
# for these credentials that you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation
    CONSUMER_KEY = '[Consumer Key]'
    CONSUMER_SECRET = '[Consumer Secret]'
    OAUTH_TOKEN = '[OAuth Token]'
    OAUTH_TOKEN_SECRET = '[OAuth Token Secret]'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

# The least number of tweets to be sampled 
TWEET_NUMBER = 5000

# Get the twitter API connector
twitter_api = oauth_login()

# The geocode parameter for the city
geocode = "[latitude, longitude, radius]"

tmp_search = make_twitter_request(twitter_api.search.tweets, q = "%20", geocode = geocode,\
                                  lang = "en", result_type = "recent", count = 50)

search_result = set([])
for status in tmp_search["statuses"]:
    user_mentions = [user_mention["screen_name"] for user_mention in status["entities"]["user_mentions"]]
    hashtags = [hashtag["text"] for hashtag in status["entities"]["hashtags"]]
    urls = [url["url"] for url in status["entities"]["urls"]]
        
    search_result.add((status["user"]["id_str"], status["created_at"], status["text"],\
                           tuple(user_mentions), tuple(hashtags),tuple(urls)))

max_id = long(tmp_search["statuses"][len(tmp_search["statuses"])-1]["id_str"]) - 1

while max_id>0 and len(search_result)<TWEET_NUMBER:
    
    tmp_search = make_twitter_request(twitter_api.search.tweets, q = "%20", geocode = geocode,\
                                  lang = "en", result_type = "recent", count = 50, max_id = max_id)
    for status in tmp_search["statuses"]:
        user_mentions = [user_mention["screen_name"] for user_mention in status["entities"]["user_mentions"]]
        hashtags = [hashtag["text"] for hashtag in status["entities"]["hashtags"]]
        urls = [url["url"] for url in status["entities"]["urls"]]
        
        search_result.add((status["user"]["id_str"], status["created_at"], status["text"],\
                           tuple(user_mentions), tuple(hashtags),tuple(urls)))

    max_id = long(tmp_search["statuses"][len(tmp_search["statuses"])-1]["id_str"]) - 1
    
print "New tweets number: ", str(len(search_result))

fo = open("[city name]_search_tweets.txt", "w+")
try:
    search_result = search_result | set(json.load(fo))
except ValueError:
    pass

print "Total tweets number: ", str(len(search_result))
search_result = list(search_result)
json.dump(search_result, fo, indent=1)
print "Name of the file: ", fo.name
fo.close()
