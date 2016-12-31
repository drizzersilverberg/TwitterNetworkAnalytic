import tweepy
import string
# Consumer keys and access tokens, used for OAuth
from config import consumer_key
from config import consumer_secret
from config import access_token
from config import access_token_secret
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret) 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def clearTweet(tweet):
	tweet = filter(lambda x: x in string.printable, tweet)
	tweet = tweet.replace(":","")
	return tweet

def userTweet(query, max_tweets):
	tweets = [] 
	for tweet in tweepy.Cursor(api.search,
	                           q=query,
	                           rpp=100,
	                           result_type="recent",
	                           include_entities=True,
	                           lang="en").items(max_tweets):
	    text = clearTweet(tweet.text)
	    text = text.split(" ")
	    if query in text:
	    	text = " ".join(text)
	    	tweets.append(text)

	return tweets

def topicTweet(query, max_tweets):
	tweets = [] 
	for tweet in tweepy.Cursor(api.search,
	                           q=query,
	                           rpp=100,
	                           result_type="recent",
	                           include_entities=True,
	                           lang="en").items(max_tweets):

		text = clearTweet(tweet.text)
		tweets.append(text)

 	return tweets

# ut = user_tweet("@Dendi_Hansamu", 100)
# tt = topic_tweet("Ahok", 100)

# for i in ut:
# 	print i

# for i in tt:
# 	print i

# print len(ut)
# print len(tt)
