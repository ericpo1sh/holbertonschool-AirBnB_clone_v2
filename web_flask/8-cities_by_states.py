#!/usr/bin/python3
"""Starts Flask web application"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


def hello_world():
    """ Function that returns text """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_title():
    """ Function that displays HBNB prompt """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ function that returns the value of text in a string """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """ function that returns Python + value of text input """
    return "Python {}".format(text.replace('_', " "))


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_a_number(n):
    """ checks if n is int, returns text if n is a integer """
    return "{} ".format(n) + "is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_in_html(n):
    """ function that adds n into html file """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    """ Function that checks if number is even or odd """
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """ Function that returns HTML page of states in storage """
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Function that returns the html page of """
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """ Function that removes the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
