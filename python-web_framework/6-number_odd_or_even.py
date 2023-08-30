#!/usr/bin/python3
"""
This module contains the code for a simple Flask web application.
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    """
    The application has a single route, `/`,
    which calls the `index()` function
    """
    return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
    return "HBNB"

@app.route("/c/<text>")
def text_display(text):
    """
    Display "C " followed by the value of the text variable.
    Replace underscores with spaces
    """
    text = text.replace('_', ' ')
    return "C {}".format(text)

@app.route("/python/")
@app.route("/python/<text>")
def display_text(text="is cool"):
    text_with_spaces = text.replace('_', ' ')
    return "Python {}".format(text_with_spaces)

@app.route("/number/<int:n>")
def display_number(n):
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>")
def display_templates(n):
    return render_template("5-number.html", number=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n):
    """ 
    Display a HTML page with the number's odd/even status using a template.
    """
    result = "even" if n % 2 == 0 else "odd"
    return "6-number_odd_or_even.html", number=n, result=result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)