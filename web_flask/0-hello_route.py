#!/usr/bin/python3
"""
This script starts a Flask web application
"""
from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """This section defines content for home route"""
    return "Hello HBNHB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
