#!/usr/bin/python3
"""Flask web application that render all states"""

from flask import Flask, render_template
from models.state import State
from models.city import City
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def city_list():
    """
    This method is a Flask route that renders a template to display
    all States in an HTML page
    """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


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
