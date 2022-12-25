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
    year = get_year(url)
    file = determine_file(url)
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
    return url_elements[-2]

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
    else:
        file = ""
        log_to_console(f"Invalid url: {url}", "ERROR")
        create_log(f"Invalid url: {url}")
    return file
