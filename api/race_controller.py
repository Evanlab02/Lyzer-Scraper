"""
This module will contain the logic to get the race data from the data files and
return to the client.
"""

from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.file_parser import read_json_file

def get_races():
    """
    Get all the race data from the data files and return to the client.

    Returns:
        (dict): A dictionary with all the races data.
    """
    race_data = {
        "result": "failure",
        "message": "Internal server error: race file not found."
    }

    try:
        create_log("Client requested all race data.")
        race_data = read_json_file("data/races.json")
        create_log("Sending race data to client.")
        log_to_console("Sent - All race data.")
    except FileNotFoundError:
        create_log("Internal server error: race file not found.")
        log_to_console("Internal server error: race file not found.", "ERROR")
    return race_data
