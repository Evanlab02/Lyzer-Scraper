"""
This will test the web scraper class.
"""

from io import StringIO

import unittest
from unittest.mock import patch

from lyzer_scraper import start_web_scraper, scrape_link
from src.web_scraper import WebScraper

class TestLyzerScraper(unittest.TestCase):
    """
    This class contains the tests to test the Web Scraper.
    """
    @patch("sys.stdout", StringIO())
    def setUp(self):
        """
        This will setup the tests.
        """
        self.locations = [
            "bahrain",
            "portugal",
            "spain"
        ]

    @patch("sys.stdout", StringIO())
    def test_start_web_scraper(self):
        """
        This function will test the start_web_scraper function.
        """
        scraper = start_web_scraper()
        self.assertIsInstance(scraper, WebScraper)

    @patch("sys.stdout", StringIO())
    def test_scrape_link(self):
        """
        This function will test the scrape_link function.
        """

        types = [
            "race-result.html",
            "fastest-laps.html",
            "pit-stop-summary.html",
            "unknown.html"
        ]

        for year in range(1950, 2023):
            for location in self.locations:
                for page_type in types:
                    url = f"https://www.formula1.com/en/results.html/{year}"\
                        +f"/races/1124/{location}/{page_type}"
                    url_elements = scrape_link(url)
                    print(url_elements)
                    self.assertEqual(url_elements[1], year)
                    if page_type == types[0]:
                        self.assertEqual(url_elements[0], "races")
                        self.assertEqual(url_elements[2], location.capitalize())
                    elif page_type == types[1]:
                        self.assertEqual(url_elements[0], "fastest_laps")
                        self.assertEqual(url_elements[2], location.capitalize())
                    elif page_type == types[2]:
                        self.assertEqual(url_elements[0], "pit_stop_summary")
                        self.assertEqual(url_elements[2], location.capitalize())
                    else:
                        self.assertEqual(url_elements[0], "unknown")
                        self.assertEqual(url_elements[2], "unknown")
