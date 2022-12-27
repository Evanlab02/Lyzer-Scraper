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
    url_elements = url.split("/")
    if url_elements[-1] == "races.html":
        file = "season_summaries.json"
    elif url_elements[-1] == "race-result.html":
        file = "races.json"
    elif url_elements[-1] == "fastest-laps.html":
        file = "fastest_laps.json"
    elif url_elements[-1] == "pit-stop-summary.html":
        file = "pit_stop_data.json"
    elif url_elements[-1] == "starting-grid.html":
        file = "starting_grids.json"
    elif url_elements[-1] == "qualifying.html":
        file = "qualifying.json"
    elif url_elements[-1] == "practice-3.html":
        file = "practice3.json"
    elif url_elements[-1] == "practice-2.html":
        file = "practice2.json"
    elif url_elements[-1] == "practice-1.html":
        file = "practice1.json"
    elif url_elements[-1] == "sprint-results.html":
        file = "sprints.json"
    elif url_elements[-1] == "sprint-grid.html":
        file = "sprint_grids.json"
    elif url_elements[-1] == "drivers.html" or url_elements[6] == "drivers":
        file = "drivers.json"
    elif url_elements[-1] == "team.html" or url_elements[6] == "team":
        file = "teams.json"
    else:
        file = ""
        log_to_console(f"Invalid url: {url}", "ERROR")
        create_log(f"Invalid url: {url}")
    return file
