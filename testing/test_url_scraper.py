"""
This module will contain the tests for the url scraper class.
"""

from io import StringIO

import unittest
from unittest.mock import patch

from src.url_scraper import UrlScraper

class TestUrlScraper(unittest.TestCase):
    """
    This class will contain the tests for the url scraper class.
    """

    def setUp(self):
        """
        This will setup the tests.
        """
        self.locations = [
            "bahrain",
            "portugal",
            "spain",
            "monaco",
            "canada",
            "france",
            "austria",
            "great-britain",
            "hungary",
            "belgium",
            "italy",
            "singapore",
            "russia",
            "japan",
            "united-states",
            "mexico",
            "brazil",
            "abu-dhabi",
        ]

    @patch("sys.stdout", StringIO())
    def test_start(self):
        """
        This will test the start method.
        """
        url = "https://www.formula1.com/en/results.html/2022/races.html"
        url_scraper = UrlScraper(url)
        elements = url_scraper.start()
        self.assertEqual(elements, ["2022", "races.html"])

    @patch("sys.stdout", StringIO())
    def test_start_with_less_than_2_elements(self):
        """
        This will test the start method with less than 2 elements.
        """
        url = "https://www.formula1.com/en/results.html/2022"
        url_scraper = UrlScraper(url)
        with self.assertRaises(IndexError):
            url_scraper.start()

    @patch("sys.stdout", StringIO())
    def test_start_with_small_link(self):
        """
        This will test the start method with a small link.
        """
        url = "https://www.formula1.com/en"
        url_scraper = UrlScraper(url)
        with self.assertRaises(IndexError):
            url_scraper.start()

    @patch("sys.stdout", StringIO())
    def test_start_with_almost_perfect_link(self):
        """
        This will test the start method with a small link.
        """
        url = "https://www.formula1.com/en/results.html/2022/"
        url_scraper = UrlScraper(url)
        with self.assertRaises(IndexError):
            url_scraper.start()

    @patch("sys.stdout", StringIO())
    def test_get_year_from_url(self):
        """
        This will test the get_year_from_url method.
        """
        url = "https://www.formula1.com/en/results.html/2022/races.html"
        url_scraper = UrlScraper(url)
        url_scraper.start()
        year = url_scraper.get_year_from_url()
        self.assertEqual(year, 2022)

    @patch("sys.stdout", StringIO())
    def test_get_invalid_year_from_url(self):
        """
        This will test the get_year_from_url method.
        """
        url = "https://www.formula1.com/en/results.html/abcd/races.html"
        url_scraper = UrlScraper(url)
        url_scraper.start()
        with self.assertRaises(ValueError):
            url_scraper.get_year_from_url()

    @patch("sys.stdout", StringIO())
    def test_get_invalid_index_from_url(self):
        """
        This will test the get_year_from_url method.
        """
        url = "https://www.formula1.com/en/results.html/abcd/races.html"
        url_scraper = UrlScraper(url)
        with self.assertRaises(IndexError):
            url_scraper.get_year_from_url()


    @patch("sys.stdout", StringIO())
    def test_generate_url_data(self):
        """
        This will test the generate_url_data method.
        """
        url = "https://www.formula1.com/en/results.html/2022/races.html"
        url_scraper = UrlScraper(url)
        url_elements = url_scraper.start()
        url_year = url_scraper.get_year_from_url()
        url_data = url_scraper.generate_url_data(url_elements, url_year)
        self.assertEqual(url_data, ("races", 2022, "All"))

    @patch("sys.stdout", StringIO())
    def test_generate_url_data_individual_race_result(self):
        """
        This will test the generate_url_data method.
        """
        url = "https://www.formula1.com/en/results.html/2022/races/1124/bahrain/race-result.html"
        url_scraper = UrlScraper(url)
        url_elements = url_scraper.start()
        url_year = url_scraper.get_year_from_url()
        url_data = url_scraper.generate_url_data(url_elements, url_year)
        self.assertEqual(url_data, ("races", 2022, "Bahrain"))

    @patch("sys.stdout", StringIO())
    def test_generate_url_data_future_year(self):
        """
        This will test the generate_url_data method.
        """
        url = "https://www.formula1.com/en/results.html/2102/races/1124/bahrain/race-result.html"
        url_scraper = UrlScraper(url)
        url_elements = url_scraper.start()
        url_year = url_scraper.get_year_from_url()
        with self.assertRaises(ValueError):
            url_scraper.generate_url_data(url_elements, url_year)

    @patch("sys.stdout", StringIO())
    def test_generate_url_data_race_results(self):
        """
        This will test the generate_url_data method.
        """
        for year in range(1950, 2023):
            for location in self.locations:
                url = f"https://www.formula1.com/en/results.html/{year}"+\
                    f"/races/1124/{location}/race-result.html"
                url_scraper = UrlScraper(url)
                url_elements = url_scraper.start()
                url_year = url_scraper.get_year_from_url()
                url_data = url_scraper.generate_url_data(url_elements, url_year)
                self.assertEqual(url_data[0], "races")
                self.assertEqual(url_data[1], year)
                self.assertEqual(url_data[2], location.capitalize())

    @patch("sys.stdout", StringIO())
    def test_generate_url_data_race_results_summaries(self):
        """
        This will test the generate_url_data method.
        """
        for year in range(1950, 2023):
            url = f"https://www.formula1.com/en/results.html/{year}/races.html"
            url_scraper = UrlScraper(url)
            url_elements = url_scraper.start()
            url_year = url_scraper.get_year_from_url()
            url_data = url_scraper.generate_url_data(url_elements, url_year)
            self.assertEqual(url_data[0], "races")
            self.assertEqual(url_data[1], year)
            self.assertEqual(url_data[2], "All")


    @patch("sys.stdout", StringIO())
    def test_generate_url_data_fastest_laps(self):
        """
        This will test the generate_url_data method.
        """
        for year in range(1950, 2023):
            for location in self.locations:
                url = f"https://www.formula1.com/en/results.html/{year}"+\
                    f"/races/1124/{location}/fastest-laps.html"
                url_scraper = UrlScraper(url)
                url_elements = url_scraper.start()
                url_year = url_scraper.get_year_from_url()
                url_data = url_scraper.generate_url_data(url_elements, url_year)
                self.assertEqual(url_data[0], "fastest_laps")
                self.assertEqual(url_data[1], year)
                self.assertEqual(url_data[2], location.capitalize())

    @patch("sys.stdout", StringIO())
    def test_generate_url_data_pit_stop_summary(self):
        """
        This will test the generate_url_data method.
        """
        for year in range(1950, 2023):
            for location in self.locations:
                url = f"https://www.formula1.com/en/results.html/{year}/races"+\
                    f"/1124/{location}/pit-stop-summary.html"
                url_scraper = UrlScraper(url)
                url_elements = url_scraper.start()
                url_year = url_scraper.get_year_from_url()
                url_data = url_scraper.generate_url_data(url_elements, url_year)
                self.assertEqual(url_data[0], "pit_stop_summary")
                self.assertEqual(url_data[1], year)
                self.assertEqual(url_data[2], location.capitalize())

    @patch("sys.stdout", StringIO())
    def test_generate_url_data_unknown_summary(self):
        """
        This will test the generate_url_data method.
        """
        for year in range(1950, 2023):
            for location in self.locations:
                url = f"https://www.formula1.com/en/results.html/{year}"\
                    +f"/races/1124/{location}/unknown"
                url_scraper = UrlScraper(url)
                url_elements = url_scraper.start()
                url_year = url_scraper.get_year_from_url()
                url_data = url_scraper.generate_url_data(url_elements, url_year)
                self.assertEqual(url_data[0], "unknown")
                self.assertEqual(url_data[1], year)
                self.assertEqual(url_data[2], "unknown")
