#!/usr/bin/python3
"""Starts Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Function that returns text """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_prompt():
    """ Function thatdisplays HBNB prompt """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ function that returns the value of tet in a string """
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
