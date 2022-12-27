"""
This will compile and save the data based on the site data.
"""

from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.file_parser import read_json_file, write_json_file

def compile_data(site_data: dict):
    """
    This will compile the data and save the data.
    Args:
        site_data (dict): The site data.
    """
    data_file = site_data["file"]
    do_write = False
    data = read_json_file(f"data/{data_file}")
    links_list = read_json_file("data/links.json")

    create_log(f"Category: {site_data['category']}")

    if site_data["category"] == "Races" and site_data["location"] == "All":
        compile_season_summary_data(site_data, data)
        do_write = True
    elif site_data["category"] == "Races" and site_data["location"] != "All":
        compile_race_data(site_data, data)
        do_write = True
    elif site_data["category"] == "DRIVERS":
        compile_driver_data(site_data, data)
        do_write = True
    elif site_data["category"] == "Teams":
        compile_team_data(site_data, data)
        do_write = True

    if do_write:
        write_json_file(f"data/{data_file}", data)
        create_log(f"Data written to file: {data_file}")
        links_list.append(site_data["url"])
        create_log(f"Url added to links list: {site_data['url']}")
        write_json_file("data/links.json", links_list)
        create_log("Links list written to file: links.json")

def compile_season_summary_data(site_data: dict, data: dict):
    """
    This will compile the season summary data.
    Args:
        site_data (dict): The site data.
        data (dict): The data.
    """
    url = site_data["url"]
    year = site_data["year"]
    headers = site_data["headers"]
    rows = site_data["rows"]

    if year in data:
        create_log("Year already in data, skipping")
        log_to_console("Year already in data, skipping", "WARNING")
        return data

    sub_data = {
        "url": url,
        "headers": headers,
        "rows": rows
    }
    data[year] = sub_data
    return data

def compile_race_data(site_data: dict, data: dict):
    """
    This will the race result data.

    Args:
        site_data (dict): The site data.
        data (dict): The data.
    """
    url = site_data["url"]
    year = site_data["year"]
    location = site_data["location"]
    headers = site_data["headers"]
    rows = site_data["rows"]

    try:
        year_data = data[year]
    except KeyError as key_error:
        create_log(f"Key error: {key_error}")
        create_log("Year not found in data, assuming this is the first")
        create_log("Year data defaulting to empty dictionary")
        year_data = {}

    if location in year_data:
        create_log("Location already in data, skipping")
        log_to_console("Location already in data, skipping", "WARNING")
        return data

    sub_data = {
        "url": url,
        "headers": headers,
        "rows": rows
    }

    year_data[location] = sub_data
    data[year] = year_data
    return data

def compile_driver_data(site_data: dict, data: dict):
    """
    This will compile the driver data.

    Args:
        site_data (dict): The site data.
        data (dict): The data.
    """
    url = site_data["url"]
    year = site_data["year"]
    driver = site_data["driver"]
    headers = site_data["headers"]
    rows = site_data["rows"]

    try:
        year_data = data[year]
    except KeyError as key_error:
        create_log(f"Key error: {key_error}")
        create_log("Year not found in data, assuming this is the first")
        create_log("Year data defaulting to empty dictionary")
        year_data = {}

    if driver in year_data:
        create_log("Driver already in data, skipping")
        log_to_console("Driver already in data, skipping", "WARNING")
        return data

    sub_data = {
        "url": url,
        "headers": headers,
        "rows": rows
    }

    year_data[driver] = sub_data
    data[year] = year_data
    return data

def compile_team_data(site_data: dict, data: dict):
    """
    This will compile the team data.

    Args:
        site_data (dict): The site data.
        data (dict): The data.
    """
    url = site_data["url"]
    year = site_data["year"]
    team = site_data["team"]
    headers = site_data["headers"]
    rows = site_data["rows"]

    try:
        year_data = data[year]
    except KeyError as key_error:
        create_log(f"Key error: {key_error}")
        create_log("Year not found in data, assuming this is the first")
        create_log("Year data defaulting to empty dictionary")
        year_data = {}

    if team in year_data:
        create_log("Team already in data, skipping")
        log_to_console("Team already in data, skipping", "WARNING")
        return data

    sub_data = {
        "url": url,
        "headers": headers,
        "rows": rows
    }

    year_data[team] = sub_data
    data[year] = year_data
    return data
