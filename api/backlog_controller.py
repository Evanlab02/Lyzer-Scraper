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

def queue_endpoint():
    """Contains the logic for the backlog endpoint."""
    message = {
        "result": "failure",
        "message": "invalid request method"
    }
    if request.method == "GET":
        message = get_queue()
    if request.method == "POST":
        message = add_to_queue()
    return message

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
            "result": "ignored",
            "message": "Url already scraped."
        }

    log_to_console("Processing following url immediately.", "WARNING")
    create_log(f"Processing following url immediately: {url}")
    site_data = parse_url(url)

    if not site_data["file"]:
        create_log("Invalid url received.")
        return {
            "result": "failure",
            "message": "Invalid url: url is not supported."
        }

    parse_site(site_data)
    compile_data(site_data)
    log_to_console("Processed url.", "SUCCESS")
    return {"result": "success"}
