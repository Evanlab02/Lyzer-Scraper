"""
This file contains the class to test the pit stop controller file.
"""

import unittest

from api.pit_stop_controller import (
    read_pitstops_file,
    get_all_pitstops,
    get_key_value,
    get_pitstops_for_year
)
from source.installer import uninstall_lyzer_data_files, install_lyzer_data_files
from source.file_parser import write_json_file

class TestPitStopController(unittest.TestCase):
    """
    This class will test the functions in the pit stop controller file.
    """
    def test_read_pitstops_missing_file(self):
        """
        This method will test the read pit stops file method when there is no file.
        """
        uninstall_lyzer_data_files()
        response = read_pitstops_file()
        self.assertEqual(response.result, "failure")
        self.assertEqual(response.status, 500)
        self.assertEqual(response.message, "Internal server error: pit stops file not found.")
        install_lyzer_data_files()

    def test_read_pitstops_file(self):
        """
        This method will test the read pit stops file method when there is a file.
        """
        install_lyzer_data_files()
        write_json_file("data/pit_stop_data.json", {"test": "test"})
        response = read_pitstops_file()
        self.assertEqual(response, {"test": "test"})

    def test_get_all_pitstops_missing_file(self):
        """
        This method will test the get all pit stops method when there is no file.
        """
        uninstall_lyzer_data_files()
        response = get_all_pitstops()[0]
        self.assertEqual(response["result"], "failure")
        self.assertEqual(response["status"], 500)
        self.assertEqual(response["message"], "Internal server error: pit stops file not found.")
        install_lyzer_data_files()

    def test_get_all_pitstops_file(self):
        """
        This method will test the get all pit stops method when there is a file.
        """
        install_lyzer_data_files()
        write_json_file("data/pit_stop_data.json", {"test": "test"})
        response = get_all_pitstops()[0]
        self.assertEqual(response["result"], "success")
        self.assertEqual(response["status"], 200)
        self.assertEqual(response["message"], "Pit stop data retrieved successfully.")
        self.assertEqual(response["data"], {"test": "test"})

    def test_get_key_value_invalid_key(self):
        """
        This method will test the get key value method when the key is not found.
        """
        response = get_key_value({"test": "test"}, "2021")
        self.assertEqual(response.result, "failure")
        self.assertEqual(response.status, 404)
        self.assertEqual(response.message, "Pit stop data not found for 2021.")

    def test_get_key_value_valid_key(self):
        """
        This method will test the get key value method when the key is found.
        """
        response = get_key_value({"test": {"testing": "testing"}}, "test")
        self.assertEqual(response.result, "success")
        self.assertEqual(response.status, 200)
        self.assertEqual(response.message, "Pit stop data retrieved successfully.")
        self.assertEqual(response.data, {"testing": "testing"})

    def test_get_pitstops_for_year_missing_file(self):
        """
        This method will test the get pit stops for year method when there is no file.
        """
        uninstall_lyzer_data_files()
        response, status = get_pitstops_for_year("2021")
        install_lyzer_data_files()
        self.assertEqual(response["result"], "failure")
        self.assertEqual(response["status"], 500)
        self.assertEqual(response["message"], "Internal server error: pit stops file not found.")
        self.assertEqual(status, 500)

    def test_get_pitstops_for_year_invalid_year(self):
        """
        This method will test the get pit stops for year method when the year is invalid.
        """
        install_lyzer_data_files()
        write_json_file("data/pit_stop_data.json", {"test": "test"})
        response, status = get_pitstops_for_year("2021")
        self.assertEqual(response["result"], "failure")
        self.assertEqual(response["status"], 404)
        self.assertEqual(response["message"], "Pit stop data not found for 2021.")
        self.assertEqual(status, 404)

    def test_get_pitstops_for_year_valid(self):
        """
        This method will test the get pit stops for year method when the year is valid.
        """
        install_lyzer_data_files()
        write_json_file("data/pit_stop_data.json", {"2021": {"test": "test"}})
        response, status = get_pitstops_for_year("2021")
        print(response)
        self.assertEqual(response["result"], "success")
        self.assertEqual(response["status"], 200)
        self.assertEqual(response["message"], "Pit stop data retrieved successfully.")
        self.assertEqual(response["data"], {"test": "test"})
        self.assertEqual(status, 200)
