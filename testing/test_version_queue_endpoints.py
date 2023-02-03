"""
This module will contain the logic to test the api factory module.
"""
import unittest

from api.api_factory import assign_endpoints, get_version
from source.installer import install_lyzer_data_files, uninstall_lyzer_data_files
from web.flask_web_app import create_app

class TestApiEndpointsV1(unittest.TestCase):
    """Test the api factory module."""
    def __init__(self, methodName: str = ...) -> None:
        uninstall_lyzer_data_files()
        install_lyzer_data_files()
        self.app = create_app()
        assign_endpoints(self.app)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        super().__init__(methodName)

    def test_version_endpoint(self):
        """Test the assign endpoints function."""
        client = self.app.test_client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
        "status": 200,
        "result": "success",
        "message": "Data retrieved successfully.",
        "data": "0.6.1"
        })

    def test_queue_endpoint(self):
        """Test the queue endpoint get method."""
        client = self.app.test_client()
        response = client.post("/queue", json=[
            "https://www.youtube.com/watch?v=QH2-TGUlwu4",
            "https://www.youtube.com/watch?v=QH2-TGUlwu4",
            "https://www.youtube.com/watch?v=QH2-TGUlwu4"
            ]
        )
        self.assertEqual(response.status_code, 200)
        json_data = response.json
        result = json_data["result"]
        message = json_data["message"]
        self.assertEqual(result, "success")
        self.assertEqual(message, "Item added to backlog successfully.")
        response = client.get("/queue")
        self.assertEqual(response.status_code, 200)
        json_data = response.json
        result = json_data["result"]
        message = json_data["message"]
        queue = json_data["data"]
        self.assertEqual(result, "success")
        self.assertEqual(message, "Data retrieved successfully.")
        self.assertEqual(queue, [
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
        "message": "Data retrieved successfully.",
        "data": "0.6.1"
        }, 200))
