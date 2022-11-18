"""
This module will contain the logic to load and write data from and to a json file.
"""

import json

from rich import print as rich_print

def load_json_data(file_path: str):
    """
    This function will load the json data from the given file path.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        rich_print("This json file is empty.")
        rich_print("Defaulting to {}")
        data = {}
    except FileNotFoundError:
        rich_print("This file does not exist.")
        rich_print("Defaulting to {}")
        data = {}
    return data

def write_json_data(file_path: str, data):
    """
    This function will write the json data to the given file path.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
