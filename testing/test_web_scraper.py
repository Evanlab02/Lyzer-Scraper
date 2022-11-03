"""
This will test the web scraper class.
"""

from io import StringIO

import unittest
from unittest.mock import patch

from scraper.web_scraper import WebScraper

class TestWebScraper(unittest.TestCase):
    """
    This class contains the tests to test the Web Scraper.
    """

    def setUp(self):
        """
        This will run before each test.
        """
        self.scraper = WebScraper()

    @patch("sys.stdout", StringIO())
    def test_start(self):
        """
        This will test the start method.
        """
        self.assertEqual(0, self.scraper.start())

    @patch("sys.stdout", StringIO())
    def test_scrape_site_exit(self):
        """
        This will test the scrape_site method.
        """
        data = ("abcd")
        with self.assertRaises(SystemExit):
            self.scraper.scrape_site(data)
