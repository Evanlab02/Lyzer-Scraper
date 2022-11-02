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
        self.assertFalse(self.scraper.installer.install_data_directory(".lyzer/"))
