"""
This module will contain the logic for the flask web app.
"""

from flask import Flask

from api.backlog_controller import queue_endpoint, priority_queue
from api.fastest_laps_controller import get_fastest_laps, get_fastest_laps_from_year
from api.race_controller import get_races, get_races_from_year, get_races_from_year_and_location
from api.season_controller import get_seasons, get_season


def assign_endpoints(app: Flask):
    """Assign endpoints to the flask app."""
    app.route("/")(get_version)
    app.route("/queue", methods=["GET", "POST"])(queue_endpoint)
    app.route("/queue/priority", methods=["POST"])(priority_queue)

    app.route("/races", methods=["GET"])(get_races)
    app.route("/races/fastest_laps", methods=["GET"])(get_fastest_laps)
    app.route("/races/fastest_laps/<year>", methods=["GET"])(get_fastest_laps_from_year)
    app.route("/races/<year>", methods=["GET"])(get_races_from_year)
    app.route("/race/<year>/<location>", methods=["GET"])(get_races_from_year_and_location)

    app.route("/seasons", methods=["GET"])(get_seasons)
    app.route("/season/<season_year>", methods=["GET"])(get_season)

def get_version():
    """Return the version of the lyzer scraper program."""
    return {"version": "0.6.0-beta"}
