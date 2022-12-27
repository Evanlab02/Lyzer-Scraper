"""
This module will contain the logic for the flask web app.
"""

from flask import Flask, request

from api.backlog_controller import queue_endpoint
from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.data_compiler import compile_data
from source.file_parser import read_json_file
from source.site_scraper import parse_site
from source.url_parser import parse_url


def assign_endpoints(app: Flask):
    """Assign endpoints to the flask app."""
    app.route("/")(get_version)
    app.route("/queue", methods=["GET", "POST"])(queue_endpoint)
    app.route("/queue/priority", methods=["POST"])(priority_queue)

def get_version():
    """Return the version of the lyzer scraper program."""
    return {"version": "0.5.0"}

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
