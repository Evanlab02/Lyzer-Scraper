"""
This module will test the scraper class.
"""

import unittest

from unittest.mock import patch
from io import StringIO

from scraper.web_scraper import Scraper

class TestScraper(unittest.TestCase):
    """
    This class will test the scraper class.
    """

    @patch("sys.stdout", StringIO())
    def setUp(self):
        """
        This will set up the tests.
        """
        self.scraper = Scraper()

    @patch("sys.stdout", StringIO())
    def test_introduce(self):
        """
        This will test the introduce method.
        """
        self.assertEqual(0, self.scraper.start())

    @patch("sys.stdout", StringIO())
    def test_install(self):
        """
        This will test the install method.
        """
        self.assertEqual(0, self.scraper.install(".test/"))
        self.assertTrue(self.scraper.installer.remove_data_file("races.json", ".test/"))
        self.assertTrue(self.scraper.installer.remove_data_directory(".test/"))

    @patch("sys.stdout", StringIO())
    def test_process_args(self):
        """
        This will test the process_args method.
        """
        self.assertEqual("", self.scraper.process_args())
        self.scraper.args = ["", "-l", "https://www.google.com"]
        self.assertEqual("https://www.google.com", self.scraper.process_args())
        self.scraper.args = ["", "--link", "https://www.google.com"]
        self.assertEqual("https://www.google.com", self.scraper.process_args())
