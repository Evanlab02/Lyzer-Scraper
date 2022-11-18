"""
This will test the web scraper class.
"""

from io import StringIO
import json
import os
import unittest
from unittest.mock import patch

from src.web_scraper import WebScraper

class TestWebScraper(unittest.TestCase):
    """
    This class contains the tests to test the WebScraper.
    """

    @patch("sys.stdout", StringIO())
    def setUp(self):
        """
        This will run before each test.
        """
        self.web_scraper = WebScraper()

    @patch("sys.stdout", StringIO())
    def test_scrape_site_year_too_soon(self):
        """
        This will test the scrape_site method.
        """
        with self.assertRaises(RuntimeError):
            self.web_scraper.scrape_site(("races", 1940, "All"),
            "https://www.formula1.com/en/results.html/1940/races.html")

    @patch("sys.stdout", StringIO())
    def test_scrape_site_year_too_far(self):
        """
        This will test the scrape_site method.
        """
        with self.assertRaises(RuntimeError):
            self.web_scraper.scrape_site(("races", 2300, "All"),
            "https://www.formula1.com/en/results.html/2300/races.html")

    @patch("sys.stdout", StringIO())
    def test_scrape_season_summary_page(self):
        """
        This will test the scrape_site method.
        """
        headers, data_rows = self.web_scraper.scrape_site(("races", 2021, "All"),
        "https://www.formula1.com/en/results.html/2021/races.html")
        self.assertEqual(headers, [
            "Grand Prix",
            "Date",
            "Winner",
            "Car",
            "Laps",
            "Time"
        ])
        self.assertEqual(data_rows,
        [
['Bahrain','28 Mar 2021','Lewis Hamilton','Mercedes','56','1:32:03.897'],
['Emilia Romagna','18 Apr 2021','Max Verstappen','Red Bull Racing Honda','63','2:02:34.598'],
['Portugal','02 May 2021','Lewis Hamilton','Mercedes','66','1:34:31.421'],
['Spain','09 May 2021','Lewis Hamilton', 'Mercedes', '66', '1:33:07.680'],
['Monaco','23 May 2021','Max Verstappen','Red Bull Racing Honda','78','1:38:56.820'],
['Azerbaijan','06 Jun 2021','Sergio Perez', 'Red Bull Racing Honda', '51', '2:13:36.410'],
['France','20 Jun 2021', 'Max Verstappen', 'Red Bull Racing Honda', '53', '1:27:25.770'],
['Styria','27 Jun 2021', 'Max Verstappen', 'Red Bull Racing Honda', '71', '1:22:18.925'],
['Austria','04 Jul 2021', 'Max Verstappen', 'Red Bull Racing Honda', '71', '1:23:54.543'],
['Great Britain','18 Jul 2021', 'Lewis Hamilton', 'Mercedes', '52', '1:58:23.284'],
['Hungary','01 Aug 2021', 'Esteban Ocon', 'Alpine Renault', '70', '2:04:43.199'],
['Belgium','29 Aug 2021', 'Max Verstappen', 'Red Bull Racing Honda', '1', '0:03:27.071'],
['Netherlands','05 Sep 2021', 'Max Verstappen', 'Red Bull Racing Honda', '72', '1:30:05.395'],
['Italy','12 Sep 2021', 'Daniel Ricciardo', 'McLaren Mercedes', '53', '1:21:54.365'],
['Russia','26 Sep 2021', 'Lewis Hamilton', 'Mercedes', '53', '1:30:41.001'],
['Turkey','10 Oct 2021', 'Valtteri Bottas', 'Mercedes', '58', '1:31:04.103'],
['United States','24 Oct 2021', 'Max Verstappen', 'Red Bull Racing Honda', '56', '1:34:36.552'],
['Mexico','07 Nov 2021', 'Max Verstappen', 'Red Bull Racing Honda', '71', '1:38:39.086'],
['Brazil','14 Nov 2021', 'Lewis Hamilton', 'Mercedes', '71', '1:32:22.851'],
['Qatar','21 Nov 2021', 'Lewis Hamilton', 'Mercedes', '57', '1:24:28.471'],
['Saudi Arabia','05 Dec 2021', 'Lewis Hamilton', 'Mercedes', '50', '2:06:15.118'],
['Abu Dhabi','12 Dec 2021','Max Verstappen','Red Bull Racing Honda','58','1:30:17.345']
        ])

    @patch("sys.stdout", StringIO())
    def test_scrape_season_summary_page_three_years(self):
        """
        This will test the scrape_site method.
        """
        for year in range(2018, 2022):
            headers, data_rows = self.web_scraper.scrape_site(("races", year, "All"),
            f"https://www.formula1.com/en/results.html/{year}/races.html")
            self.assertEqual(len(headers), 6)
            for data_row in data_rows:
                self.assertEqual(len(data_row), 6)

    @patch("sys.stdout", StringIO())
    def test_scrape_race_result_page(self):
        """
        This will test the scrape_site method.
        """
        headers, data_rows = self.web_scraper.scrape_site(("races", 2021, "Saudi-arabia"),
        "https://www.formula1.com/en/results.html/2021/races/1106/saudi-arabia/race-result.html")
        self.assertEqual(headers, ['Pos', 'No', 'Driver', 'Car', 'Laps', 'Time/Retired', 'PTS'])
        self.assertEqual(data_rows,
        [
    ['1', '44', 'Lewis Hamilton', 'Mercedes', '50', '2:06:15.118', '26'],
    ['2', '33', 'Max Verstappen', 'Red Bull Racing Honda', '50', '+21.825s', '18'],
    ['3', '77', 'Valtteri Bottas', 'Mercedes', '50', '+27.531s', '15'],
    ['4', '31', 'Esteban Ocon', 'Alpine Renault', '50', '+27.633s', '12'],
    ['5', '3', 'Daniel Ricciardo', 'McLaren Mercedes', '50', '+40.121s', '10'],
    ['6', '10', 'Pierre Gasly', 'AlphaTauri Honda', '50', '+41.613s', '8'],
    ['7', '16', 'Charles Leclerc', 'Ferrari', '50', '+44.475s', '6'],
    ['8', '55', 'Carlos Sainz', 'Ferrari', '50', '+46.606s', '4'],
    ['9', '99', 'Antonio Giovinazzi', 'Alfa Romeo Racing Ferrari', '50', '+58.505s', '2'],
    ['10', '4', 'Lando Norris', 'McLaren Mercedes', '50', '+61.358s', '1'],
    ['11', '18', 'Lance Stroll', 'Aston Martin Mercedes', '50', '+77.212s', '0'],
    ['12', '6', 'Nicholas Latifi', 'Williams Mercedes', '50', '+83.249s', '0'],
    ['13', '14', 'Fernando Alonso', 'Alpine Renault', '49', '+1 lap', '0'],
    ['14', '22', 'Yuki Tsunoda', 'AlphaTauri Honda', '49', '+1 lap', '0'],
    ['15', '7', 'Kimi Raikkonen', 'Alfa Romeo Racing Ferrari', '49', '+1 lap', '0'],
    ['NC', '5', 'Sebastian Vettel', 'Aston Martin Mercedes', '44', 'DNF', '0'],
    ['NC', '11', 'Sergio Perez', 'Red Bull Racing Honda', '14', 'DNF', '0'],
    ['NC', '9', 'Nikita Mazepin', 'Haas Ferrari', '14', 'DNF', '0'],
    ['NC', '63', 'George Russell', 'Williams Mercedes', '14', 'DNF', '0'],
    ['NC', '47', 'Mick Schumacher', 'Haas Ferrari', '8', 'DNF', '0']
        ])

    @patch("sys.stdout", StringIO())
    def test_scrape_fastest_laps_page(self):
        """
        This will test the scrape_site method.
        """
        headers, data_rows = self.web_scraper.scrape_site(("fastest_laps", 2021, "Qatar"),
        "https://www.formula1.com/en/results.html/2021/races/1105/qatar/fastest-laps.html")
        self.assertEqual(headers,
        ['Pos', 'No', 'Driver', 'Car', 'Lap', 'Time of day', 'Time', 'Avg Speed'])
        self.assertEqual(data_rows,
        [
['1', '33', 'Max Verstappen', 'Red Bull Racing Honda', '57', '18:28:42', '1:23.196', '232.799'],
['2', '44', 'Lewis Hamilton', 'Mercedes', '50', '18:17:33', '1:25.084', '227.633'],
['3', '11', 'Sergio Perez', 'Red Bull Racing Honda', '49', '18:17:13', '1:25.613', '226.227'],
['4', '4', 'Lando Norris', 'McLaren Mercedes', '51', '18:20:30', '1:25.746', '225.876'],
['5', '63', 'George Russell', 'Williams Mercedes', '55', '18:28:35', '1:25.768', '225.818'],
['6', '7', 'Kimi Raikkonen', 'Alfa Romeo Racing Ferrari', '53', '18:23:57', '1:26.358','224.275'],
['7', '5', 'Sebastian Vettel', 'Aston Martin Mercedes', '53', '18:23:22', '1:26.434','224.078'],
['8', '16', 'Charles Leclerc', 'Ferrari', '46', '18:13:02', '1:26.555', '223.765'],
['9', '55', 'Carlos Sainz', 'Ferrari', '46', '18:13:00', '1:26.570', '223.726'],
['10', '14', 'Fernando Alonso', 'Alpine Renault', '48', '18:15:33', '1:26.682', '223.437'],
['11', '10', 'Pierre Gasly', 'AlphaTauri Honda', '46', '18:13:13', '1:27.019', '222.572'],
['12', '22', 'Yuki Tsunoda', 'AlphaTauri Honda', '50', '18:19:29', '1:27.043', '222.510'],
['13', '31', 'Esteban Ocon', 'Alpine Renault', '46', '18:12:55', '1:27.061', '222.464'],
['14', '3', 'Daniel Ricciardo', 'McLaren Mercedes', '50', '18:19:26', '1:27.198', '222.115'],
['15', '77', 'Valtteri Bottas', 'Mercedes', '39', '18:03:13', '1:27.246', '221.992'],
['16', '9', 'Nikita Mazepin', 'Haas Ferrari', '55', '18:28:57', '1:27.340', '221.754'],
['17', '18', 'Lance Stroll', 'Aston Martin Mercedes', '44', '18:10:01', '1:27.356', '221.713'],
['18','99','Antonio Giovinazzi','Alfa Romeo Racing Ferrari','40','18:04:59','1:27.823','220.534'],
['19', '47', 'Mick Schumacher', 'Haas Ferrari', '46', '18:13:53', '1:28.412', '219.065'],
['20', '6', 'Nicholas Latifi', 'Williams Mercedes', '44', '18:10:53', '1:28.732', '218.275']
        ])

    @patch("sys.stdout", StringIO())
    def test_scrape_pit_stops_page(self):
        """
        This will test the scrape_site method.
        """
        headers, data_rows = self.web_scraper.scrape_site(("pit_stop_summary", 2021, "Bahrain"),
        "https://www.formula1.com/en/results.html/2021/races/1064/bahrain/pit-stop-summary.html")
        self.assertEqual(headers,
        ['Stops', 'No', 'Driver', 'Car', 'Lap', 'Time of day', 'Time', 'Total'])
        self.assertEqual(data_rows,
        [
['1', '11', 'Sergio Perez', 'Red Bull Racing Honda', '2', '18:11:56', '23.993', '23.993'],
['1', '10', 'Pierre Gasly', 'AlphaTauri Honda', '4', '18:16:14', '38.338', '38.338'],
['1', '14', 'Fernando Alonso', 'Alpine Renault', '11', '18:27:32', '24.373', '24.373'],
['1', '4', 'Lando Norris', 'McLaren Mercedes', '12', '18:29:05', '24.899', '24.899'],
['1', '16', 'Charles Leclerc', 'Ferrari', '12', '18:29:06', '24.925', '24.925'],
['1', '18', 'Lance Stroll', 'Aston Martin Mercedes', '12', '18:29:09', '24.884', '24.884'],
['1', '99', 'Antonio Giovinazzi', 'Alfa Romeo Racing Ferrari', '12', '18:29:14', '31.998','31.998'],
['1', '44', 'Lewis Hamilton', 'Mercedes', '13', '18:30:29', '24.839', '24.839'],
['1', '3', 'Daniel Ricciardo', 'McLaren Mercedes', '13', '18:30:45', '24.688', '24.688'],
['1', '7', 'Kimi Raikkonen', 'Alfa Romeo Racing Ferrari', '13', '18:30:52', '24.107', '24.107'],
['1', '31', 'Esteban Ocon', 'Alpine Renault', '13', '18:30:55', '25.226', '25.226'],
['1', '63', 'George Russell', 'Williams Mercedes', '13', '18:31:02', '24.621', '24.621'],
['1', '6', 'Nicholas Latifi', 'Williams Mercedes', '14', '18:32:44', '26.046', '26.046'],
['1', '47', 'Mick Schumacher', 'Haas Ferrari', '14', '18:32:58', '25.798', '25.798'],
['1', '55', 'Carlos Sainz', 'Ferrari', '15', '18:34:04', '24.353', '24.353'],
['1', '22', 'Yuki Tsunoda', 'AlphaTauri Honda', '15', '18:34:12', '25.046', '25.046'],
['1', '77', 'Valtteri Bottas', 'Mercedes', '16', '18:35:24', '24.262', '24.262'],
['1', '33', 'Max Verstappen', 'Red Bull Racing Honda', '17', '18:36:54', '24.767', '24.767'],
['2', '11', 'Sergio Perez', 'Red Bull Racing Honda', '19', '18:40:35', '24.105', '48.098'],
['2', '10', 'Pierre Gasly', 'AlphaTauri Honda', '19', '18:41:17', '24.317', '1:02.655'],
['1', '5', 'Sebastian Vettel', 'Aston Martin Mercedes', '24', '18:49:08', '24.626', '24.626'],
['2', '44', 'Lewis Hamilton', 'Mercedes', '28', '18:54:40', '24.076', '48.915'],
['2', '18', 'Lance Stroll', 'Aston Martin Mercedes', '28', '18:55:23', '25.525', '50.409'],
['2', '7', 'Kimi Raikkonen', 'Alfa Romeo Racing Ferrari', '29', '18:57:06', '24.046', '48.153'],
['2', '14', 'Fernando Alonso', 'Alpine Renault', '29', '18:57:13', '24.775', '49.148'],
['2', '77', 'Valtteri Bottas', 'Mercedes', '30', '18:57:58', '32.897', '57.159'],
['2', '99', 'Antonio Giovinazzi', 'Alfa Romeo Racing Ferrari', '30', '18:58:53', '24.223','56.221'],
['2', '31', 'Esteban Ocon', 'Alpine Renault', '31', '19:00:29', '24.471', '49.697'],
['2', '16', 'Charles Leclerc', 'Ferrari', '32', '19:01:40', '24.176', '49.101'],
['2', '3', 'Daniel Ricciardo', 'McLaren Mercedes', '32', '19:01:44', '24.655', '49.343'],
['2', '6', 'Nicholas Latifi', 'Williams Mercedes', '32', '19:02:32', '23.983', '50.029'],
['2', '4', 'Lando Norris', 'McLaren Mercedes', '33', '19:03:11', '25.640', '50.539'],
['2', '22', 'Yuki Tsunoda', 'AlphaTauri Honda', '33', '19:03:36', '24.328', '49.374'],
['2', '47', 'Mick Schumacher', 'Haas Ferrari', '33', '19:04:27', '25.343', '51.141'],
['2', '63', 'George Russell', 'Williams Mercedes', '36', '19:08:48', '24.248', '48.869'],
['2', '55', 'Carlos Sainz', 'Ferrari', '37', '19:09:53', '24.341', '48.694'],
['3', '11', 'Sergio Perez', 'Red Bull Racing Honda', '38', '19:11:20', '24.191', '1:12.289'],
['2', '33', 'Max Verstappen', 'Red Bull Racing Honda', '39', '19:12:13', '23.848', '48.615'],
['3', '10', 'Pierre Gasly', 'AlphaTauri Honda', '39', '19:13:55', '24.983', '1:27.638'],
['3', '77', 'Valtteri Bottas', 'Mercedes', '54', '19:36:21', '24.566', '1:21.725']
        ])

    @patch("sys.stdout", StringIO())
    def test_unknown_scrape(self):
        """Test that the scraper can
        handle unknown data"""
        headers, data_rows = self.web_scraper.scrape_site(("unknown", 2021, "unknown"),
        "https://www.formula1.com/en/results.html/2021/fastest-laps.html")
        self.assertEqual(headers, ['Grand Prix', 'Driver', 'Car', 'Time'])
        self.assertEqual(data_rows, [
    ['Bahrain', 'Valtteri Bottas', 'Mercedes', '1:32.090'],
    ['Emilia Romagna', 'Lewis Hamilton', 'Mercedes', '1:16.702'],
    ['Portugal', 'Valtteri Bottas', 'Mercedes', '1:19.865'],
    ['Spain', 'Max Verstappen', 'Red Bull Racing Honda', '1:18.149'],
    ['Monaco', 'Lewis Hamilton', 'Mercedes', '1:12.909'],
    ['Azerbaijan', 'Max Verstappen', 'Red Bull Racing Honda', '1:44.481'],
    ['France', 'Max Verstappen', 'Red Bull Racing Honda', '1:36.404'],
    ['Styria', 'Lewis Hamilton', 'Mercedes', '1:07.058'],
    ['Austria', 'Max Verstappen', 'Red Bull Racing Honda', '1:06.200'],
    ['Great Britain', 'Sergio Perez', 'Red Bull Racing Honda', '1:28.617'],
    ['Hungary', 'Pierre Gasly', 'AlphaTauri Honda', '1:18.394'],
    ['Netherlands', 'Lewis Hamilton', 'Mercedes', '1:11.097'],
    ['Italy', 'Daniel Ricciardo', 'McLaren Mercedes', '1:24.812'],
    ['Russia', 'Lando Norris', 'McLaren Mercedes', '1:37.423'],
    ['Turkey', 'Valtteri Bottas', 'Mercedes', '1:30.432'],
    ['United States', 'Lewis Hamilton', 'Mercedes', '1:38.485'],
    ['Mexico', 'Valtteri Bottas', 'Mercedes', '1:17.774'],
    ['Brazil', 'Sergio Perez', 'Red Bull Racing Honda', '1:11.010'],
    ['Qatar', 'Max Verstappen', 'Red Bull Racing Honda', '1:23.196'],
    ['Saudi Arabia', 'Lewis Hamilton', 'Mercedes', '1:30.734'],
    ['Abu Dhabi', 'Max Verstappen', 'Red Bull Racing Honda', '1:26.103']
        ])

    @patch("sys.stdout", StringIO())
    def test_compile_data(self):
        """Test that the scraper can
        compile data"""
        os.mkdir("testing/resources/.lyzer/")
        os.system("touch testing/resources/.lyzer/testing.json")

        self.web_scraper.compile_and_save_data({
            "headers": ["header"],
            "data_rows": [["data"]],
            "url_data": ("testing", 2021, "Barcelona"),
            "home_directory": "testing/resources",
            "link": "https://www.formula1.com/en/results.html/2021/races.html"
        })
        self.assertTrue(os.path.exists("testing/resources/.lyzer/testing.json"))
        with open("testing/resources/.lyzer/testing.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            self.assertEqual(data,
            {'2021': {"Barcelona": {"Headers": ["header"], "Data": [["data"]]}}})

        self.assertTrue(os.path.exists("testing/resources/.lyzer/links.json"))
        with open("testing/resources/.lyzer/links.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            self.assertEqual(data,
            ["https://www.formula1.com/en/results.html/2021/races.html"])

        os.remove("testing/resources/.lyzer/testing.json")
        os.remove("testing/resources/.lyzer/links.json")
        os.rmdir("testing/resources/.lyzer/")
