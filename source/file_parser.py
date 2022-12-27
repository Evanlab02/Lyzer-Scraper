"""
This module will contain the functions that will parse the data files.
"""

import json
import os

from logs.console_logger import log_to_console

def create_data_directory(directory_path: str) -> bool:
    """
    Create a directory.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        bool: True if the directory was created, False if it wasn't.
    """
    if os.path.exists(directory_path):
        return False

    os.mkdir(directory_path)
    return True

def create_text_file(file_path: str) -> bool:
    """
    Create a text file.

    Args:
        file_path (str): The path to the file.

    Returns:
        bool: True if the file was created, False if it wasn't.
    """
    if not file_path.endswith(".txt"):
        return False

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("")
    return True

def create_json_file(file_path: str, starting_value) -> bool:
    """
    Create a json file.

    Args:
        file_path (str): The path to the file.
        starting_value (dict): The starting value of the json file.

    Returns:
        bool: True if the file was created, False if it wasn't.
    """
    if not file_path.endswith(".json"):
        return False

    if os.path.exists(file_path):
        return False

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(starting_value, file)
    return True

def read_json_file(file_path: str):
    """
    Read a json file.

    Args:
        file_path (str): The path to the file.

    Returns:
        The data from the json file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as error:
        log_to_console(f"The file {file_path} does not exist.", "ERROR")
        raise error

def write_json_file(file_path: str, data):
    """
    Write to a json file.

    Args:
        file_path (str): The path to the file.
        data (dict): The data to write to the file.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
