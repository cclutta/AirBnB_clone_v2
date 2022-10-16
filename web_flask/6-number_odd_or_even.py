#!/usr/bin/python3
""" Flask number_route script. """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
       Flask route at root.
       Displays Hello BNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
       Flask route at /hbnb.
       Displays BNB!
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
       Flask route at /c/<text>.
       Displays C + text
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
       Flask route at /python/(<text>).
       Displays Python + text
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
       Flask route at /number/<int:n>.
       Displays C + text
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
       Flask route at /number_template/<int:n>.
       Displays 5-number.html with n
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
       Flask route at /number_template/<int:n>.
       Displays 5-number.html with n
    """
    if (n % 2 == 0):
        t = "Number: {} is even".format(n)
    else:
        t = "Number: {} is odd".format(n)
    return render_template('6-number_odd_or_even.html', text=t)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
