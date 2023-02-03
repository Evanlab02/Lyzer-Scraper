"""
This module will contain the logic to test the api fastest laps endpoints.
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

class TestFastestLapsEndpoints(TestApiEndpointsV1):
    """Test the fastest laps endpoints."""

    def test_get_fastest_laps_endpoint_missing_file(self):
        """Test the get fastest laps endpoint."""
        expected = generate_500_response_missing_file()
        uninstall_lyzer_data_files()
        client = self.app.test_client()
        response = client.get("/data/fastest_laps")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_fastest_laps_endpoint(self):
        """Test the get fastest laps endpoint."""
        write_json_file("data/fastest_laps.json", {"Testing": "Testing"})
        expected = generate_200_response({"Testing": "Testing"})
        client = self.app.test_client()
        response = client.get("/data/fastest_laps")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_fastest_laps_endpoint_year_missing_file(self):
        """Test the get fastest laps endpoint."""
        expected = generate_500_response_missing_file()
        uninstall_lyzer_data_files()
        client = self.app.test_client()
        response = client.get("/data/fastest_laps/2021")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_fastest_laps_endpoint_year_invalid_year(self):
        """Test the get fastest laps endpoint."""
        write_json_file("data/fastest_laps.json", {"2022": {"Testing": "Testing"}})
        expected = generate_404_response_missing_year("2021")
        client = self.app.test_client()
        response = client.get("/data/fastest_laps/2021")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, expected)

    def test_get_fatest_laps_endpoint_year_2021(self):
        """Test the get fastest laps endpoint."""
        write_json_file("data/fastest_laps.json", {"2021": {"Testing": "Testing"}})
        expected = generate_200_response({"Testing": "Testing"})
        client = self.app.test_client()
        response = client.get("/data/fastest_laps/2021")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_fastest_laps_endpoint_year_location_missing_file(self):
        """Test the get fastest laps endpoint."""
        expected = generate_500_response_missing_file()
        uninstall_lyzer_data_files()
        client = self.app.test_client()
        response = client.get("/data/fastest_laps/2021/bahrain")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_fastest_laps_endpoint_year_location_invalid_year(self):
        """Test the get fastest laps endpoint."""
        write_json_file("data/fastest_laps.json", {"2022": {"bahrain": {"Testing": "Testing"}}})
        expected = generate_404_response_missing_year("2021")
        client = self.app.test_client()
        response = client.get("/data/fastest_laps/2021/bahrain")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, expected)

    def test_get_fastest_laps_endpoint_year_location_invalid_location(self):
        """Test the get fastest laps endpoint."""
        write_json_file("data/fastest_laps.json", {"2021": {"bahrain": {"Testing": "Testing"}}})
        expected = generate_404_response_missing_location("testing")
        client = self.app.test_client()
        response = client.get("/data/fastest_laps/2021/testing")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, expected)

    def test_get_fastest_laps_endpoint_year_location_2021_bahrain(self):
        """Test the get fastest laps endpoint."""
        write_json_file("data/fastest_laps.json", {"2021": {"bahrain": {"Testing": "Testing"}}})
        expected = generate_200_response({"Testing": "Testing"})
        client = self.app.test_client()
        response = client.get("/data/fastest_laps/2021/bahrain")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)
