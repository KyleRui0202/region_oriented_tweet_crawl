#############################################################################
# Crawl region-oriented tweet data using Twitter REST API: Get users/search #
#############################################################################

import twitter
import json
import re
from twitter_request import make_twitter_request

def oauth_login():
# XXX: Go to http://twitter.com/apps/new to create an app and get values
# for these credentials that you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation
    CONSUMER_KEY = '[COnsumer Key]'
    CONSUMER_SECRET = '[Consumer Secret]'
    OAUTH_TOKEN = '[OAuth Token]'
    OAUTH_TOKEN_SECRET = '[OAuth Token Secret]'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

# Get the twitter API connector
twitter_api = oauth_login()

# City name, suburb towns and villages. Here is the example for Albany, NY
query_list_1 = ["Albany", "Delmar", "Colonie", "East Greenbush", "Guilderland", "Glenmont",\
                "Latham", "Loudonville", "Niskayuna", "Rensselaer", "Slingerlands", "Troy",\
                "Voorheesville", "Waterford"]

# State name and its abbreviation. Here is the example for the state of New York
query_list_2 = ["", " New York", " NY", " N.Y."]

# Combine search query lists
query_list = [(query_1, query_2) for query_1 in query_list_1 for query_2 in query_list_2]

# Get the "focus" user's friends
albany_users_tweets = set([])

for query in query_list:
    
    for i in range(25):
        tmp_users = make_twitter_request(twitter_api.users.search, q = query[0] + query[1], page = i, count = 20)
        # print json.dumps(list(tmp_users), indent=1)
        print "...........\n\n"
        any_match = False
        for user in tmp_users:

            if "location" in user.keys():
                location = user["location"]
                is_match = True

                if (location.find(query[0]) < 0\
                    and location.find("Albany") < 0)\
                    or (location.find("New York") < 0\
                        and location.find("NY") < 0\
                        and location.find("N.Y.") < 0):
                    print "Not in NY"
                    is_match = False

                if is_match == True:
                    any_match = True
                    if "status" in user.keys():
                        if ("lang" in user.keys() and user["lang"]=="en")\
                           or ("lang" in user["status"].keys() and user["status"]["lang"] == "en"):
                            print json.dumps(user, indent=1)

                            user_mentions = [user_mention["screen_name"] for user_mention in user["status"]["entities"]["user_mentions"]]
                            hashtags = [hashtag["text"] for hashtag in user["status"]["entities"]["hashtags"]]
                            urls = [url["url"] for url in user["status"]["entities"]["urls"]]
                            
                            albany_users_tweets.add((user["id_str"], user["status"]["created_at"], user["status"]["text"],\
                                                      tuple(user_mentions), tuple(hashtags),tuple(urls)))

        if any_match == False:
            break

print "New tweets number: ", str(len(albany_users_tweets))
# print json.dumps(albany_users_tweets, indent=1)

fo = open("[city name]_users_tweets.txt", "w+")
try:
    users_tweets = users_tweets | set(json.load(fo))
except ValueError:
    pass
    
print "Total tweets number: ", str(len(users_tweets))
users_tweets = list(users_tweets)
json.dump(users_tweets, fo, indent=1)
print "Name of the file: ", fo.name
fo.close()
