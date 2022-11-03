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
        data = {}
    return data
