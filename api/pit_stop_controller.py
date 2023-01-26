"""
This file contains the controller for the pit stop data.
"""

# File Imports
from api.api_controller import get_data
from logs.console_logger import log_to_console
from logs.file_logger import create_log


def get_all_pitstops() -> tuple[dict[str, any], int]:
    """
    This function will return all the pit stop data that is stored in the file.

    Returns:
        (ScraperResponse): A ScraperResponse object with error data or pit stop data.
    """
    create_log("Retrieving pit stop data.")
    log_to_console("Retrieving pit stop data.", "INFO")
    result = get_data("data/pit_stop_data.json")
    return result.convert_to_json(), result.status


def get_pitstops_for_year(year) -> tuple[dict[str, any], int]:
    """
    This function will return the pit stop data for the given year.

    Args:
        year (str): The year to get the pit stop data for.

    Returns:
        (tuple[dict[str, any], int]): A tuple containing the response and the status code.
    """
    create_log(f"Retrieving pit stop data for {year}.")
    log_to_console(f"Retrieving pit stop data for {year}.", "INFO")
    result = get_data("data/pit_stop_data.json", year)
    return result.convert_to_json(), result.status
