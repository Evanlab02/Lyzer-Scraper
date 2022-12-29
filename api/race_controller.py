"""
This module will contain the logic to get the race data from the data files and
return to the client.
"""

from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.file_parser import read_json_file

def get_races():
    """
    Get all the race data from the data files and return to the client.

    Returns:
        (dict): A dictionary with all the races data.
    """
    race_data = {
        "result": "failure",
        "message": "Internal server error: race file not found."
    }

    try:
        create_log("Client requested all race data.")
        race_data = read_json_file("data/races.json")
        create_log("Sending race data to client.")
        log_to_console("Sent - All race data.")
    except FileNotFoundError:
        create_log("Internal server error: race file not found.")
        log_to_console("Internal server error: race file not found.", "ERROR")
    return race_data

def get_races_from_year(year: str):
    """
    Gets all the race data from the data files for the selected year and returns it to the client.

    Args:
        year (str): The year

    Returns:
        (dict): A dictionary with all the race data for the selected year.
    """
    create_log(f"Client requested race data for the year {year}")
    race_data = {
        "result": "failure",
        "message": "Internal server error: race file not found."
    }
    create_log("Defaulted race data to 'internal server error: race file not found.'")

    try:
        race_data = read_json_file("data/races.json")
    except FileNotFoundError as error:
        create_log("Internal server error: race file not found.")
        create_log(f"Error: {error}")
        log_to_console("Internal server error: race file not found.", "WARNING")
        log_to_console("Sent - Internal server error", "MESSAGE")
        return race_data, 500

    try:
        year_race_data = race_data[year]
    except KeyError as error:
        create_log(f"Internal server error: year {year} not found.")
        create_log(f"Error: {error}")
        log_to_console(f"Internal server error: year {year} not found.", "WARNING")
        log_to_console("Sent - Internal server error", "MESSAGE")
        return {
            "result": "failure",
            "message": f"Internal server error: year {year} not found."
        },500
    log_to_console(f"Sent - Race data for {year}", "MESSAGE")
    return year_race_data, 200

def get_races_from_year_and_location(year: str, location: str):
    """
    Gets all the races from the data files for the selected year and location and returns
    it to the client.

    Args:
        year (str): The year
        location (str): The location

    Returns:
        (dict): A dictionary with all the race data for the selected year and location.
    """
    location = location.replace("_", " ")
    year_race_data, status_code = get_races_from_year(year)
    if status_code == 500:
        return year_race_data, status_code

    try:
        location_race_data = year_race_data[location]
    except KeyError as error:
        create_log(f"Internal server error: location {location} not found.")
        create_log(f"Error: {error}")
        log_to_console(f"Internal server error: location {location} not found.", "WARNING")
        log_to_console("Sent - Internal server error", "MESSAGE")
        return {
            "result": "failure",
            "message": f"Internal server error: location {location} not found."
        }, 500
    return location_race_data, 200
