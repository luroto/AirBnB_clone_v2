#!/usr/bin/python3
"""
This script starts a Flask web application
"""
from flask import Flask, escape, request

app = Flask(__name__)

app.run(host='0.0.0.0', port=5000)
@app.route('/', strict_slashes=False)
def home():
    """This section defines content for home route"""
    return "Hello HBNHB!"
