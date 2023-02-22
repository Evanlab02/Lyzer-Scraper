"""
This module will contain the logic to test the api seasons endpoints.
"""

from source.installer import install_lyzer_data_files, uninstall_lyzer_data_files
from source.file_parser import write_json_file
from testing.helper import (
    generate_500_response_missing_file,
    generate_404_response_missing_year,
    generate_200_response
)
from testing.test_version_queue_endpoints import TestApiEndpointsV1

class TestSeasonsEndpointsV1(TestApiEndpointsV1):
    """Test the seasons endpoints."""
    def test_get_seasons_endpoint_missing_file(self):
        """Test the get seasons endpoint."""
        uninstall_lyzer_data_files()
        expected = generate_500_response_missing_file()
        client = self.app.test_client()
        response = client.get("/data/seasons")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_seasons_endpoint(self):
        """Test the get seasons endpoint."""
        write_json_file("data/season_summaries.json", {"2022": {"url": "test"}})
        expected = {
            "status": 200,
            "result": "success",
            "message": "Data retrieved successfully.",
            "data": {"2022": {"url": "test"}}
        }
        client = self.app.test_client()
        response = client.get("/data/seasons")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_seasons_endpoint_year_missing_file(self):
        """Test the get seasons year endpoint."""
        uninstall_lyzer_data_files()
        expected = generate_500_response_missing_file()
        client = self.app.test_client()
        response = client.get("/data/seasons/2022")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_seasons_endpoint_invalid_year(self):
        """Test the get seasons endpoint."""
        write_json_file("data/season_summaries.json", {"2022": {"url": "test"}})
        expected = generate_404_response_missing_year("2023")
        client = self.app.test_client()
        response = client.get("/data/seasons/2023")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, expected)

    def test_get_seasons_endpoint_valid_year(self):
        """Test the get seasons endpoint."""
        write_json_file("data/season_summaries.json", {"2022": {"url": "test"}})
        expected = generate_200_response({"url": "test"})
        season_year = "2022"
        client = self.app.test_client()
        response = client.get(f"/data/seasons/{season_year}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)
