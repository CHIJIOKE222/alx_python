#!/usr/bin/python3

"""
This module starts a Flask web application using routes for specific URLs.

It defines routes and handlers for different URLs to demonstrate
the basic usage of the Flask web framework.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    A route handler for the root URL '/'. It returns a greeting message.

    Returns:
        str: Greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    A route handler for the URL '/hbnb'. It returns a message "HBNB".

    Returns:
        str: Message "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    A route handler for the URL '/c/<text>'. 
    It returns a message "C " followed by the value of the text variable.
    Replace underscore _ symbols with a space.

    Args:
        text (str): The value of the text variable.

    Returns:
        str: Message "C " followed by the value of the text variable.
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    A route handler for the URL '/python/(<text>)'. 
    It returns a message "Python " followed by the value of the text variable.
    Replace underscore _ symbols with a space.

    Args:
        text (str): The value of the text variable.

    Returns:
        str: Message "Python " followed by the value of the text variable.
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<n>', strict_slashes=False)
def number_n(n):
    """
    A route handler for the URL '/number/<n>'. 
    It returns a message "n " is a number only if it is an integer.


    Args:
        n (int): The value of the number.

    Returns:
        str: Message "n " is a number.
    """
    if n.isdigit():
        return "{} is a number".format(n)
    else:
        return "404", 404


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_n(n):
    """
    A route handler for the URL '/number_template/<n>'. 
    It returns an HTML page with an H1 tag containing "Number: n".

    Args:
        n (int): The value of the number.

    Returns:
        str: HTML page with the H1 tag.
    """

    try:
        n_int = int(n)
        return render_template('5-number.html', n=n_int)
    except ValueError:
        return "404 Not Found", 404


@app.route('/number_odd_or_even/<n>')
def odd_or_even(n):
    """ 
    A route handler for the URL '/number_odd_or_even/<n>'. 
    It returns an HTML page with an H1 tag containing "Number: n is even|odd".

    Args:
        n(int): The value of the number

    Returns:
           str: HTML page with the H1 tag.
    """

    try:
        n_int = int(n)  # convert n to an integer
        if n_int % 2 == 0:
            return render_template('6-number_odd_or_even.html', n=n_int, status='even')
        else:
            return render_template('6-number_odd_or_even.html', n=n_int, status='odd')
    except ValueError:  # n is not a valid number
        return "404 Not Found", 404


if __name__ == '__main__':
    """
    Main entry point of the script. Starts the Flask app.
    """
    app.run(host='0.0.0.0', port=5000)