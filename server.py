#import flask package main class for app object
from flask import Flask
#import make_response from flask package for managing cookies
from flask import make_response
#import render_template from flask package for templating html code
from flask import render_template
from flask import request

#create flask object instance
app = Flask(__name__)

@app.route("/")
def index():
	inner = {
		"title":"TNA Homepage",
		"head":"Twitter Network Analytic"
	}
	response = make_response(render_template(
			"index.html",
			inner=inner
		))

	return response

@app.route("/user", methods=['GET'])
def user():
	query = request.args.get("q")
	row = request.args.get("row")
	url = "http://tna-api.herokuapp.com/user?q=%s&row=%s"%(query,row)

	inner = {
		"title":"User Analytic",
		"head":"Twitter Network Analytic - User Analytic"
	}
	
	response = make_response(
		render_template(
			"network.html",
			inner=inner,
			url=url
	))

	return response

@app.route("/topic")
def topic():
	query = request.args.get("q")
	row = request.args.get("row")
	url = "http://tna-api.herokuapp.com/topic?q=%s&row=%s"%(query,row)

	inner = {
		"title":"Topic Analytic",
		"head":"Twitter Network Analytic - Topic Analytic"
	}
	response = make_response(render_template(
			"network.html",
			inner=inner,
			url=url
		))

	return response

if __name__ == "__main__":
	app.run(debug=True)
