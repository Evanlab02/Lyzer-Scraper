"""
This module will test the installer class.
"""

import unittest

from unittest.mock import patch
from io import StringIO

from scraper.installer import Installer

class TestInstaller(unittest.TestCase):
    """
    This class will test the installer class.
    """

    @patch("sys.stdout", StringIO())
    def setUp(self):
        """
        This will set up the tests.
        """
        self.installer = Installer()

    @patch("sys.stdout", StringIO())
    def test_introduce(self):
        """
        This will test the introduce method.
        """
        self.assertEqual(self.installer, self.installer.introduce())

    @patch("sys.stdout", StringIO())
    def test_install_and_removal_data_directory(self):
        """
        This will test the install_data_directory method.
        """
        self.assertTrue(self.installer.install_data_directory(".test_data/"))
        self.assertFalse(self.installer.install_data_directory(".test_data/"))
        self.assertTrue(self.installer.remove_data_directory(".test_data/"))
        self.assertFalse(self.installer.remove_data_directory(".test_data/"))

    @patch("sys.stdout", StringIO())
    def test_install_and_remove_data_file(self):
        """
        This will test the install_data_file method.
        """
        self.assertTrue(self.installer.install_data_directory(".test_data/"))
        self.assertTrue(self.installer.install_data_file("test.txt", ".test_data/"))
        self.assertFalse(self.installer.install_data_file("test.txt", ".test_data/"))
        self.assertTrue(self.installer.remove_data_file("test.txt", ".test_data/"))
        self.assertFalse(self.installer.remove_data_file("test.txt", ".test_data/"))
        self.assertTrue(self.installer.remove_data_directory(".test_data/"))
