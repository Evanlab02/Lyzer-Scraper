"""
This file contains the tests for the practice endpoints.
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

class TestPracticeEndpoints(TestApiEndpointsV1):
    """This class contains the tests for the practice endpoints."""

    def test_get_practice_endpoint_missing_file(self):
        """This function tests the get practice endpoint when the file is missing."""
        uninstall_lyzer_data_files()
        expected = generate_500_response_missing_file()
        client = self.app.test_client()
        response = client.get("/data/firstPractice")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_practice_endpoint(self):
        """This function tests the get practice endpoint."""
        write_json_file("data/practice1.json", {"Testing": "Testing"})
        expected = generate_200_response({"Testing": "Testing"})
        client = self.app.test_client()
        response = client.get("/data/firstPractice")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_practice_endpoint_year_invalid_year(self):
        """This function tests the get practice endpoint when the year is invalid."""
        write_json_file("data/practice1.json", {"2022": {"Testing": "Testing"}})
        expected = generate_404_response_missing_year("2021")
        client = self.app.test_client()
        response = client.get("/data/firstPractice/2021")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, expected)

    def test_get_practice_endpoint_year_2022(self):
        """This function tests the get practice endpoint when the year is 2022."""
        write_json_file("data/practice1.json", {"2022": {"Testing": "Testing"}})
        expected = generate_200_response({"Testing": "Testing"})
        client = self.app.test_client()
        response = client.get("/data/firstPractice/2022")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_practice_endpoint_year_2022_location_invalid_location(self):
        """This function tests the get practice endpoint when the location is invalid."""
        write_json_file("data/practice1.json", {"2022": {"Testing": "Testing"}})
        expected = generate_404_response_missing_location("Invalid")
        client = self.app.test_client()
        response = client.get("/data/firstPractice/2022/Invalid")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, expected)

    def test_get_practice_endpoint_year_2022_location_testing(self):
        """This function tests the get practice endpoint when the location is Testing."""
        write_json_file("data/practice1.json", {"2022": {"Testing": "Testing"}})
        expected = generate_200_response("Testing")
        client = self.app.test_client()
        response = client.get("/data/firstPractice/2022/Testing")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)
