#!/usr/bin/python3
"""
This is my first Flask program using python
"""


from flask import Flask, render_template

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


@app.route('/number/<int:n>')
def number(n):
    """
    Displays "<n> is a number" when the /number/<n> URL is accessed,
            but only if n is an integer.
    Args:
        n (int): The number to display.
    Returns:
        str: The complete string to display, or an error message
        if n is not an integer.
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n=None):
    """display a HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n=None):
    """display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    if isinstance(n, int):
        if n % 2:
            num = "odd"
        else:
            num = "even"
        return render_template("6-number_odd_or_even.html", n=n, num=num)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
