#import configuration parameter
from config import port

#import flask package main class for app object
from flask import Flask
#import make_response from flask package for managing cookies
from flask import make_response
#import render_template from flask package for templating html code
from flask import render_template

#create flask object instance
app = Flask(__name__)

@app.route("/")
def home():
	response = make_response(render_template(
			"index.html"
		))

	return response

@app.route("/user")
def user():
	response = make_response(render_template(
			"user.html"
		))

	return response

@app.route("/topic")
def topic():
	response = make_response(render_template(
			"topic.html"
		))

	return response

if __name__ == "__main__":
	app.run(port=port, debug=True)
