"""Module with the api routes"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Hello World!"""
    return "<p>Hello, World!</p>"
