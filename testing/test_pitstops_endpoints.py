"""
This file contains the class to test all the pit stop endpoints.
"""

from source.installer import install_lyzer_data_files, uninstall_lyzer_data_files
from source.file_parser import write_json_file
from testing.helper import (
    generate_500_response_missing_file,
    generate_404_response_missing_year,
    generate_404_response_missing_location,
    generate_200_response
)
from testing.test_version_queue_endpoints import TestApiEndpointsV1

class TestPitstopsEndpoints(TestApiEndpointsV1):
    """
    This class contains all the tests for the pit stop endpoints.
    """

    def test_get_pitstops_endpoint_missing_file(self):
        """
        This method will test the get pit stops endpoint when the file is missing.
        """
        expected = generate_500_response_missing_file()
        client = self.app.test_client()
        uninstall_lyzer_data_files()
        response = client.get("/results/pitstops")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_pitstops_endpoint(self):
        """
        This method will test the pit stops endpoint when the file is present.
        """
        write_json_file("data/pit_stop_data.json", {"Testing": "Testing"})
        expected = generate_200_response({"Testing": "Testing"})
        client = self.app.test_client()
        response = client.get("/results/pitstops")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_pitstops_year_endpoint_invalid_year(self):
        """
        This method will test the pit stops endpoint when the year is invalid.
        """
        write_json_file("data/pit_stop_data.json", {"2022": {"Testing":"Testing"}})
        expected = generate_404_response_missing_year("1949")
        client = self.app.test_client()
        response = client.get("/results/pitstops/1949")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, expected)

    def test_get_pitstops_year_endpoint_valid(self):
        """
        This method will test the pit stops endpoint when the year is valid.
        """
        write_json_file("data/pit_stop_data.json", {"2022": {"Testing":"Testing"}})
        expected = generate_200_response({"Testing":"Testing"})
        client = self.app.test_client()
        response = client.get("/results/pitstops/2022")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_pitstops_year_and_location_invalid_location(self):
        """
        This method will test the pit stops endpoint when the location is invalid.
        """
        write_json_file("data/pit_stop_data.json", {"2022": {"Testing":"Testing"}})
        expected = generate_404_response_missing_location("Bahrain")
        response = self.client.get("/results/pitstops/2022/Bahrain")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, expected)

    def test_get_pitstops_year_and_location_valid(self):
        """
        This method will test the pit stops endpoint when the location is valid.
        """
        write_json_file("data/pit_stop_data.json", {"2022": {"Testing":{"Testing":"Testing"}}})
        expected = generate_200_response({"Testing":"Testing"})
        response = self.client.get("/results/pitstops/2022/Testing")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)
