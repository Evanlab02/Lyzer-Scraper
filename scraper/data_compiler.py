"""
This module will contain the logic to compile all the data
from the scraped site with the loaded data into a single map.
"""

import sys

def compile_data(url_data: list, headers: list, data_rows: list, json_data: dict) -> dict:
    """
    This function will compile all the data from the scraped site
    with the loaded data into a single map.

    Args:
        url_data (list): The data from the scraped site.
        headers (list): The headers from the scraped site.
        data_rows (list): The data rows from the scraped site.
        json_data (dict): The loaded data.

    Returns:
        dict: The compiled data.
    """
    json_data = edit_data_with_year(json_data, url_data[1])
    json_data = edit_data_with_location(json_data, url_data[1], url_data[2])
    json_data[str(url_data[1])][url_data[2]] = {"Headers": headers, "Data": data_rows}
    return json_data

def edit_data_with_year(data: dict, year: int) -> dict:
    """
    This function will edit the data with the given year.
    If the year already exists in the data, it will return the data.

    Args:
        data (dict): The data to edit.
        year (int): The year to edit the data with.

    Returns:
        dict: The edited data.
    """
    if str(year) not in data.keys():
        data[str(year)] = {}
    else:
        print("[INFO] The year already exists in the data.")

    return data

def edit_data_with_location(data: dict, year:int, location: str) -> dict:
    """
    This function will edit the data with the given location.

    Args:
        data (dict): The data to edit.
        year (int): The year to edit the data with.
        location (str): The location to edit the data with.

    Returns:
        dict: The edited data.
    """
    json_data = data[str(year)]
    if location not in json_data.keys():
        data[str(year)][location] = {}
    else:
        print("The location already exists in the data.")
        if input("Press enter to continue") != "":
            sys.exit(0)

    return data
