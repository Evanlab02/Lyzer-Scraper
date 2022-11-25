"""
This module will contain a class that will be used to scrape data from the web.
"""

from datetime import datetime
import os

from rich import print as rich_print

from src.data_compiler import compile_data
from src.file_parser import load_json_data, write_json_data
from src.site_scraper import SiteScraper

class WebScraper:
    """
    This class will be used to scrape data from the web.
    """

    def scrape_site(self, data: tuple, link: str=""):
        """
        This will get the data from the link we are adding to the scraper.

        Args:
            data (tuple): Tuple containing the data from the link.
            link (str, optional): Link to scrape. Defaults to "".

        Returns:
            tuple: Returns a tuple containing the data from the link.

        Raises:

        """
        site_scraper = SiteScraper(data)

        if not data[1] in range(1950, datetime.now().year + 1):
            raise RuntimeError("I grabbed a year that is not possible.")

        headers, data_rows = site_scraper.site_scrape(link)
        return headers, data_rows

    def compile_and_save_data(self, bundled_data: dict):
        """
        This function will compile the data and save it to a file.

        Args:
            headers (list): List of headers for the data.
            data_rows (list): List of data rows.
            url_data (tuple): Tuple containing the data from the link.
        """
        headers = bundled_data["headers"]
        data_rows = bundled_data["data_rows"]
        url_data = bundled_data["url_data"]
        home_directory = bundled_data["home_directory"]
        link = bundled_data["link"]
        if url_data[0] != "unknown":
            data_directory = os.path.join(home_directory, ".lyzer/")
            data_file = os.path.join(data_directory, url_data[0] + ".json")
            json_data = load_json_data(data_file)
            json_data = compile_data(url_data, headers, data_rows, json_data)
            write_json_data(data_file, json_data)
            rich_print("Data has been saved to file ->", data_file)

            data_file = os.path.join(data_directory, "links.json")
            json_data = load_json_data(data_file)
            if isinstance(json_data, dict):
                json_data = []
            if link not in json_data:
                json_data.append(link)
            write_json_data(data_file, json_data)
            rich_print("Link has been saved to file ->", data_file)
