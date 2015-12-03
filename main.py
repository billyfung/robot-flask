"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/')
def index():
	return render_template('index.html')
# def hello():
#     """Return a friendly HTTP greeting."""
#     return 'Hello World!'

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

@app.route('/<action>', methods = ['POST'])
#this redirects commands from the html page which has buttons for actions
def action(action):
# #as per index.html, whenever the root url is requested, action() is called
 #if subdirectory is called, we pass the name into the function robot/foo -> action('foo')
    #if action == 'base-anti-clockwise':
    	#then move arm by sending command via usb, and change status
 		#arm.MoveArm(t=1.0, cmd = 'base-anti-clockwise')
#     if action == 'base-clockwise':
# 	arm.MoveArm(t=1.0, cmd = 'base-clockwise')
# and so on for the rest of the commands
	response = {
	'action' : 'Do the movement ' + action
	}

	return render_template('index.html', **response)
