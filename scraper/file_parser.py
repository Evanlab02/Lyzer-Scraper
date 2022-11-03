"""
This module will contain the logic to load and write data from and to a json file.
"""

import json

def load_json_data(file_path: str) -> dict:
    """
    This function will load the json data from the given file path.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("This json file is empty.")
        print("Defaulting to {}")
        data = {}
    return data

def write_json_data(file_path: str, data: dict):
    """
    This function will write the json data to the given file path.
    """
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
