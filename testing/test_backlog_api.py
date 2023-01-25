"""
This module will contain the logic to test the backlog api module.
"""

import unittest

from api.backlog_controller import get_queue, add_to_queue
from source.installer import uninstall_lyzer_data_files

class TestBacklogApi(unittest.TestCase):
    """Test the backlog api module."""
    def test_get_queue_with_no_queue_file(self):
        """Test the get queue function."""
        uninstall_lyzer_data_files()
        expected = {
            "status": 500,
            "result": "failure",
            "message": "Internal Server Error: Backlog file not found."
        }
        self.assertEqual(get_queue()[0], expected)

    def test_add_to_queue_with_no_queue_file(self):
        """Test the add to queue function."""
        uninstall_lyzer_data_files()
        expected = {
            "status": 500,
            "result": "failure",
            "message": "Internal Server Error: Backlog file not found."
        }
        self.assertEqual(add_to_queue()[0], expected)
