"""
This module will contain the functions that will log to the logs file.
"""

from datetime import datetime

def create_log(message: str, file_path: str="logs/logs.txt") -> str:
    """Log a message to the logs file.

    Args:
        message (str): The message to log.

    Returns:
        str: The message that was logged.
    """
    message = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}"
    with open(file_path, "a") as file:
        file.write(f"{message}\n")
    return message
