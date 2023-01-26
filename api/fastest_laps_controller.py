"""
This module will contain the logic to get the fastest laps from the data files and
return to the client.
"""

from api.api_controller import get_data
from logs.console_logger import log_to_console
from logs.file_logger import create_log

def get_fastest_laps():
    """
    Get all the fastest laps from the data files and return to the client.

    Returns:
        (dict): A dictionary with all the fastest laps.
    """
    log_to_console("Client requested all fastest laps data.")
    create_log("Client requested all fastest laps data.")
    result = get_data("data/fastest_laps.json")
    return result.convert_to_json(), result.status

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
    result = get_data("data/fastest_laps.json", year)
    return result.convert_to_json(), result.status


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
    result = get_data("data/fastest_laps.json", year, location)
    return result.convert_to_json(), result.status
