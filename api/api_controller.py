"""
This module will contain functions that all controllers will use.
"""

from api.scraper_response import ScraperResponse
from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.file_parser import read_json_file

def get_data(file: str, year: str = "", location: str = ""):
    """
    This function will return the data from the file based on the year and location.
    If no year is given, it will return all the data.
    If no location is given, it will return all the data for the year.

    Args:
        file (str): The file to read the data from.
        year (str, optional): The year to get the data for. Defaults to "".
        location (str, optional): The location to get the data for. Defaults to "".

    Returns:
        (ScraperResponse): A ScraperResponse object with error data or data.
    """
    location = location.replace("_", " ")

    if file == "data/":
        return ScraperResponse("failure", 404, "Data type not found.")

    try:
        data = read_json_file(f"{file}")
    except FileNotFoundError:
        return ScraperResponse("failure", 500, "Internal server error: file not found.")

    if year:
        try:
            data = data[year]
        except KeyError:
            return ScraperResponse("failure", 404, f"Year not found {year}.")

    if year and location:
        try:
            data = data[location]
        except KeyError:
            return ScraperResponse("failure", 404, f"Location not found {location}.")

    return ScraperResponse("success", 200, "Data retrieved successfully.", data)

def data_endpoint(data_type: str, year: str = "", location: str = ""):
    """
    This function will return the data from the file based on the year and location.

    Args:
        data_type (str): The data type to get the data for.
        year (str, optional): The year to get the data for. Defaults to "".
        location (str, optional): The location to get the data for. Defaults to "".

    Returns:
        (str): The data in json format.
    """
    log_to_console(f"Getting {data_type} data: {year} {location}")
    create_log(f"Getting {data_type} data: {year} {location}")
    file_name = get_file_name(data_type)
    file_name = f"data/{file_name}"
    result = get_data(file_name, year, location)
    display_response(result.convert_to_json())
    return result.convert_to_json(), result.status

def get_file_name(data_type: str) -> str:
    """
    This function will return the file name based on the data type.

    Args:
        data_type (str): The data type to get the file name for.

    Returns:
        (str): The file name.
    """
    file_name: str
    match data_type:
        case "seasons":
            file_name = "season_summaries.json"
        case "races":
            file_name = "races.json"
        case "pitstops":
            file_name = "pit_stop_data.json"
        case "fastest_laps":
            file_name = "fastest_laps.json"
        case "starting_grids":
            file_name = "starting_grids.json"
        case "qualifying":
            file_name = "qualifying.json"
        case _:
            file_name = ""
    return file_name

def display_response(response):
    """Display the response to the server user."""
    response_data = response.copy()
    log_to_console("Sending following response to client")
    for key in response_data.keys():
        value = response_data[key]
        if len(str(value)) > 45:
            value = str(value)
            value = f"{len(value)} characters"
        log_to_console(f"{key} -> {value}", "MESSAGE")
    return response
