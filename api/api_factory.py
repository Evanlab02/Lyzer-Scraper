"""
This module will contain the logic for the flask web app.
"""

from flask import Flask

from api.api_controller import data_endpoint
from api.backlog_controller import queue_endpoint, priority_queue

def assign_endpoints(app: Flask):
    """Assign endpoints to the flask app."""
    app.route("/")(get_version)
    app.route("/queue", methods=["GET", "POST"])(queue_endpoint)
    app.route("/queue/priority", methods=["POST"])(priority_queue)

    app.route("/data/<data_type>", methods=["GET"])(data_endpoint)
    app.route("/data/<data_type>/<year>", methods=["GET"])(data_endpoint)
    app.route("/data/<data_type>/<year>/<location_driver_team>", methods=["GET"])(data_endpoint)

def get_version():
    """Return the version of the lyzer scraper program."""
    return {
        "status": 200,
        "result": "success",
        "message": "Data retrieved successfully.",
        "data": "1.0.0"
        }, 200
