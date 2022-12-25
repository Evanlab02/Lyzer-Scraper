"""
This module will contain the logic for the backlog endpoint.
"""

from flask import request

from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.file_parser import read_json_file, write_json_file

def queue_endpoint():
    """Contains the logic for the backlog endpoint."""
    if request.method == "GET":
        return get_queue()
    if request.method == "POST":
        return add_to_queue()

def get_queue():
    """Return the backlog queue."""
    try:
        backlog = read_json_file("data/backlog.json")
        log_to_console("Sent backlog to client.")
        create_log("Sent backlog to client.")
        return backlog
    except FileNotFoundError:
        create_log("Internal server error: backlog file not found.")
        return {
            "result": "failure",
            "message": "Internal server error: backlog file not found."
        }

def add_to_queue():
    """Add a new item to the queue."""
    try:
        backlog = read_json_file("data/backlog.json")
        backlog.append(request.json)
        write_json_file("data/backlog.json", backlog)
        log_to_console("Added new item to backlog.")
        create_log("Added new item to backlog.")
        return {"result": "success"}
    except FileNotFoundError:
        create_log("Internal server error: backlog file not found.")
        return {
            "result": "failure",
            "message": "Internal server error: backlog file not found."
        }