"""
This module will contain the logic to get the race data from the data files and
return to the client.
"""

from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.file_parser import read_json_file

def race_file_not_found():
    """
    This function will return the default response for when the race file cannot be found.

    Returns:
        (dict): A dictionary with the default response for when the race file cannt be found.
    """
    create_log("Internal server error: race file not found.")
    log_to_console("Internal server error: race file not found.", "ERROR")
    return {
        "status": 500,
        "result": "failure",
        "message": "Internal server error: race file not found."
    }

def generate_race_data():
    """
    This function will read the race data from the file and return it.

    Returns:
        (dict): A dictionary with all the race data from the file.
    """
    race_data = read_json_file("data/races.json")
    response = {}
    response["data"] = race_data
    status_code = 200
    response["status"] = status_code
    response["result"] = "success"
    response["message"] = "Races - All time"
    return response, status_code

def year_not_found():
    """"
    This function will return the default response for when the data for the given year cannot be
    found.

    Returns:
        (dict): A dictionary with the default response for when the data cannot be found.
    """
    status_code = 404
    create_log("Updated status code to bad request (404)")
    create_log("BAD REQUEST: Year not found.")
    log_to_console("BAD REQUEST: Year not found.", "WARNING")
    return {
        "status": status_code,
        "result": "failure",
        "message": "BAD REQUEST: Year not found."
    }, status_code

def location_not_found():
    """"
    This function will return the default response for when the data for the given location
    cannot be found.

    Returns:
        (dict): A dictionary with the default response for when the data cannot be found.
    """
    status_code = 404
    create_log("Updated status code to bad request (404)")
    create_log("BAD REQUEST: Location not found.")
    log_to_console("BAD REQUEST: Location not found.", "WARNING")
    return {
        "status": status_code,
        "result": "failure",
        "message": "BAD REQUEST: Location not found."
    }, status_code

def get_races():
    """
    Get all the race data from the data files and return to the client.

    Returns:
        (dict): A dictionary with all the races data.
    """
    log_to_console("Client requested all race data.")
    create_log("Client requested all race data.")
    create_log("Defaulted to 'internal server error' (500) status code.")

    status_code = 500

    try:
        response, status_code = generate_race_data()
        create_log("Sending response to client")
        log_to_console("Sending response to client", "SUCCESS")
    except FileNotFoundError:
        response = race_file_not_found()

    return response, status_code

def get_races_from_year(year: str):
    """
    Gets all the race data from the data files for the selected year and returns it to the client.

    Args:
        year (str): The year

    Returns:
        (dict): A dictionary with all the race data for the selected year.
    """
    log_to_console(f"Client requested race data for the year {year}")
    create_log(f"Client requested race for the year {year}")
    create_log("Defaulted to 'internal server error' (500) status code.")

    status_code = 500

    try:
        response, status_code = generate_race_data()
        response["data"] = response["data"][year]
        response["message"] = f"Races for year {year}"
        create_log("Sending response to client")
        log_to_console("Sending response to client", "SUCCESS")
    except FileNotFoundError:
        response = race_file_not_found()
    except KeyError:
        response, status_code = year_not_found()

    return response, status_code

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
    log_to_console(f"Client requested race data for the year {year} and location {location}")
    create_log(f"Client requested race for the year {year} and location {location}")
    create_log("Defaulted to 'internal server error' (500) status code.")

    location = location.replace("_", " ")
    status_code = 500

    try:
        response, status_code = generate_race_data()
        response["data"] = response["data"][year]
    except FileNotFoundError:
        response = race_file_not_found()
        return response, status_code
    except KeyError:
        response, status_code = year_not_found()
        return response, status_code

    try:
        response["data"] = response["data"][location]
        response["message"] = f"Races for year {year} and location {location}"
        create_log("Sending response to client")
        log_to_console("Sending response to client", "SUCCESS")
    except KeyError:
        response, status_code = location_not_found()

    return response, status_code
