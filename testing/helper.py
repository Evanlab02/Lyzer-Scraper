"""
This module contains helper functions for the tests.
"""

def generate_500_response_missing_file():
    """
    This function will generate a 500 response.
    """
    return {
        "status": 500,
        "result": "failure",
        "message": "Internal server error: file not found."
    }

def generate_404_response_missing_year(year: str):
    """
    This function will generate a 404 response.

    Args:
        year (str): The year that was not found.
    """
    return {
        "status": 404,
        "result": "failure",
        "message": f"Year not found {year}."
    }

def generate_404_response_missing_location(location: str):
    """
    This function will generate a 404 response.

    Args:
        location (str): The location that was not found.
    """
    return {
        "status": 404,
        "result": "failure",
        "message": f"Location not found {location}."
    }

def generate_200_response(data: dict):
    """
    This function will generate a 200 response.

    Args:
        data (dict): The data that was retrieved.
    """
    return {
        "status": 200,
        "result": "success",
        "message": "Data retrieved successfully.",
        "data": data
    }
