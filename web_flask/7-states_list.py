#!/usr/bin/python3
""" Scritp for start a Flask web application"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def removing(self):
    """ Method for removing SQLAlchemy Session"""
    storage.close()


@app.route('/states_list')
def states_list():
    """This script is for displaying a HTML page listing states """
    toret = storage.all(State)
    toret = toret.values()
    return render_template('7-states_list.html', toret=toret)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
