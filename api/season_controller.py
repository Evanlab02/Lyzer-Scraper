"""
This module will contain the logic to get the seasons summary data from the data files and
return to the client.
"""

from api.api_controller import get_data
from logs.console_logger import log_to_console
from logs.file_logger import create_log

def get_seasons():
    """Get the seasons summary data from the data files and return to the client."""
    log_to_console("Client requested all seasons data.")
    create_log("Client requested all seasons data.")
    result = get_data("data/season_summaries.json")
    return result.convert_to_json(), result.status

def get_season(season_year: str) -> dict:
    """Get the season data from the data files and return to the client."""
    log_to_console(f"Client requested seasons data for {season_year}.")
    create_log(f"Client requested seasons data for {season_year}.")
    result = get_data("data/season_summaries.json", season_year)
    return result.convert_to_json(), result.status
