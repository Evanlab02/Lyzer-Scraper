"""
This module will contain the logic to get the fastest laps from the data files and
return to the client.
"""

from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.file_parser import read_json_file

def get_fastest_laps():
    """
    Get all the fastest laps from the data files and return to the client.

    Returns:
        (dict): A dictionary with all the fastest laps.
    """
    log_to_console("Client requested all fastest laps data.")
    create_log("Client requested all fastest laps data.")

    try:
        create_log("Attempting to read fastest laps data now.")
        fastest_laps = read_json_file("data/fastest_laps.json")
        create_log("Fastest laps data read successfully.")
        response = {
            "status": 200,
            "result": "success",
            "message": "Fastest laps - All",
            "data": fastest_laps
            }
        create_log("Sending response to client: Fastest laps - All")
        log_to_console("Sent - Fastest laps - All")
    except FileNotFoundError:
        create_log("Internal server error: fastest laps file not found.")
        log_to_console("Internal server error: fastest laps file not found.", "ERROR")
        response = {
            "status": 500,
            "result": "failure",
            "message": "Internal server error: fastest laps file not found."
        }
    return response, response["status"]

def get_fastest_laps_from_year(year: str):
    """
    Get all the fastest laps from the data files and return to the client.

    Args:
        year (str): The year to get the fastest laps from.

    Returns:
        (dict): A dictionary with all the fastest laps.
    """
    create_log(f"Client requested fastest laps data from {year}.")
    log_to_console(f"Client requested fastest laps data for {year}")

    create_log("Defaulting to 500 status code until data is found.")
    response = {
        "status": 500,
        "result": "failure",
        "message": "Internal server error: fastest laps file not found."
    }

    try:
        create_log(f"Attempting to read fastest laps data for year({year}) now.")
        fastest_laps = read_json_file("data/fastest_laps.json")
        fastest_laps = fastest_laps[year]
        response = {
            "data": fastest_laps,
            "status": 200,
            "result": "success",
            "message": f"Fastest laps data for year: {year}"
        }
    except FileNotFoundError:
        create_log("Internal server error: fastest laps file not found.")
        log_to_console("Internal server error: fastest laps file not found.", "ERROR")
    except KeyError:
        create_log(f"Data not found for year: {year}")
        log_to_console(f"Data not found for year: {year}", "ERROR")
        response["message"] = f"Data not found for year: {year}"
        response["status"] = 404

    create_log(f"Sending response to client: {response['message']}")
    log_to_console(f"Sent - {response['message']}")
    return response, response["status"]


def get_fastest_laps_year_and_location(year, location):
    """
    Get all the fastest laps from the data files for a specific year and location and
    return to the client.

    Args:
        year (str): The year of the event.
        location (str): The location of the event.

    Returns:
        (dict): A dictionary with all the fastest laps for an event.
    """
    location = location.replace("_", " ")
    create_log(f"Client requested fastest laps data from {year} at {location}.")
    log_to_console(f"Client requested fastest laps data for {year} at {location}")
    try:
        create_log("Reading data file (fastest_laps.json) now.")
        fastest_laps = read_json_file("data/fastest_laps.json")
        create_log("Compiling response now.")
        fastest_laps = fastest_laps[year][location]
        response = {
            "data": fastest_laps,
            "status": 200,
            "result": "success",
            "message": f"Fastest laps data for year: {year} at {location}"
        }
        create_log(f"Sending response to client: {response['message']}")
        log_to_console(f"Sent - {response['message']}")
    except FileNotFoundError:
        create_log("Internal server error: fastest laps file not found.")
        log_to_console("Internal server error: fastest laps file not found.", "ERROR")
        response = {
            "status": 500,
            "result": "failure",
            "message": "Internal server error: fastest laps file not found."
        }
    except KeyError:
        create_log(f"Data not found for year: {year} at {location}")
        log_to_console(f"Data not found for year: {year} at {location}", "ERROR")
        response = {
            "status": 404,
            "result": "failure",
            "message": f"Data not found for year: {year} at {location}"
        }
    return response, response["status"]
