"""
This module will contain the tests for the data compiler module.
"""

from io import StringIO

import unittest
from unittest.mock import patch

from scraper.data_compiler import (
    edit_data_with_year,
    edit_data_with_location,
    compile_data
)

class TestDataCompiler(unittest.TestCase):
    """
    This class will test the data compiler module.
    """

    @patch("sys.stdout", StringIO())
    def test_edit_data_with_year(self):
        """
        This will test the edit_data_with_year method.
        """
        data = {}
        data = edit_data_with_year(data, 2020)
        self.assertEqual({"2020":{}}, data)

    @patch("sys.stdin", StringIO("\n"))
    @patch("sys.stdout", StringIO())
    def test_edit_data_with_year_with_existing_year(self):
        """
        This will test the edit_data_with_year method with an existing year.
        """
        data = {"2020":{}}
        data = edit_data_with_year(data, 2020)
        self.assertEqual({"2020":{}}, data)

    @patch("sys.stdout", StringIO())
    def test_edit_data_with_location(self):
        """
        This will test the edit_data_with_location method.
        """
        data = {"2020":{}}
        data = edit_data_with_location(data, 2020, "all")[0]
        self.assertEqual({"2020":{"all":{}}}, data)

    @patch("sys.stdin", StringIO("\n"))
    @patch("sys.stdout", StringIO())
    def test_edit_data_with_location_with_existing_location(self):
        """
        This will test the edit_data_with_location method with an existing location.
        """
        data = {"2020":{"all":{}}}
        data = edit_data_with_location(data, 2020, "all")[0]
        self.assertEqual({"2020":{"all":{}, "allI":{}}}, data)

    @patch("sys.stdin", StringIO("exit\n"))
    @patch("sys.stdout", StringIO())
    def test_edit_data_with_location_with_existing_location_and_input(self):
        """
        This will test the edit_data_with_location method with an existing location and input.
        """
        data = {"2020":{"all":{}}}
        with self.assertRaises(SystemExit):
            data = edit_data_with_location(data, 2020, "all")

    @patch("sys.stdout", StringIO())
    def test_compile_data(self):
        """
        This will test the compile_data method.
        """
        url_data = ["races", 2020, "All"]
        headers = ["header1", "header2"]
        data_rows = [["data1", "data2"], ["data3", "data4"]]
        json_data = {}
        json_data = compile_data(url_data, headers, data_rows, json_data)
        self.assertEqual({
            "2020":{
                "All":{
                    "Headers":["header1", "header2"],
                    "Data":[["data1", "data2"], ["data3", "data4"]]}}}, json_data)

    @patch("sys.stdin", StringIO("\n"))
    @patch("sys.stdout", StringIO())
    def test_compile_data_with_existing_data(self):
        """
        This will test the compile_data method with existing data.
        """
        url_data = ["races", 2020, "All"]
        headers = ["header1", "header2"]
        data_rows = [["data1", "data2"], ["data3", "data4"]]
        json_data = {"2020":{}}
        json_data = compile_data(url_data, headers, data_rows, json_data)
        self.assertEqual({
            "2020":{
                "All":{
                    "Headers":["header1", "header2"],
                    "Data":[["data1", "data2"], ["data3", "data4"]]}}}, json_data)

    @patch("sys.stdin", StringIO("\n"))
    @patch("sys.stdout", StringIO())
    def test_compile_data_with_existing_location(self):
        """
        This will test the compile_data method with existing data and input.
        """
        url_data = ["races", 2020, "All"]
        headers = ["header1", "header2"]
        data_rows = [["data1", "data2"], ["data3", "data4"]]
        json_data = {"2020":{"All":{}}}
        json_data = compile_data(url_data, headers, data_rows, json_data)
        self.assertEqual({
            "2020":{
                "All":{},
                "AllI":{"Headers":["header1", "header2"],
                "Data":[["data1", "data2"], ["data3", "data4"]]}}}, json_data)
