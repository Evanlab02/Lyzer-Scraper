"""
TODO: Add docstring
"""

import unittest

from api.scraper_response import ScraperResponse

class TestScraperResponse(unittest.TestCase):
    """
    TODO: Add docstring
    """

    def test_scraper_response_no_data(self):
        """
        TODO: Add Docstring
        """
        response = ScraperResponse("success", 200, "OK")
        self.assertEqual(
            response.convert_to_json(),
            {
                "result": "success",
                "status": 200,
                "message": "OK"
            }
        )

    def test_scraper_response_with_data(self):
        """
        TODO: Add Docstring
        """
        response = ScraperResponse("success", 200, "OK", {"test": "test"})
        self.assertEqual(
            response.convert_to_json(),
            {
                "result": "success",
                "status": 200,
                "message": "OK",
                "data": {"test": "test"}
            }
        )
