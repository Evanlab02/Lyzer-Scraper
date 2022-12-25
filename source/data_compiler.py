"""
This will compile and save the data based on the site data.
"""

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

    if site_data["location"] == "All" and site_data["category"] == "Races":
        compile_season_summary_data(site_data, data)
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
        return data

    sub_data = {
        "url": url,
        "headers": headers,
        "rows": rows
    }
    data[year] = sub_data

    return data
