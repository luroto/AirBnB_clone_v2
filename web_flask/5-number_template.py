#!/usr/bin/python3
"""
This script starts a Flask web application with some routes
"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """This section defines content for home route"""
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
        """This section defines for hbnb route """
        return ("HBNB")


@app.route('/c/<text>')
def c(text):
        """ This section defines for routes for variables"""
        if "_" in text:
            text = text.replace("_", " ")
        return ("C {}".format(text))


@app.route('/python/<text>')
@app.route('/python')
def python(text="is cool"):
        """ This section defines proceedure for python routes"""
        if "_" in text:
            text = text.replace("_", " ")
        return("Python {}".format(text))


@app.route('/number/<int:number>')
def number(number):
        """ This section defines procedures for number routes"""
        return("{} is a number".format(number))


@app.route('/number_template/<int:number>')
def number_template(number):
    """ This section defines procedures for number template routes,
    including HTML documents"""
    return render_template('5-number.html', number=number)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
