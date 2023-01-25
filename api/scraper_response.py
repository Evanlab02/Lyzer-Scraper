"""
TODO: Add file docstring.
"""

from dataclasses import dataclass

@dataclass
class ScraperResponse:
    """
    TODO: Add class docstring.
    """
    result: str
    status: int
    message: str
    data: dict = None

    def convert_to_json(self):
        """
        TODO: Add method docstring.
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
