"""
This will test the file parser module.
"""

from io import StringIO
import unittest
from unittest.mock import patch

from src.file_parser import load_json_data, write_json_data

class TestFileParser(unittest.TestCase):
    """
    This will test the file parser module.
    """
    @patch("sys.stdout", StringIO())
    def test_load_json_data(self):
        """
        This will test the load_json_data function.
        """
        json_data = load_json_data("testing/resources/basic.json")
        self.assertEqual(json_data, {"Basic": "Test","test": "basic"})
        self.assertEqual(load_json_data("testing/resources/empty.json"), {})
        self.assertEqual(load_json_data("testing/resources/invalid.json"), {})

    @patch("sys.stdout", StringIO())
    def test_write_json_data(self):
        """
        This will test the write_json_data function.
        """
        json_data = {"Basic": "Test","test": "basic"}
        write_json_data("testing/resources/writer.json", json_data)
        self.assertEqual(load_json_data("testing/resources/writer.json"), json_data)
        json_data = {"Basic": "Testing"}
        write_json_data("testing/resources/writer.json", json_data)
        self.assertEqual(load_json_data("testing/resources/writer.json"), json_data)
        