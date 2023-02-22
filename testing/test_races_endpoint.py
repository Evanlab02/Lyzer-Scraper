"""
This module will contain the logic to test the api races endpoints.
"""

from source.installer import install_lyzer_data_files, uninstall_lyzer_data_files
from source.file_parser import write_json_file, read_json_file
from testing.helper import (
    generate_500_response_missing_file,
    generate_404_response_missing_year,
    generate_404_response_missing_location,
    generate_200_response
)
from testing.test_version_queue_endpoints import TestApiEndpointsV1

class TestRacesEndpoints(TestApiEndpointsV1):
    """This class contains all the tests for the races endpoints."""
    def test_get_races_endpoint(self):
        """Test the get races endpoint."""
        expected_data = read_json_file("data/races.json")
        expected_response = generate_200_response(expected_data)
        client = self.app.test_client()
        response = client.get("/scraper/races")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_response)

    def test_get_races_missing_file_endpoint(self):
        """Test the get races year endpoint."""
        uninstall_lyzer_data_files()
        expected = generate_500_response_missing_file()
        client = self.app.test_client()
        response = client.get("/scraper/races")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_races_year_missing_file_endpoint(self):
        """Test the get races year endpoint."""
        expected = generate_500_response_missing_file()
        uninstall_lyzer_data_files()
        client = self.app.test_client()
        response = client.get("/scraper/races/2022")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_races_invalid_year(self):
        """"Test the get races year endpoint"""
        expected = generate_404_response_missing_year("1949")
        client = self.app.test_client()
        response = client.get("/scraper/races/1949")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, expected)

    def test_get_races_valid_year(self):
        """Test the get races year endpoint"""
        write_json_file("data/races.json", {"2022": {
            "headers": [
                "Round", "Name", "Date", "Circuit", "Location", "Country",
                "Laps", "Distance", "Pole Position", "Fastest Lap"
            ]
        }})

        client = self.app.test_client()

        expected = {
            "status": 200,
            "result": "success",
            "message": "Data retrieved successfully.",
            "data": {
                "headers": [
                    "Round", "Name", "Date", "Circuit", "Location", "Country",
                    "Laps", "Distance", "Pole Position", "Fastest Lap"
                ]
            }
        }

        response = client.get("/scraper/races/2022")
        self.assertEqual(response.json, expected)
        self.assertEqual(response.status_code, 200)

    def test_get_races_year_and_location_missing_file(self):
        """Test the get races year and location endpoint."""
        uninstall_lyzer_data_files()
        expected = generate_500_response_missing_file()
        client = self.app.test_client()
        response = client.get("/scraper/races/2022/australia")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_races_year_and_location_invalid_year(self):
        """Test the get races year and location endpoint."""
        write_json_file("data/races.json", {"2022": {
            "bahrain": {
                "headers": [
                    "Round", "Name", "Date", "Circuit", "Location", "Country",
                    "Laps", "Distance", "Pole Position", "Fastest Lap"
                ]
            }
        }})
        expected = generate_404_response_missing_year("1949")

        client = self.app.test_client()
        response = client.get("/scraper/races/1949/bahrain")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, expected)

    def test_get_races_year_and_location_invalid_location(self):
        """Test the get races year and location endpoint."""
        write_json_file("data/races.json", {"2022": {
            "bahrain": {
                "headers": [
                    "Round", "Name", "Date", "Circuit", "Location", "Country",
                    "Laps", "Distance", "Pole Position", "Fastest Lap"
                ]
            }
        }})
        expected = generate_404_response_missing_location("australia")

        client = self.app.test_client()
        response = client.get("/scraper/races/2022/australia")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, expected)

    def test_get_races_year_and_location_endpoint_valid(self):
        """Test the get races year and location endpoint."""
        write_json_file("data/races.json", {"2022": {
            "bahrain": {
                "headers": [
                    "Round", "Name", "Date", "Circuit", "Location", "Country",
                    "Laps", "Distance", "Pole Position", "Fastest Lap"
                ]
            }
        }})
        expected = {
            "data": {
                "headers": [
                    "Round", "Name", "Date", "Circuit", "Location", "Country",
                    "Laps", "Distance", "Pole Position", "Fastest Lap"
                ]
            },
            "result": "success",
            "status": 200,
            "message": "Data retrieved successfully."
        }

        client = self.app.test_client()
        response = client.get("/scraper/races/2022/bahrain")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)
