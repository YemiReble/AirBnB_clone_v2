#!/usr/bin/python3
"""
This is my first Flask program using python
"""


from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Function that return Hello HBNB when user
        make a request to our ip address.
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """The function display "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """This c function returns multiple
    stuff on the screen"""
    return "C " + text.replace("_", " ")


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    """This fucntion returns a default text "Python is"
    with an argument passed to it
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<n>')
def number(int: n):
    """This route fuction allow only integers to be
    passed into it, if not integer, it fails
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
