"""
This module will contain the logic to test the backlog api module.
"""

import unittest

from api.backlog_api import get_queue, add_to_queue
from source.installer import uninstall_lyzer_data_files

class TestBacklogApi(unittest.TestCase):
    """Test the backlog api module."""
    def test_get_queue_with_no_queue_file(self):
        """Test the get queue function."""
        uninstall_lyzer_data_files()
        expected = {
            "result": "failure",
            "message": "Internal server error: backlog file not found."
        }
        self.assertEqual(get_queue(), expected)

    def test_add_to_queue_with_no_queue_file(self):
        """Test the add to queue function."""
        uninstall_lyzer_data_files()
        expected = {
            "result": "failure",
            "message": "Internal server error: backlog file not found."
        }
        self.assertEqual(add_to_queue(), expected)
