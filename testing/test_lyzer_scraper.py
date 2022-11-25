"""
This will test the web scraper class.
"""

from io import StringIO

import unittest
from unittest.mock import patch

from lyzer_scraper import start_web_scraper, scrape_link, create_web_app
from src.file_parser import write_json_data, load_json_data
from src.web_scraper import WebScraper

class TestLyzerScraper(unittest.TestCase):
    """
    This class contains the tests to test the Web Scraper.
    """
    @patch("sys.stdout", StringIO())
    def setUp(self):
        """
        This will setup the tests.
        """
        self.locations = [
            "bahrain",
            "portugal",
            "spain"
        ]

    @patch("sys.stdout", StringIO())
    def test_start_web_scraper(self):
        """
        This function will test the start_web_scraper function.
        """
        scraper = start_web_scraper()
        self.assertIsInstance(scraper, WebScraper)

    @patch("sys.stdout", StringIO())
    def test_scrape_link(self):
        """
        This function will test the scrape_link function.
        """

        types = [
            "race-result.html",
            "fastest-laps.html",
            "pit-stop-summary.html",
            "unknown.html"
        ]

        for year in range(1950, 2023):
            for location in self.locations:
                for page_type in types:
                    url = f"https://www.formula1.com/en/results.html/{year}"\
                        +f"/races/1124/{location}/{page_type}"
                    url_elements = scrape_link(url)
                    print(url_elements)
                    self.assertEqual(url_elements[1], year)
                    if page_type == types[0]:
                        self.assertEqual(url_elements[0], "races")
                        self.assertEqual(url_elements[2], location.capitalize())
                    elif page_type == types[1]:
                        self.assertEqual(url_elements[0], "fastest_laps")
                        self.assertEqual(url_elements[2], location.capitalize())
                    elif page_type == types[2]:
                        self.assertEqual(url_elements[0], "pit_stop_summary")
                        self.assertEqual(url_elements[2], location.capitalize())
                    else:
                        self.assertEqual(url_elements[0], "unknown")
                        self.assertEqual(url_elements[2], "unknown")

    @patch("sys.stdout", StringIO())
    def test_links_endpoints(self):
        """
        This function will test the links endpoints.
        """
        app = create_web_app("testing/resources/advanced/")
        app.config["TESTING"] = True
        with app.app_context():
            with app.test_client() as client:
                response = client.post("/links", json=[
                "https://www.formula1.com/en/results.html/2021/races.html",
                "https://www.formula1.com/en/results.html/2022/races.html"
                ])
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json, {"exit_codes":[0, 0]})

                response = client.get("/links", content_type="application/json")
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json, [
                "https://www.formula1.com/en/results.html/2021/races.html",
                "https://www.formula1.com/en/results.html/2022/races.html"
                ])

                write_json_data("testing/resources/advanced/.lyzer/links.json", [])
                write_json_data("testing/resources/advanced/.lyzer/races.json", {})

    @patch("sys.stdout", StringIO())
    def test_file_race_endpoint(self):
        """
        This function will test the file (races.json) endpoint.
        """
        app = create_web_app("testing/resources/advanced")
        app.config["TESTING"] = True
        with app.app_context():
            with app.test_client() as client:
                response = client.post("/links", json=[
            "https://www.formula1.com/en/results.html/2021/races.html",
            "https://www.formula1.com/en/results.html/2021/races/1064/bahrain/race-result.html"
                ])
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json, {"exit_codes":[0, 0]})

                response = client.get("/file/races", content_type="application/json")
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json, load_json_data("testing/resources/races.json"))

                write_json_data("testing/resources/advanced/.lyzer/links.json", [])
                write_json_data("testing/resources/advanced/.lyzer/races.json", {})

    @patch("sys.stdout", StringIO())
    def test_file_fastest_laps_endpoint(self):
        """
        This function will test the file (races.json) endpoint.
        """
        app = create_web_app("testing/resources/advanced")
        app.config["TESTING"] = True
        with app.app_context():
            with app.test_client() as client:
                response = client.post("/links", json=[
            "https://www.formula1.com/en/results.html/2021/races/1064/bahrain/fastest-laps.html"
                ])
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json, {"exit_codes":[0]})

                response = client.get("/file/fastest_laps", content_type="application/json")
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json,
                load_json_data("testing/resources/fastest_laps.json"))

                write_json_data("testing/resources/advanced/.lyzer/links.json", [])
                write_json_data("testing/resources/advanced/.lyzer/fastest_laps.json", {})

    @patch("sys.stdout", StringIO())
    def test_file_pit_stop_summary_endpoint(self):
        """
        This function will test the file (races.json) endpoint.
        """
        app = create_web_app("testing/resources/advanced")
        app.config["TESTING"] = True
        with app.app_context():
            with app.test_client() as client:
                response = client.post("/links", json=[
        "https://www.formula1.com/en/results.html/2021/races/1064/bahrain/pit-stop-summary.html"
                ])
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json, {"exit_codes":[0]})

                response = client.get("/file/pit_stop_summary", content_type="application/json")
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json,
                load_json_data("testing/resources/pit_stop_summary.json"))

                write_json_data("testing/resources/advanced/.lyzer/links.json", [])
                write_json_data("testing/resources/advanced/.lyzer/pit_stop_summary.json", {})

    @patch("sys.stdout", StringIO())
    def test_file_starting_grid_endpoint(self):
        """
        This function will test the file (races.json) endpoint.
        """
        app = create_web_app("testing/resources/advanced")
        app.config["TESTING"] = True
        with app.app_context():
            with app.test_client() as client:
                response = client.post("/links", json=[
            "https://www.formula1.com/en/results.html/2022/races/1124/bahrain/starting-grid.html"
                ])
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json, {"exit_codes":[0]})

                response = client.get("/file/starting_grid", content_type="application/json")
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json,
                load_json_data("testing/resources/starting_grid.json"))

                write_json_data("testing/resources/advanced/.lyzer/links.json", [])
                write_json_data("testing/resources/advanced/.lyzer/starting_grid.json", {})
