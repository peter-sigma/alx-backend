#!/usr/bin/env python3

"""

"""

from flask import Flask,  render_template
from flask_babel import Babel

class Config:
    """
       Configuring babel object
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)
babel.init_app(app)


@app.route("/", strict_slashes=False)
def hello_holberton():
    """
       A function to return hello world
    """""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
