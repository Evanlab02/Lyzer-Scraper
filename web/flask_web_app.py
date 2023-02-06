"""
This module will contain the logic for the flask web app.
"""

from flask import Flask
from waitress import serve

def create_app():
    """Create and configure the flask app."""
    app = Flask(__name__)
    return app

def host_app(app: Flask, selected_port: int = 8000):
    """
    Host the flask app.
    """
    serve(app, port=selected_port)
