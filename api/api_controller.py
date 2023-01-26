"""
This module will contain functions that all controllers will use.
"""

from api.scraper_response import ScraperResponse
from source.file_parser import read_json_file

def get_data(file: str, year: str = "", location: str = ""):
    """
    This function will return the data from the file based on the year and location.
    If no year is given, it will return all the data.
    If no location is given, it will return all the data for the year.

    Args:
        file (str): The file to read the data from.
        year (str, optional): The year to get the data for. Defaults to "".
        location (str, optional): The location to get the data for. Defaults to "".

    Returns:
        (ScraperResponse): A ScraperResponse object with error data or data.
    """
    location = location.replace("_", " ")
    try:
        data = read_json_file(f"{file}")
    except FileNotFoundError:
        return ScraperResponse("failure", 500, "Internal server error: file not found.")

    if year:
        try:
            data = data[year]
        except KeyError:
            return ScraperResponse("failure", 404, f"Year not found {year}.")

    if year and location:
        try:
            data = data[location]
        except KeyError:
            return ScraperResponse("failure", 404, f"Location not found {location}.")

    return ScraperResponse("success", 200, "Data retrieved successfully.", data)
