"""
This file contains the class to test all the pit stop endpoints.
"""

from source.installer import install_lyzer_data_files, uninstall_lyzer_data_files
from source.file_parser import write_json_file
from testing.test_version_queue_endpoints import TestApiEndpointsV1

class TestPitstopsEndpoints(TestApiEndpointsV1):
    """
    This class contains all the tests for the pit stop endpoints.
    """

    def test_get_pitstops_endpoint_missing_file(self):
        """
        This method will test the get pit stops endpoint when the file is missing.
        """
        expected = {
            "status": 500,
            "result": "failure",
            "message": "Internal server error: pit stops file not found."
        }
        client = self.app.test_client()
        uninstall_lyzer_data_files()
        response = client.get("/pitstops")
        install_lyzer_data_files()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, expected)

    def test_get_pitstops_endpoint(self):
        """
        This method will test the pit stops endpoint when the file is present.
        """
        write_json_file("data/pit_stop_data.json", {"Testing": "Testing"})
        expected = {
            "status": 200,
            "result": "success",
            "message": "Pit stop data retrieved successfully.",
            "data": {"Testing": "Testing"}
        }
        client = self.app.test_client()
        response = client.get("/pitstops")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)
