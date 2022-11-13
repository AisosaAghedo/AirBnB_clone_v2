#!/usr/bin/python3
"""  a script that starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ return hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """ return text"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/(<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """ return python is cool as default"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """return n is a number if it is"""
    return "{} is a number".format(n)



@app.route('/number_template/<int:n>', strict_slashes=False)
def index(n):
    """display an html page  only if n is an int"""
    return render_template('5-number.html', variable=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

