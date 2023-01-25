"""
This module will contain the logic to test the api fastest laps endpoints.
"""

from source.installer import install_lyzer_data_files, uninstall_lyzer_data_files
from source.file_parser import write_json_file
from testing.test_version_queue_endpoints import TestApiEndpointsV1

class TestFastestLapsEndpoints(TestApiEndpointsV1):
    """Test the fastest laps endpoints."""

    def test_get_fastest_laps_endpoint_missing_file(self):
        """Test the get fastest laps endpoint."""
        expected = {
            "status": 500,
            "result": "failure",
            "message": "Internal server error: fastest laps file not found."
        }
        uninstall_lyzer_data_files()
        client = self.app.test_client()
        response = client.get("/races/fastest_laps")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_fastest_laps_endpoint(self):
        """Test the get fastest laps endpoint."""
        write_json_file("data/fastest_laps.json", {"Testing": "Testing"})
        expected = {
            "status": 200,
            "result": "success",
            "message": "Fastest laps - All",
            "data": {"Testing": "Testing"}
        }
        client = self.app.test_client()
        response = client.get("/races/fastest_laps")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_fastest_laps_endpoint_year_missing_file(self):
        """Test the get fastest laps endpoint."""
        expected = {
            "result": "failure",
            "message": "Internal server error: fastest laps file not found.",
            "status": 500
        }
        uninstall_lyzer_data_files()
        client = self.app.test_client()
        response = client.get("/races/fastest_laps/2021")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_fastest_laps_endpoint_year_invalid_year(self):
        """Test the get fastest laps endpoint."""
        write_json_file("data/fastest_laps.json", {"2022": {"Testing": "Testing"}})
        expected = {
            "status": 404,
            "result": "failure",
            "message": "Data not found for year: 2021"
        }
        client = self.app.test_client()
        response = client.get("/races/fastest_laps/2021")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, expected)

    def test_get_fatest_laps_endpoint_year_2021(self):
        """Test the get fastest laps endpoint."""
        write_json_file("data/fastest_laps.json", {"2021": {"Testing": "Testing"}})
        expected = {
            "data": {"Testing": "Testing"},
            "message": "Fastest laps data for year: 2021",
            "result": "success",
            "status": 200
            }
        client = self.app.test_client()
        response = client.get("/races/fastest_laps/2021")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)
