#!/usr/bin/python3
"""
Flask web application that render all states
"""

from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def state_list():
    """
    This method is a Flask route that renders a template to display
    a list of all the states in the database.
    Returns: A Flask template that displays a list of all the
        states in the database.
    Raises: None.
    """
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown():
    """
    This method is a Flask teardown function that ends the SQLAlchemy session
    Returns: None.
    Raises: None.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
