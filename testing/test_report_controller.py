"""
This module contains tests for the report controller.
"""

from testing.test_version_queue_endpoints import TestApiEndpointsV1

class TestReportController(TestApiEndpointsV1):
    """
    This class contains tests for the report controller.
    """

    def test_incident_endpoint(self):
        """
        This method tests the incident endpoint.
        """
        request = {
            "id": "1",
            "timestamp": "2021-01-01 00:00:00",
            "message": "Testing"
        }
        expected = {
            "status": 200,
            "result": "success",
            "message": "Incident reported successfully."
        }
        response = self.client.post("/incident", json=request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_invalid_incident_endpoint(self):
        """
        This method tests the incident endpoint with an invalid request.
        """
        request = {
            "id": "1",
            "timestamp": "2021-01-01 00:00:00"
        }
        expected = {
            "status": 400,
            "result": "failure",
            "message": "Invalid request body."
        }
        response = self.client.post("/incident", json=request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, expected)

    def test_request_endpoint(self):
        """
        This method tests the request endpoint.
        """
        request = {
            "id": "1",
            "timestamp": "2021-01-01 00:00:00",
            "message": "Testing"
        }
        expected = {
            "status": 200,
            "result": "success",
            "message": "Request submitted successfully."
        }
        response = self.client.post("/request", json=request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_invalid_request_endpoint(self):
        """
        This method tests the request endpoint with an invalid request.
        """
        request = {
            "id": "1",
            "timestamp": "2021-01-01 00:00:00"
        }
        expected = {
            "status": 400,
            "result": "failure",
            "message": "Invalid request body."
        }
        response = self.client.post("/request", json=request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, expected)
