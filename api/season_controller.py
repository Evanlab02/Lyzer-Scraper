"""
This module will contain the logic to get the seasons summary data from the data files and
return to the client.
"""

from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.file_parser import read_json_file

def get_seasons():
    """Get the seasons summary data from the data files and return to the client."""
    log_to_console("Client requested all seasons data.")
    create_log("Client requested all seasons data.")
    try:
        create_log("Reading seasons data from file.")
        seasons = read_json_file("data/season_summaries.json")
        create_log("Seasons data read successfully.")
        response = {
            "status": 200,
            "result": "success",
            "message": "All Seasons Data",
            "data": seasons
        }
        create_log("Seasons data compiled and ready to send.")
        log_to_console("Seasons data compiled and ready to send.", "SUCCESS")
    except FileNotFoundError:
        create_log("Internal server error: seasons file not found.")
        log_to_console("Internal server error: seasons file not found.", "ERROR")
        response = {
            "status": 500,
            "result": "failure",
            "message": "Internal server error: seasons file not found."
        }
    return response, response["status"]

def get_season(season_year: str) -> dict:
    """Get the season data from the data files and return to the client."""
    log_to_console(f"Client requested seasons data for {season_year}.")
    create_log(f"Client requested seasons data for {season_year}.")
    try:
        create_log("Reading season data from file.")
        seasons = read_json_file("data/season_summaries.json")
        create_log("Seasons data read successfully.")
        response = {
            "status": 200,
            "result": "success",
            "message": f"Season {season_year} Data",
            "data": seasons[season_year]
        }
        create_log(f"Season {season_year} data compiled and ready to send.")
        log_to_console(f"Season {season_year} data compiled and ready to send.", "SUCCESS")
    except FileNotFoundError:
        create_log("Internal server error: seasons file not found.")
        log_to_console("Internal server error: seasons file not found.", "ERROR")
        response = {
            "status": 500,
            "result": "failure",
            "message": "Internal server error: seasons file not found."
        }
    except KeyError:
        create_log(f"Season {season_year} not found.")
        log_to_console(f"Season {season_year} not found.", "ERROR")
        response = {
            "status": 404,
            "result": "failure",
            "message": f"Season {season_year} not found."
        }
    return response, response["status"]
