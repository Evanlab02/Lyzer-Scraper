"""
This module will contain the class that will test the file logger module.
"""

import os
import unittest

from logs.file_logger import create_log

class TestFileLogger(unittest.TestCase):
    """This class contains the tests for the file logger module."""
    def setUp(self) -> None:
        """Set up the test class."""
        if os.path.exists("logs/logs.txt"):
            os.remove("logs/logs.txt")
        return super().setUp()

    def test_create_log(self):
        """Test the create_log function."""
        self.assertTrue(create_log("Test").endswith("- Test"))
        self.assertTrue(os.path.exists("logs/logs.txt"))
        with open("logs/logs.txt", "r") as file:
            file.readlines()[0].endswith("- Test")
