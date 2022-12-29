"""
This module will contain the logic to get the fastest laps from the data files and
return to the client.
"""

from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.file_parser import read_json_file

def get_fastest_laps():
    """
    Get all the fastest laps from the data files and return to the client.

    Returns:
        (dict): A dictionary with all the fastest laps.
    """
    status_code = 500
    fastest_laps = {
        "result": "failure",
        "message": "Internal server error: fastest laps file not found."
    }

    try:
        create_log("Client requested all fastest laps data.")
        fastest_laps = read_json_file("data/fastest_laps.json")
        create_log("Sending fastest laps data to client.")
        status_code = 200
        log_to_console("Sent - All fastest laps data.", "MESSAGE")
    except FileNotFoundError:
        create_log("Internal server error: fastest laps file not found.")
        log_to_console("Internal server error: fastest laps file not found.", "ERROR")
    return fastest_laps, status_code
