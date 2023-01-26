"""
This module will contain the logic for the flask web app.
"""

from flask import Flask

from api.backlog_controller import queue_endpoint, priority_queue
from api.fastest_laps_controller import (
    get_fastest_laps,
    get_fastest_laps_from_year,
    get_fastest_laps_year_and_location
)
from api.pit_stop_controller import (
    get_all_pitstops,
    get_pitstops_for_year,
    get_pitstops_for_year_and_location
)
from api.race_controller import get_races, get_races_from_year, get_races_from_year_and_location
from api.season_controller import get_seasons, get_season
from logs.console_logger import log_to_console

def assign_endpoints(app: Flask):
    """Assign endpoints to the flask app."""
    app.route("/")(get_version)
    app.route("/queue", methods=["GET", "POST"])(queue_endpoint)
    app.route("/queue/priority", methods=["POST"])(priority_queue)

    app.route("/fastest_laps", methods=["GET"])(get_fastest_laps)
    app.route("/fastest_laps/<year>", methods=["GET"])(get_fastest_laps_from_year)
    app.route("/fastest_laps/<year>/<location>", methods=["GET"])\
        (get_fastest_laps_year_and_location)

    app.route("/pitstops", methods=["GET"])(get_all_pitstops)
    app.route("/pitstops/<year>", methods=["GET"])(get_pitstops_for_year)
    app.route("/pitstops/<year>/<location>", methods=["GET"])(get_pitstops_for_year_and_location)

    app.route("/races", methods=["GET"])(get_races)
    app.route("/races/<year>", methods=["GET"])(get_races_from_year)
    app.route("/race/<year>/<location>", methods=["GET"])(get_races_from_year_and_location)

    app.route("/seasons", methods=["GET"])(get_seasons)
    app.route("/season/<season_year>", methods=["GET"])(get_season)

    app.after_request(display_response)

def get_version():
    """Return the version of the lyzer scraper program."""
    return {
        "status": 200,
        "result": "success",
        "message": "Data retrieved successfully.",
        "data": "0.6.1-beta"
        }, 200

def display_response(response):
    """Display the response to the server user."""
    response_data = response.json
    response_data = response_data.copy()
    log_to_console("Sending following response to client")
    for key in response_data.keys():
        value = response_data[key]
        if len(str(value)) > 45:
            value = str(value)
            value = f"{len(value)} characters"
        log_to_console(f"{key} -> {value}", "MESSAGE")
    return response
