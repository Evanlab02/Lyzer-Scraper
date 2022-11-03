"""
This module will be used to test the file parser.
"""

from io import StringIO

import unittest
from unittest.mock import patch

from scraper.file_parser import load_json_data, write_json_data

class TestFilePaser(unittest.TestCase):
    """
    This class will test the file parser.
    """

    @patch("sys.stdout", StringIO())
    def test_load_json_data(self):
        """
        This will test the load_json_data method.
        """
        self.assertEqual({}, load_json_data("testing/resources/empty.json"))
        self.assertEqual({
            "Basic": "Test",
            "test": "basic"
        }, load_json_data("testing/resources/basic.json"))

    @patch("sys.stdout", StringIO())
    def test_write_json_data(self):
        """
        This will test the write_json_data method.
        """
        self.assertEqual({"Basic": "Testing"}, load_json_data("testing/resources/writer.json"))
        write_json_data("testing/resources/writer.json", {"Basic": "Testing", "unittest": "acceptancetest"})
        self.assertEqual({"Basic": "Testing", "unittest": "acceptancetest"}, load_json_data("testing/resources/writer.json"))
        write_json_data("testing/resources/writer.json", {"Basic": "Testing"})
