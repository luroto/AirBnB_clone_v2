#!/usr/bin/python3
"""
This script starts a Flask web application with some routes
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def home():
    """This section defines content for home route"""
    return "Hello HBNB!"

@app.route ('/hbnb')
def hbnb():
	"""This section defines for hbnb route """
	return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
