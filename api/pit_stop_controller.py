"""
This file contains the controller for the pit stop data.
"""

# File Imports
from api.scraper_response import ScraperResponse
from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.file_parser import read_json_file

def read_pitstops_file() -> ScraperResponse | dict:
    """
    This function will read the pit stops data from the file and return it.
    If the file cannot be found, it will return a ScraperResponse object with the error message.

    Returns:
        (ScraperResponse | dict): A ScraperResponse object with error data or a dictionary
        with all the pit stop data.
    """
    try:
        pit_stop_data = read_json_file("data/pit_stop_data.json")
        return pit_stop_data
    except FileNotFoundError:
        create_log("Internal server error: pit stops file not found.")
        log_to_console("Internal server error: pit stops file not found.", "ERROR")
        return ScraperResponse("failure", 500, "Internal server error: pit stops file not found.")


def get_all_pitstops() -> tuple[dict[str, any], int]:
    """
    This function will return all the pit stop data that is stored in the file.

    Returns:
        (ScraperResponse): A ScraperResponse object with error data or pit stop data.
    """
    create_log("Retrieving pit stop data.")
    log_to_console("Retrieving pit stop data.", "INFO")
    result = read_pitstops_file()

    if isinstance(result, ScraperResponse):
        json_result = result.convert_to_json()
        return json_result, result.status

    result = ScraperResponse("success", 200, "Pit stop data retrieved successfully.", result)
    json_result = result.convert_to_json()
    create_log("Pit stop data retrieved successfully.")
    log_to_console("Pit stop data retrieved successfully.", "INFO")
    print("Check here ->",json_result)
    return json_result, result.status
