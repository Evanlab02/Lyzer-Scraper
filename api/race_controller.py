"""
This module will contain the logic to get the race data from the data files and
return to the client.
"""

from api.api_controller import get_data
from logs.console_logger import log_to_console
from logs.file_logger import create_log

def get_races():
    """
    Get all the race data from the data files and return to the client.

    Returns:
        (dict): A dictionary with all the races data.
    """
    log_to_console("Client requested all race data.")
    create_log("Client requested all race data.")
    result = get_data("data/races.json")
    return result.convert_to_json(), result.status

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
    result = get_data("data/races.json", year)
    return result.convert_to_json(), result.status

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
    result = get_data("data/races.json", year, location)
    return result.convert_to_json(), result.status
