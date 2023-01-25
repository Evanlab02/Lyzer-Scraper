"""
This file contains the class to test the pit stop controller file.
"""

import unittest

from api.pit_stop_controller import read_pitstops_file, get_all_pitstops
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
        response = get_all_pitstops()
        self.assertEqual(response.result, "failure")
        self.assertEqual(response.status, 500)
        self.assertEqual(response.message, "Internal server error: pit stops file not found.")
        install_lyzer_data_files()

    def test_get_all_pitstops_file(self):
        """
        This method will test the get all pit stops method when there is a file.
        """
        install_lyzer_data_files()
        write_json_file("data/pit_stop_data.json", {"test": "test"})
        response = get_all_pitstops()
        self.assertEqual(response.result, "success")
        self.assertEqual(response.status, 200)
        self.assertEqual(response.message, "Pit stop data retrieved successfully.")
        self.assertEqual(response.data, {"test": "test"})
