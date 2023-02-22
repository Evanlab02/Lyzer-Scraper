"""
TODO: Add File Docstring
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


class TestQualifyingEndpoints(TestApiEndpointsV1):
    """
    TODO: Add Class Docstring
    """

    def test_get_qualifying_results_missing_file(self):
        """
        This method will test the get qualifying results endpoint when the file is missing.
        """
        expected = generate_500_response_missing_file()
        uninstall_lyzer_data_files()
        response = self.client.get("/scraper/qualifying")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_qualifying_endpoint(self):
        """
        This method will test the qualifying endpoint when the file is present.
        """
        write_json_file("data/qualifying.json", {"Testing": "Testing"})
        expected = generate_200_response({"Testing": "Testing"})
        response = self.client.get("/scraper/qualifying")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_qualifying_year_endpoint_invalid_year(self):
        """
        This method will test the qualifying endpoint when the year is invalid.
        """
        write_json_file("data/qualifying.json", {"2022": {"Testing":"Testing"}})
        expected = generate_404_response_missing_year("1949")
        response = self.client.get("/scraper/qualifying/1949")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, expected)

    def test_get_qualifying_year_endpoint_valid(self):
        """
        This method will test the qualifying endpoint when the year is valid.
        """
        write_json_file("data/qualifying.json", {"2022": {"Testing":"Testing"}})
        expected = generate_200_response({"Testing":"Testing"})
        response = self.client.get("/scraper/qualifying/2022")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_qualifying_year_location_endpoint_invalid_year(self):
        """
        This method will test the qualifying endpoint when the year is invalid.
        """
        write_json_file("data/qualifying.json", {"2022": {"Testing":"Testing"}})
        expected = generate_404_response_missing_year("1949")
        response = self.client.get("/scraper/qualifying/1949/Testing")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, expected)

    def test_get_qualifying_year_location_endpoint_invalid_location(self):
        """
        This method will test the qualifying endpoint when the location is invalid.
        """
        write_json_file("data/qualifying.json", {"2022": {"Bahrain":"Testing"}})
        expected = generate_404_response_missing_location("Testing")
        response = self.client.get("/scraper/qualifying/2022/Testing")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, expected)

    def test_get_qualifying_year_location_endpoint_valid(self):
        """
        This method will test the qualifying endpoint when the location is valid.
        """
        write_json_file("data/qualifying.json", {"2022": {"Testing":{"Testing": "Testing"}}})
        expected = generate_200_response({"Testing":"Testing"})
        response = self.client.get("/scraper/qualifying/2022/Testing")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)
