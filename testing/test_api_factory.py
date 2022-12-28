"""
This module will contain the logic to test the api factory module.
"""
import unittest

from api.api_factory import assign_endpoints, get_version
from source.installer import install_lyzer_data_files, uninstall_lyzer_data_files
from source.file_parser import read_json_file, write_json_file
from web.flask_web_app import create_app

class TestApiFactory(unittest.TestCase):
    """Test the api factory module."""
    def __init__(self, methodName: str = ...) -> None:
        uninstall_lyzer_data_files()
        install_lyzer_data_files()
        self.app = create_app()
        assign_endpoints(self.app)
        self.app.config['TESTING'] = True
        super().__init__(methodName)

    def setUp(self) -> None:
        """Set up the test client."""
        with self.app.app_context():
            with self.app.test_client() as client:
                yield client
        return super().setUp()

    def test_version_endpoint(self):
        """Test the assign endpoints function."""
        client = self.app.test_client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"version": "0.5.0"})

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

    def test_priority_queue_endpoint_race_summary(self):
        """Test the priority queue endpoint post method."""
        expected = {
            "result": "success"
        }
        client = self.app.test_client()
        response = client.post("/queue/priority", json={
            "url": "https://www.formula1.com/en/results.html/2022/races.html"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_priority_queue_endpoint_race_results(self):
        """Test the priority queue endpoint post method."""
        expected = {
            "result": "success"
        }
        client = self.app.test_client()
        response = client.post("/queue/priority", json={
            "url":
            "https://www.formula1.com/en/results.html/2022/races/1124/bahrain/race-result.html"
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_priority_queue_endpoint_qualifying_results(self):
        """Test the priority queue endpoint post method."""
        expected = {
            "result": "success"
        }
        client = self.app.test_client()
        response = client.post("/queue/priority", json={
            "url":
            "https://www.formula1.com/en/results.html/2022/races/1124/bahrain/qualifying.html"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_priority_queue_endpoint_practice1_results(self):
        """Test the priority queue endpoint post method."""
        expected = {
            "result": "success"
        }
        client = self.app.test_client()
        response = client.post("/queue/priority", json={
            "url":
            "https://www.formula1.com/en/results.html/2022/races/1124/bahrain/practice-1.html"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_priority_queue_endpoint_practice2_results(self):
        """Test the priority queue endpoint post method."""
        expected = {
            "result": "success"
        }
        client = self.app.test_client()
        response = client.post("/queue/priority", json={
            "url":
            "https://www.formula1.com/en/results.html/2022/races/1124/bahrain/practice-2.html"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_priority_queue_endpoint_practice3_results(self):
        """Test the priority queue endpoint post method."""
        expected = {
            "result": "success"
        }
        client = self.app.test_client()
        response = client.post("/queue/priority", json={
            "url":
            "https://www.formula1.com/en/results.html/2022/races/1124/bahrain/practice-3.html"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_priority_queue_endpoint_starting_grid(self):
        """Test the priority queue endpoint post method."""
        expected = {
            "result": "success"
        }
        client = self.app.test_client()
        response = client.post("/queue/priority", json={
            "url":
            "https://www.formula1.com/en/results.html/2022/races/1124/bahrain/starting-grid.html"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_priority_queue_endpoint_pitstops(self):
        """Test the priority queue endpoint post method."""
        expected = {
            "result": "success"
        }
        client = self.app.test_client()
        response = client.post("/queue/priority", json={
        "url":
        "https://www.formula1.com/en/results.html/2022/races/1124/bahrain/pit-stop-summary.html"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_priority_queue_endpoint_fastest_laps(self):
        """Test the priority queue endpoint post method."""
        expected = {
            "result": "success"
        }
        client = self.app.test_client()
        response = client.post("/queue/priority", json={
            "url":
            "https://www.formula1.com/en/results.html/2022/races/1124/bahrain/fastest-laps.html"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_priority_queue_endpoint_drivers(self):
        """Test the priority queue endpoint post method."""
        expected = {
            "result": "success"
        }
        client = self.app.test_client()
        response = client.post("/queue/priority", json={
            "url":
            "https://www.formula1.com/en/results.html/2022/drivers.html"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_priority_queue_endpoint_teams(self):
        """Test the priority queue endpoint post method."""
        expected = {
            "result": "success"
        }
        client = self.app.test_client()
        response = client.post("/queue/priority", json={
            "url":
            "https://www.formula1.com/en/results.html/2021/team/alphatauri_honda.html"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_priority_queue_endpoint_scraped_url(self):
        """Test the priority queue endpoint post method."""
        expected = {
            "result": "ignored",
            "message": "Url already scraped."
        }
        client = self.app.test_client()
        response = client.post("/queue/priority", json={
            "url":
            "https://www.formula1.com/en/results.html/2022/races.html"
        })
        response = client.post("/queue/priority", json={
            "url":
            "https://www.formula1.com/en/results.html/2022/races.html"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_priority_queue_endpoint_invalid_url(self):
        """Test the priority queue endpoint post method."""
        expected = {
            "result": "failure",
            "message": "Invalid url: url is not supported."
        }
        client = self.app.test_client()
        response = client.post("/queue/priority", json={
            "url":
            "https://www.formula1.com/"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_get_version(self):
        """Test the get version function."""
        self.assertEqual(get_version(), {"version": "0.5.0"})

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
