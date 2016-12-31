#import configuration parameter
from config import api_port

#import flask package main class for app object
from flask import Flask
#import make_response from flask package for managing cookies
from flask import make_response
#import render_template from flask package for templating html code
from flask import render_template
from flask import request

from tweepyModule import userTweet
from tweepyModule import topicTweet

#create flask object instance
app = Flask(__name__)

@app.route("/get_user")
def get_user():
	user_id = request.args.get("user_id")
	tweetList = userTweet(user_id, 10)
	return

if __name__ == "__main__":
	app.run(port=api_port, debug=True)
