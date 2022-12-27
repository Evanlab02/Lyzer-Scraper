"""
This module will contain the logic to test the data compiler module.
"""

import unittest

from source.data_compiler import (
    compile_team_data,
    compile_driver_data,
    compile_race_data
)

class TestDataCompiler(unittest.TestCase):
    """Tests the data compiler module."""

    def test_compile_team_data_with_new_year(self):
        """Test the compile team data function."""
        site_data = {
            "url": "https://www.formula1.com/en/results.html/2022/team/alfa_romeo_ferrari.html",
            "year": "2022",
            "team": "Alfa Romeo Ferrari",
            "headers": ["These", "are", "the", "headers"],
            "rows": [["These", "are", "the", "rows"], ["These", "are", "the", "rows"]]
        }
        data = {}
        compile_team_data(site_data, data)
        expected = {
            "2022": {
                "Alfa Romeo Ferrari": {
                    "url":
                    "https://www.formula1.com/en/results.html/2022/team/alfa_romeo_ferrari.html",
                    "headers": ["These", "are", "the", "headers"],
                    "rows": [["These", "are", "the", "rows"], ["These", "are", "the", "rows"]]
                }
            }
        }
        self.assertEqual(data, expected)

    def test_compile_team_data_with_existing_team(self):
        """Test the compile team data function."""
        site_data = {
            "url": "https://www.formula1.com/en/results.html/2022/team/alfa_romeo_ferrari.html",
            "year": "2022",
            "team": "Alfa Romeo Ferrari",
            "headers": ["These", "are", "the", "headers"],
            "rows": [["These", "are", "the", "rows"], ["These", "are", "the", "rows"]]
        }
        data = {
            "2022": {
                "Alfa Romeo Ferrari": {
                    "url":
                    "https://www.formula1.com/en/results.html/2022/team/alfa_romeo_ferrari.html",
                    "headers": ["These", "are", "the", "headers"],
                    "rows": [["These", "are", "the", "rows"], ["These", "are", "the", "rows"]]
                }
            }
        }
        compile_team_data(site_data, data)
        expected = {
            "2022": {
                "Alfa Romeo Ferrari": {
                    "url":
                    "https://www.formula1.com/en/results.html/2022/team/alfa_romeo_ferrari.html",
                    "headers": ["These", "are", "the", "headers"],
                    "rows": [["These", "are", "the", "rows"], ["These", "are", "the", "rows"]]
                }
            }
        }
        self.assertEqual(data, expected)

    def test_compile_driver_data_with_new_year(self):
        """Test the compile driver data function."""
        site_data = {
            "url": "https://www.formula1.com/en/results.html/2022/drivers/lewis_hamilton.html",
            "year": "2022",
            "driver": "Lewis Hamilton",
            "headers": ["These", "are", "the", "headers"],
            "rows": [["These", "are", "the", "rows"], ["These", "are", "the", "rows"]]
        }
        data = {}
        compile_driver_data(site_data, data)
        expected = {
            "2022": {
                "Lewis Hamilton": {
                    "url":
                    "https://www.formula1.com/en/results.html/2022/drivers/lewis_hamilton.html",
                    "headers": ["These", "are", "the", "headers"],
                    "rows": [["These", "are", "the", "rows"], ["These", "are", "the", "rows"]]
                }
            }
        }
        self.assertEqual(data, expected)

    def test_compile_driver_data_with_existing_driver(self):
        """Test the compile driver data function."""
        site_data = {
            "url": "https://www.formula1.com/en/results.html/2022/drivers/lewis_hamilton.html",
            "year": "2022",
            "driver": "Lewis Hamilton",
            "headers": ["These", "are", "the", "headers"],
            "rows": [["These", "are", "the", "rows"], ["These", "are", "the", "rows"]]
        }
        data = {
            "2022": {
                "Lewis Hamilton": {
                    "url":
                    "https://www.formula1.com/en/results.html/2022/drivers/lewis_hamilton.html",
                    "headers": ["These", "are", "the", "headers"],
                    "rows": [["These", "are", "the", "rows"], ["These", "are", "the", "rows"]]
                }
            }
        }
        compile_driver_data(site_data, data)
        expected = {
            "2022": {
                "Lewis Hamilton": {
                    "url":
                    "https://www.formula1.com/en/results.html/2022/drivers/lewis_hamilton.html",
                    "headers": ["These", "are", "the", "headers"],
                    "rows": [["These", "are", "the", "rows"], ["These", "are", "the", "rows"]]
                }
            }
        }
        self.assertEqual(data, expected)

    def test_compile_race_data_with_new_year(self):
        """Test the compile race data function."""
        site_data = {
            "url":
            "https://www.formula1.com/en/results.html/2022/races/1124/bahrain/race-result.html",
            "year": "2022",
            "location": "Bahrain",
            "headers": ["This", "is", "a", "header"],
            "rows": [["This", "is", "a", "row"], ["This", "is", "a", "row"]]
        }
        data = {}
        compile_race_data(site_data, data)
        expected = {
            "2022": {
                "Bahrain": {
                "url":
                "https://www.formula1.com/en/results.html/2022/races/1124/bahrain/race-result.html",
                "headers": ["This", "is", "a", "header"],
                "rows": [["This", "is", "a", "row"], ["This", "is", "a", "row"]]
                }
            }
        }

        self.assertEqual(data, expected)

    def test_compile_race_data_with_existing_location(self):
        """
        This test is to make sure that the compile race data function is
        working as expected.
        """
        site_data = {
            "url":
            "https://www.formula1.com/en/results.html/2022/races/1124/bahrain/race-result.html",
            "year": "2022",
            "location": "Bahrain",
            "headers": ["This", "is", "a", "header"],
            "rows": [["This", "is", "a", "row"], ["This", "is", "a", "row"]]
        }
        data = {
            "2022": {
                "Bahrain": {
                "url":
                "https://www.formula1.com/en/results.html/2022/races/1124/bahrain/race-result.html",
                "headers": ["This", "is", "a", "header"],
                "rows": [["This", "is", "a", "row"], ["This", "is", "a", "row"]]
                }
            }
        }
        compile_race_data(site_data, data)
        expected = {
            "2022": {
                "Bahrain": {
                "url":
                "https://www.formula1.com/en/results.html/2022/races/1124/bahrain/race-result.html",
                "headers": ["This", "is", "a", "header"],
                "rows": [["This", "is", "a", "row"], ["This", "is", "a", "row"]]
                }
            }
        }
        self.assertEqual(data, expected)
