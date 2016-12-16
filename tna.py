#import flask package main class for app object
from flask import Flask
#import make_response from flask package for managing cookies
from flask import make_response
#import render_template from flask package for templating html code
from flask import render_template
#import render_template from flask package for to perform request

#create flask object instance
app = Flask(__name__)

@app.route("/")
def home():
	response = make_response(render_template(
			"index.html"
		))

	return response

if __name__ == "__main__":
	app.run(port=5000, debug=True)
