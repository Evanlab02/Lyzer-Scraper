"""
This module will test the cli parser class.
"""

from io import StringIO

import unittest
from unittest.mock import patch

from src.cli_parser import get_link, remove_first_item, find_link_in_args

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

    @patch("sys.stdout", StringIO())
    def test_get_link_no_args(self):
        """
        This will test the get_link method.
        """
        self.assertEqual(get_link([]), "Unexpected Error 2")

    @patch("sys.stdout", StringIO())
    def test_get_link_invalid_link(self):
        """
        This will test the get_link method.
        """
        self.assertEqual(get_link(["lyzer_scraper.py", "-l"]), "No Link Passed")

    @patch("sys.stdout", StringIO())
    def test_remove_first_item(self):
        """
        This will test the remove_first_item method.
        """
        args = ["lyzer_scraper.py", "-l", "https://www.dndbeyond.com/monsters"]
        self.assertEqual(remove_first_item(args), 0)
        self.assertEqual(args, ["-l", "https://www.dndbeyond.com/monsters"])

    @patch("sys.stdout", StringIO())
    def test_remove_first_item_no_args(self):
        """
        This will test the remove_first_item method.
        """
        args = []
        self.assertEqual(remove_first_item(args), 2)
        self.assertEqual(args, [])

    @patch("sys.stdout", StringIO())
    def test_find_link_in_args(self):
        """
        This will test the find_link_in_args method.
        """
        args = ["lyzer_scraper.py", "-l", "https://www.dndbeyond.com/monsters"]
        self.assertEqual(find_link_in_args(args), "https://www.dndbeyond.com/monsters")

    @patch("sys.stdout", StringIO())
    def test_find_link_in_args_no_args(self):
        """
        This will test the find_link_in_args method.
        """
        args = ["-l"]
        self.assertEqual(find_link_in_args(args), "No Link Passed")
