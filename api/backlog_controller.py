"""
This module will contain the logic for the backlog endpoint.
"""

from flask import request

from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.data_compiler import compile_data
from source.file_parser import read_json_file, write_json_file
from source.site_scraper import parse_site
from source.url_parser import parse_url

def invalid_method():
    """Return an error for an invalid method."""
    return {
        "status": 500,
        "result": "failure",
        "message": "Internal Server Error: Invalid method."
    }

def backlog_file_not_found():
    """Return an error for a missing backlog file."""
    return {
        "status": 500,
        "result": "failure",
        "message": "Internal Server Error: Backlog file not found."
    }

def queue_endpoint():
    """Contains the logic for the backlog endpoint."""
    message = invalid_method()
    if request.method == "GET":
        message = get_queue()
    if request.method == "POST":
        message = add_to_queue()
    return message

def get_queue():
    """Return the backlog queue."""
    create_log("Client requested backlog.")
    log_to_console("Client requested backlog.")

    try:
        backlog = read_json_file("data/backlog.json")
        backlog = {"queue": backlog}
        backlog["status"] = 200
        backlog["result"] = "success"
        backlog["message"] = "Backlog retrieved successfully."
        log_to_console("Sending backlog to client.")
        create_log("Sending backlog to client.")
    except FileNotFoundError:
        create_log("Internal server error: backlog file not found.")
        log_to_console("Internal server error: backlog file not found.", "ERROR")
        backlog = backlog_file_not_found()
    return backlog, backlog["status"]

def add_to_queue():
    """Add a new item to the queue."""
    response = backlog_file_not_found()

    create_log("Client requested to add new item to backlog.")
    log_to_console("Client requested to add new item to backlog.")
    try:
        backlog = read_json_file("data/backlog.json")
        backlog.append(request.json)
        write_json_file("data/backlog.json", backlog)
        log_to_console("Added new item to backlog.")
        create_log("Added new item to backlog.")
        response["status"] = 200
        response["result"] = "success"
        response["message"] = "Item added to backlog successfully."
    except FileNotFoundError:
        create_log("Internal server error: backlog file not found.")
        log_to_console("Internal server error: backlog file not found.", "ERROR")
    return response, response["status"]

def priority_queue():
    """Immediately process the item given."""
    request_data = request.json
    url = request_data["url"]
    return scrape(url)

def scrape(url: str):
    """Scrape the url given."""
    links = read_json_file("data/links.json")
    if url in links:
        create_log("Url already scraped.")
        log_to_console("Url already scraped, ignoring link.", "WARNING")
        log_to_console("Skipped.")
        return {
            "status": 200,
            "result": "ignored",
            "message": "Url already scraped."
        }, 200

    log_to_console("Processing following url immediately.", "WARNING")
    create_log(f"Processing following url immediately: {url}")
    site_data = parse_url(url)

    if not site_data["file"]:
        create_log("Invalid url received.")
        return {
            "status": 400,
            "result": "failure",
            "message": "Invalid url: url is not supported."
        }, 400

    parse_site(site_data)
    compile_data(site_data)
    log_to_console("Processed url.", "SUCCESS")
    return {
            "status": 200,
            "result": "success",
            "message": "Url processed successfully."
        } , 200
