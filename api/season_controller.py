"""
This module will contain the logic to get the seasons summary data from the data files and
return to the client.
"""

from source.file_parser import read_json_file

def get_seasons():
    """Get the seasons summary data from the data files and return to the client."""
    seasons = read_json_file("data/season_summaries.json")
    return seasons
