"""
This module contains the tests for the api_controller module.
"""

import unittest

from api.api_controller import get_data
from source.file_parser import write_json_file
from source.installer import uninstall_lyzer_data_files, install_lyzer_data_files
from testing.helper import (
    generate_500_response_missing_file,
    generate_404_response_missing_year,
    generate_404_response_missing_location,
    generate_200_response
)

class TestApiController(unittest.TestCase):
    """
    This class will contain the tests for the api_controller module.
    """
    def test_get_data_with_no_file(self):
        """
        This function will test the get_data function with a invalid file.
        """
        uninstall_lyzer_data_files()
        expected = generate_500_response_missing_file()
        actual = get_data("data/invalid.json")
        self.assertEqual(actual.convert_to_json(), expected)

    def test_get_data_with_file(self):
        """
        This function will test the get_data function with a valid file.
        """
        install_lyzer_data_files()
        write_json_file("data/races.json", {"2020": {"A": {"B": "C"}}})
        expected = generate_200_response({"2020": {"A": {"B": "C"}}})
        actual = get_data("data/races.json")
        self.assertEqual(actual.convert_to_json(), expected)

    def test_get_data_with_file_and_year(self):
        """
        This function will test the get_data function with a valid file and year.
        """
        install_lyzer_data_files()
        write_json_file("data/races.json", {"2020": {"A": {"B": "C"}}})
        expected = generate_200_response({"A": {"B": "C"}})
        actual = get_data("data/races.json", "2020")
        self.assertEqual(actual.convert_to_json(), expected)

    def test_get_data_with_year_and_location(self):
        """
        This function will test the get_data function with a valid file, year, and location.
        """
        install_lyzer_data_files()
        write_json_file("data/races.json", {"2020": {"A": {"B": "C"}}})
        expected = generate_200_response({"B": "C"})
        actual = get_data("data/races.json", "2020", "A")
        self.assertEqual(actual.convert_to_json(), expected)

    def test_get_data_invalid_year(self):
        """
        This function will test the get_data function with a invalid year.
        """
        install_lyzer_data_files()
        write_json_file("data/races.json", {"2020": {"A": {"B": "C"}}})
        expected = generate_404_response_missing_year("2021")
        actual = get_data("data/races.json", "2021")
        self.assertEqual(actual.convert_to_json(), expected)

    def test_get_data_invalid_location(self):
        """
        This function will test the get_data function with a invalid location.
        """
        install_lyzer_data_files()
        write_json_file("data/races.json", {"2020": {"A": {"B": "C"}}})
        expected = generate_404_response_missing_location("D")
        actual = get_data("data/races.json", "2020", "D")
        self.assertEqual(actual.convert_to_json(), expected)
