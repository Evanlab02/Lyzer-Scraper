"""
This file contains the unit tests for the ScraperResponse class.
"""

import unittest

from api.scraper_response import ScraperResponse

class TestScraperResponse(unittest.TestCase):
    """
    This class contains the unit tests for the ScraperResponse class.
    """

    def test_scraper_response_no_data(self):
        """
        This method tests the ScraperResponse class with no data key.
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
        This method tests the ScraperResponse class with a data key.
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
