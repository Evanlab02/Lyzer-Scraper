"""
This module will test the cli parser class.
"""

from io import StringIO

import unittest
from unittest.mock import patch

from scraper.cli_parser import get_link

class TestCliParser(unittest.TestCase):
    """
    This class will test the cli parser class.
    """

    @patch("sys.stdout", StringIO())
    def test_get_link(self):
        """
        This will test the get_link method.
        """
        self.assertEqual(get_link(
            ["lyzer_scraper.py", "-l", "https://www.dndbeyond.com/monsters"]),
            "https://www.dndbeyond.com/monsters"
        )
