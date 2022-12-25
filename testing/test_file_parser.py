"""
This module will contain the class that will test the file parser module.
"""

import os
import unittest

from source.file_parser import (
    create_text_file,
    create_data_directory,
    create_json_file,
    read_json_file,
    write_json_file
    )

class TestFileParser(unittest.TestCase):
    """This class contains the tests for the file parser module."""
    def setUp(self) -> None:
        """Set up the test class."""
        if os.path.exists("testing/test.txt"):
            os.remove("testing/test.txt")
        if os.path.exists("testing/test"):
            os.rmdir("testing/test")
        if not os.path.exists("testing/test.json"):
            create_json_file("testing/test.json")
        return super().setUp()

    def test_create_text_file_invalid_file(self):
        """Test the create_text_file function."""
        self.assertFalse(create_text_file("testing/test.json"))

    def test_create_text_file_valid_file(self):
        """Test the create_text_file function."""
        self.assertTrue(create_text_file("testing/test.txt"))
        self.assertTrue(os.path.exists("testing/test.txt"))

    def test_create_json_file_invalid_file(self):
        """Test the create_json_file function."""
        self.assertFalse(create_json_file("testing/test.txt"))

    def test_create_json_file_valid_file(self):
        """Test the create_json_file function."""
        os.remove("testing/test.json")
        self.assertTrue(create_json_file("testing/test.json"))
        self.assertTrue(os.path.exists("testing/test.json"))

    def test_create_json_file_existing_file(self):
        """Test the create_json_file function."""
        self.assertFalse(create_json_file("testing/test.json"))
        self.assertTrue(os.path.exists("testing/test.json"))

    def test_create_data_directory_invalid_directory(self):
        """Test the create_data_directory function."""
        self.assertFalse(create_data_directory("testing"))

    def test_create_data_directory_valid_directory(self):
        """Test the create_data_directory function."""
        self.assertTrue(create_data_directory("testing/test/"))
        self.assertTrue(os.path.exists("testing/test/"))

    def test_read_json_file(self):
        """Test the read_json_file function."""
        self.assertEqual(read_json_file("testing/read_test.json"), {"Test": "Test"})

    def test_read_json_file_invalid_file(self):
        """Test the read_json_file function."""
        with self.assertRaises(FileNotFoundError):
            read_json_file("testing/fisher.json")

    def test_write_json_file(self):
        """Test the write_json_file function."""
        write_json_file("testing/write_test.json", {"Test": "Test"})
        self.assertEqual(read_json_file("testing/write_test.json"), {"Test": "Test"})
        write_json_file("testing/write_test.json", {})
