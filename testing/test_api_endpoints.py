"""
This module will contain the logic to test the api factory module.
"""
import unittest

from api.api_factory import assign_endpoints, get_version
from source.installer import install_lyzer_data_files, uninstall_lyzer_data_files
from source.file_parser import read_json_file, write_json_file
from web.flask_web_app import create_app

class TestApiEndpointsV1(unittest.TestCase):
    """Test the api factory module."""
    def __init__(self, methodName: str = ...) -> None:
        uninstall_lyzer_data_files()
        install_lyzer_data_files()
        self.app = create_app()
        assign_endpoints(self.app)
        self.app.config['TESTING'] = True
        super().__init__(methodName)

    def test_version_endpoint(self):
        """Test the assign endpoints function."""
        client = self.app.test_client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
        "status": 200,
        "result": "success",
        "message": "Version for Lyzer Scraper",
        "version": "0.6.1-beta"
        })

    def test_queue_endpoint(self):
        """Test the queue endpoint get method."""
        client = self.app.test_client()
        client.post("/queue", json=[
            "https://www.youtube.com/watch?v=QH2-TGUlwu4",
            "https://www.youtube.com/watch?v=QH2-TGUlwu4",
            "https://www.youtube.com/watch?v=QH2-TGUlwu4"
            ]
        )
        response = client.get("/queue")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [
            [
            "https://www.youtube.com/watch?v=QH2-TGUlwu4",
            "https://www.youtube.com/watch?v=QH2-TGUlwu4",
            "https://www.youtube.com/watch?v=QH2-TGUlwu4"
            ]
        ])

    def test_get_version(self):
        """Test the get version function."""
        self.assertEqual(get_version(), ({
        "status": 200,
        "result": "success",
        "message": "Version for Lyzer Scraper",
        "version": "0.6.1-beta"
        }, 200))

    def test_get_seasons_endpoint(self):
        """Test the get seasons endpoint."""
        expected = read_json_file("data/season_summaries.json")
        client = self.app.test_client()
        response = client.get("/seasons")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_seasons_endpoint_invalid_year(self):
        """Test the get seasons endpoint."""
        expected = {"message": "The season you requested was not found."}
        client = self.app.test_client()
        response = client.get("/season/2023")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_seasons_endpoint_valid_year(self):
        """Test the get seasons endpoint."""
        write_json_file("data/season_summaries.json", {"2022": "test"})
        expected = "test"
        app = create_app()
        assign_endpoints(app)
        app.config['TESTING'] = True
        client = app.test_client()
        season_year = "2022"
        response = client.get(f"/season/{season_year}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, expected)

    def test_get_races_endpoint(self):
        """Test the get races endpoint."""
        expected = read_json_file("data/races.json")
        client = self.app.test_client()
        response = client.get("/races")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_races_missing_file_endpoint(self):
        """Test the get races year endpoint."""
        uninstall_lyzer_data_files()
        expected = {
            "result": "failure",
            "message": "Internal server error: race file not found."
        }
        client = self.app.test_client()
        response = client.get("/races")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_races_year_missing_file_endpoint(self):
        """Test the get races year endpoint."""
        uninstall_lyzer_data_files()
        expected = {
            "result": "failure",
            "message": "Internal server error: race file not found."
        }
        client = self.app.test_client()
        response = client.get("/races/2022")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_races_invalid_year(self):
        """"Test the get races year endpoint"""
        expected = {
            "result": "failure",
            "message": "Internal server error: year 1949 not found."
        }

        client = self.app.test_client()
        response = client.get("/races/1949")
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_races_valid_year(self):
        """Test the get races year endpoint"""
        write_json_file("data/races.json", {"2022": {
            "headers": [
                "Round", "Name", "Date", "Circuit", "Location", "Country",
                "Laps", "Distance", "Pole Position", "Fastest Lap"
            ]
        }})

        expected = {
            "headers": [
                "Round", "Name", "Date", "Circuit", "Location", "Country",
                "Laps", "Distance", "Pole Position", "Fastest Lap"
            ]
        }

        client = self.app.test_client()
        response = client.get("/races/2022")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_races_year_and_location_missing_file(self):
        """Test the get races year and location endpoint."""
        uninstall_lyzer_data_files()
        expected = {
            "result": "failure",
            "message": "Internal server error: race file not found."
        }

        client = self.app.test_client()
        response = client.get("/race/2022/australia")
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
        expected = {
            "result": "failure",
            "message": "Internal server error: year 1949 not found."
        }

        client = self.app.test_client()
        response = client.get("/race/1949/bahrain")
        self.assertEqual(response.status_code, 500)
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
        expected = {
            "result": "failure",
            "message": "Internal server error: location australia not found."
        }

        client = self.app.test_client()
        response = client.get("/race/2022/australia")
        self.assertEqual(response.status_code, 500)
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
            "headers": [
                "Round", "Name", "Date", "Circuit", "Location", "Country",
                "Laps", "Distance", "Pole Position", "Fastest Lap"
            ]
        }

        client = self.app.test_client()
        response = client.get("/race/2022/bahrain")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_fastest_laps_endpoint_missing_file(self):
        """Test the get fastest laps endpoint."""
        uninstall_lyzer_data_files()
        expected = {
            "result": "failure",
            "message": "Internal server error: fastest laps file not found."
        }
        client = self.app.test_client()
        response = client.get("/races/fastest_laps")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_fastest_laps_endpoint(self):
        """Test the get fastest laps endpoint."""
        write_json_file("data/fastest_laps.json", {"Testing": "Testing"})
        expected = read_json_file("data/fastest_laps.json")
        client = self.app.test_client()
        response = client.get("/races/fastest_laps")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_fastest_laps_endpoint_year_missing_file(self):
        """Test the get fastest laps endpoint."""
        uninstall_lyzer_data_files()
        expected = {
            "status": 500,
            "result": "failure",
            "message": "Internal server error: fastest laps file not found."
        }
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
            "Testing": "Testing",
            "message": "Fastest laps data for year: 2021",
            "result": "success",
            "status": 200
            }
        client = self.app.test_client()
        response = client.get("/races/fastest_laps/2021")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)
