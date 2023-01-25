"""
This file contains the ScraperResponse class.
"""

from dataclasses import dataclass

@dataclass
class ScraperResponse:
    """
    This class will be used to generate responses from the API.

    Attributes:
        result (str): The result of the API call.
        status (int): The status code of the API call.
        message (str): The message of the API call.
        data (dict): The data of the API call.

    Methods:
        convert_to_json: Converts the ScraperResponse object to a JSON object.
    """
    result: str
    status: int
    message: str
    data: dict = None

    def convert_to_json(self):
        """
        This method will be used to convert the ScraperResponse object to a JSON object.

        Returns:
            dict: The ScraperResponse object converted to a JSON object.
        """
        response = {
            "result": self.result,
            "status": self.status,
            "message": self.message,
            "data": self.data
        }
        if self.data is None:
            del response["data"]
        return response
