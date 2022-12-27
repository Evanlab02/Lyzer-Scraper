"""
This module will contain the logic to parse the url and return the data.
"""
from logs.console_logger import log_to_console
from logs.file_logger import create_log

def parse_url(url: str):
    """
    Parse the url and return the data.

    Args:
        url (str): The url to parse.
    """
    log_to_console(f"{url}", "LINK")
    try:
        year = get_year(url)
        file = determine_file(url)
    except IndexError:
        log_to_console("Invalid url: url is not supported.", "ERROR")
        create_log("Invalid url: url is not supported.")
        return {
            "url": url,
            "year": "",
            "file": ""
        }
    create_log(f"Url parsed: {url}")
    create_log(f"Year parsed from url: {year}")
    create_log(f"File parsed from url: {file}")
    return {
        "url": url,
        "year": year,
        "file": file
    }

def get_year(url: str) -> str:
    """
    Return the year of the url.

    Args:
        url (str): The url to parse.

    Returns:
        str: The year from the url.
    """
    url_elements = url.split("/")
    create_log(f"Url elements: {url_elements}")
    return url_elements[6]

def determine_file(url: str) -> str:
    """
    Determine the file to write to.

    Args:
        url (str): The url to parse.

    Returns:
        str: The file to write to.
    """
    # Create a dictionary to map values of url_elements[-1] to values of file
    file_mapping = {
        "races.html": "season_summaries.json",
        "race-result.html": "races.json",
        "fastest-laps.html": "fastest_laps.json",
        "pit-stop-summary.html": "pit_stop_data.json",
        "starting-grid.html": "starting_grids.json",
        "qualifying.html": "qualifying.json",
        "practice-3.html": "practice3.json",
        "practice-2.html": "practice2.json",
        "practice-1.html": "practice1.json",
        "sprint-results.html": "sprints.json",
        "sprint-grid.html": "sprint_grids.json",
        "drivers.html": "drivers.json",
        "team.html": "teams.json",
        "team": "teams.json",
        "drivers": "drivers.json"
    }

    # Split the URL into elements
    url_elements = url.split("/")

    # Check if url_elements[-1] is in the dictionary
    file = file_mapping.get(url_elements[-1], "")
    if not file:
        file = file_mapping.get(url_elements[6], "")

    # If file is an empty string, it means the value of url_elements[-1]
    # was not found in the dictionary
    if not file:
        log_to_console(f"Invalid url: {url}", "ERROR")
        create_log(f"Invalid url: {url}")
        return file
    return file
