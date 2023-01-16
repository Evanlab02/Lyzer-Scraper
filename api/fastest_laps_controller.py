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
    status_code = 500
    fastest_laps = {
        "result": "failure",
        "message": "Internal server error: fastest laps file not found."
    }

    try:
        create_log("Client requested all fastest laps data.")
        fastest_laps = read_json_file("data/fastest_laps.json")
        create_log("Sending fastest laps data to client.")
        status_code = 200
        log_to_console("Sent - All fastest laps data.", "MESSAGE")
    except FileNotFoundError:
        create_log("Internal server error: fastest laps file not found.")
        log_to_console("Internal server error: fastest laps file not found.", "ERROR")
    return fastest_laps, status_code

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
        response.update(fastest_laps)
        response["status"] = 200
        response["result"] = "success"
        response["message"] = f"Fastest laps data for year: {year}"
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
