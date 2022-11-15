"""
This will test the data compiler module.
"""

from io import StringIO
import unittest
from unittest.mock import patch

from src.data_compiler import compile_data, edit_data_with_year, edit_data_with_location

class TestDataCompiler(unittest.TestCase):
    """
    This class will test the data compiler module.
    """

    @patch("sys.stdout", StringIO())
    def test_edit_data_with_year(self):
        """
        This will test the edit_data_with_year function.
        """
        data = {"2019": {}}
        self.assertEqual(edit_data_with_year(data, 2019), data)
        self.assertEqual(edit_data_with_year(data, 2020), {"2019": {}, "2020": {}})

    @patch("sys.stdout", StringIO())
    def test_edit_data_with_location(self):
        """
        This will test the edit_data_with_location function.
        """
        data = {"2019": {}}
        data, location = edit_data_with_location(data, 2019, "Location")
        self.assertEqual(data, {"2019": {"Location": {}}})
        self.assertEqual(location, "Location")

    @patch("sys.stdin", StringIO("\n"))
    @patch("sys.stdout", StringIO())
    def test_edit_data_with_location_duplicate(self):
        """
        This will test the edit_data_with_location function with a duplicate location.
        """
        data = {"2019": {"Location": {}}}
        data, location = edit_data_with_location(data, 2019, "Location")
        self.assertEqual(data, {"2019": {"Location": {}, "LocationI": {}}})
        self.assertEqual(location, "LocationI")

    @patch("sys.stdin", StringIO("exit\n"))
    @patch("sys.stdout", StringIO())
    def test_edit_data_with_location_duplicate_exit(self):
        """
        This will test the edit_data_with_location function with a duplicate location and exit.
        """
        with self.assertRaises(SystemExit):
            data = {"2019": {"Location": {}}}
            edit_data_with_location(data, 2019, "Location")

    @patch("sys.stdout", StringIO())
    def test_compile_data(self):
        """
        This will test the compile_data function.
        """
        url_data = ("races", 2019, "Location")
        headers = ["Header"]
        data_rows = [["Data"]]
        json_data = {}
        self.assertEqual(compile_data(url_data, headers, data_rows, json_data),
        {"2019": {"Location": {"Headers": ["Header"], "Data": [["Data"]]}}})
