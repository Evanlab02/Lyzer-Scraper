"""
Tests the main lyzer_scraper module.
"""

import unittest

from lyzer_scraper import main

class MyTestCase(unittest.TestCase):
    def test_return_code_main(self):
        """
        Tests that the main function returns the correct exit code.
        """
        self.assertEqual(main(), 0)
