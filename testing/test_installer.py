"""
This will test the installer class.
"""

from io import StringIO

import unittest
from unittest.mock import patch

from src.installer import Installer

class TestInstaller(unittest.TestCase):
    """
    This class contains the tests to test the Installer.
    """

    @patch("sys.stdout", StringIO())
    def setUp(self):
        """
        This will run before each test.
        """
        self.installer = Installer()

    @patch("sys.stdout", StringIO())
    def test_install_data_directory(self):
        """
        This will test the install_data_directory method.
        """
        self.assertTrue(self.installer.install_data_directory(".test_data/"))
        self.assertFalse(self.installer.install_data_directory(".test_data/"))
        self.assertTrue(self.installer.remove_data_directory(".test_data/"))

    @patch("sys.stdout", StringIO())
    def test_install_data_file(self):
        """
        This will test the install_data_file method.
        """
        self.assertTrue(self.installer.install_data_directory(".test_data/"))
        self.assertTrue(self.installer.install_data_file("test_data.json", ".test_data/"))
        self.assertFalse(self.installer.install_data_file("test_data.json", ".test_data/"))
        self.assertTrue(self.installer.remove_data_file("test_data.json", ".test_data/"))
        self.assertFalse(self.installer.remove_data_file("test_data.json", ".test_data/"))
        self.assertTrue(self.installer.remove_data_directory(".test_data/"))
        self.assertFalse(self.installer.remove_data_directory(".test_data/"))
