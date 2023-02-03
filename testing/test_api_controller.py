"""
This module contains the tests for the api_controller module.
"""

import unittest

from api.api_controller import get_data, get_file_name
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

    def test_get_file_name_with_invalid_file(self):
        """
        This function will test the get_file_name function with a invalid file.
        """
        expected = ""
        actual = get_file_name("invalid")
        self.assertEqual(actual, expected)

    def test_get_file_name_seasons(self):
        """
        This function will test the get_file_name function with the seasons file.
        """
        expected = "season_summaries.json"
        actual = get_file_name("seasons")
        self.assertEqual(actual, expected)

    def test_get_file_name_races(self):
        """
        This function will test the get_file_name function with the race file.
        """
        expected = "races.json"
        actual = get_file_name("races")
        self.assertEqual(actual, expected)

    def test_get_file_name_pits(self):
        """
        This function will test the get_file_name function with the pit file.
        """
        expected = "pit_stop_data.json"
        actual = get_file_name("pitstops")
        self.assertEqual(actual, expected)

    def test_get_file_name_fastest_laps(self):
        """
        This function will test the get_file_name function with the fastest lap file.
        """
        expected = "fastest_laps.json"
        actual = get_file_name("fastest_laps")
        self.assertEqual(actual, expected)

    def test_get_file_name_starting_grids(self):
        """
        This function will test the get_file_name function with the starting grid file.
        """
        expected = "starting_grids.json"
        actual = get_file_name("starting_grids")
        self.assertEqual(actual, expected)

    def test_get_file_name_qualifying(self):
        """
        This function will test the get_file_name function with the qualifying file.
        """
        expected = "qualifying.json"
        actual = get_file_name("qualifying")
        self.assertEqual(actual, expected)
