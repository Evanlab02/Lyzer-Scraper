"""
This module contains the controller for all user reporting endpoints.
"""

from flask import request

from source.file_parser import read_json_file, write_json_file

def incident_endpoint():
    """
    Endpoint for reporting any incidents/issues with any other services or
    this service.

    returns:
        A JSON response with the status of the request.
    """
    try:
        response_json = request.get_json()
        response_keys = response_json.keys()
        for key in response_keys:
            if key not in ["id", "timestamp", "message"]:
                raise ValueError("Invalid request body.")
        all_incidents = read_json_file("data/incidents.json")
        all_incidents[response_json["id"]] = {
            "timestamp": response_json["timestamp"],
            "message": response_json["message"]
        }
        write_json_file("data/incidents.json", all_incidents)
        return {
            "status": 200,
            "result": "success",
            "message": "Incident reported successfully."
        }, 200
    except ValueError as value_error:
        return {
            "status": 400,
            "result": "failure",
            "message": value_error.args[0],
            "data": None
        }, 400

def request_endpoint():
    """
    Endpoint for requesting new features or changes to existing features.

    returns:
        A JSON response with the status of the request.
    """
    try:
        response_json = request.get_json()
        response_keys = response_json.keys()
        for key in response_keys:
            if key not in ["id", "timestamp", "message"]:
                raise ValueError("Invalid request body.")
        all_requests = read_json_file("data/requests.json")
        all_requests[response_json["id"]] = {
            "timestamp": response_json["timestamp"],
            "message": response_json["message"]
        }
        write_json_file("data/requests.json", all_requests)
        return {
            "status": 200,
            "result": "success",
            "message": "Request submitted successfully."
        }, 200
    except ValueError as value_error:
        return {
            "status": 400,
            "result": "failure",
            "message": value_error.args[0],
            "data": None
        }, 400
