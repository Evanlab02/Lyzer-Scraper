"""
This module will contain the logic to get the seasons summary data from the data files and
return to the client.
"""

from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.file_parser import read_json_file

def get_seasons():
    """Get the seasons summary data from the data files and return to the client."""
    seasons = read_json_file("data/season_summaries.json")
    log_to_console("Sent - Seasons Data", "MESSAGE")
    return seasons

def get_season(season_year: str):
    """Get the season data from the data files and return to the client."""
    seasons = read_json_file("data/season_summaries.json")
    try:
        season = seasons[season_year]
    except KeyError as error:
        log_to_console(f"Season {season_year} not found.", "WARNING")
        log_to_console(error, "WARNING")
        create_log(f"Season {season_year} not found: {error}")
        season = {}
    log_to_console(f"Sent - Season {season_year} Data", "MESSAGE")
    return season
