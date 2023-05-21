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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
