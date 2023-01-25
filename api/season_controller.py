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
    seasons = read_json_file("data/season_summaries.json")
    season = {"message": "The season you requested was not found."}
    try:
        season = seasons[season_year]
    except KeyError as error:
        log_to_console(f"Season {season_year} not found.", "WARNING")
        log_to_console(error, "WARNING")
        create_log(f"Season {season_year} not found: {error}")
    log_to_console(f"Sent - Season {season_year} Data", "MESSAGE")
    return season
