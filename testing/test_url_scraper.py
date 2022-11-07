"""
This module will contain the tests for the url scraper class.
"""

from io import StringIO

import unittest
from unittest.mock import patch

from scraper.url_scraper import UrlScraper

class TestUrlScraper(unittest.TestCase):
    """
    This class will contain the tests for the url scraper class.
    """

    @patch("sys.stdout", StringIO())
    def test_start(self):
        """
        This will test the start method.
        """
        url = "https://www.formula1.com/en/results.html/2022/races.html"
        url_scraper = UrlScraper(url)
        elements = url_scraper.start()
        self.assertEqual(elements, ["2022", "races.html"])

    @patch("sys.stdout", StringIO())
    def test_get_year_from_url(self):
        """
        This will test the get_year_from_url method.
        """
        url = "https://www.formula1.com/en/results.html/2022/races.html"
        url_scraper = UrlScraper(url)
        url_scraper.start()
        year = url_scraper.get_year_from_url()
        self.assertEqual(year, 2022)

    @patch("sys.stdout", StringIO())
    def test_get_invalid_year_from_url(self):
        """
        This will test the get_year_from_url method.
        """
        url = "https://www.formula1.com/en/results.html/abcd/races.html"
        url_scraper = UrlScraper(url)
        url_scraper.start()
        with self.assertRaises(SystemExit):
            url_scraper.get_year_from_url()

    @patch("sys.stdout", StringIO())
    def test_generate_url_data(self):
        """
        This will test the generate_url_data method.
        """
        url = "https://www.formula1.com/en/results.html/2022/races.html"
        url_scraper = UrlScraper(url)
        url_elements = url_scraper.start()
        url_year = url_scraper.get_year_from_url()
        url_data = url_scraper.generate_url_data(url_elements, url_year)
        self.assertEqual(url_data, ("races", 2022, "All"))

    @patch("sys.stdout", StringIO())
    def test_generate_url_data_individual_race_result(self):
        """
        This will test the generate_url_data method.
        """
        url = "https://www.formula1.com/en/results.html/2022/races/1124/bahrain/race-result.html"
        url_scraper = UrlScraper(url)
        url_elements = url_scraper.start()
        url_year = url_scraper.get_year_from_url()
        url_data = url_scraper.generate_url_data(url_elements, url_year)
        self.assertEqual(url_data, ("races", 2022, "Bahrain"))
