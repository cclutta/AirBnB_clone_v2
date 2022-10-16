#!/usr/bin/python3
""" Flask hello_route script. """
from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
