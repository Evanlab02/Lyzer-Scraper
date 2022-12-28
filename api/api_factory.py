"""
This module will contain the logic for the flask web app.
"""

from flask import Flask

from api.backlog_controller import queue_endpoint, priority_queue
from api.season_controller import get_seasons, get_season


def assign_endpoints(app: Flask):
    """Assign endpoints to the flask app."""
    app.route("/")(get_version)
    app.route("/queue", methods=["GET", "POST"])(queue_endpoint)
    app.route("/queue/priority", methods=["POST"])(priority_queue)
    app.route("/seasons", methods=["GET"])(get_seasons)
    app.route("/season/<season_year>", methods=["GET"])(get_season)

def get_version():
    """Return the version of the lyzer scraper program."""
    return {"version": "0.5.0"}
