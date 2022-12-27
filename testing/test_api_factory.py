"""
This module will contain the logic to test the api factory module.
"""
import unittest

from api.api_factory import assign_endpoints, get_version
from source.installer import install_lyzer_data_files, uninstall_lyzer_data_files
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