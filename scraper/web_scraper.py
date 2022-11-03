"""
This module will contain a class that will be used to scrape data from the web.
"""

import sys

from datetime import datetime

from scraper.url_scraper import UrlScraper
from scraper.site_scraper import SiteScraper

class WebScraper:
    """
    This class will be used to scrape data from the web.
    """

    def __init__(self):
        """
        This is the constructor for the scraper class.
        """
        self.version = "0.1.0" # Version of the scraper class
        self.url_scraper = UrlScraper() # Instance of the url scraper class
        self.link = "" # List of links to scrape
        self.file = "" # File to store data in

    def start(self):
        """
        This will start the scraper.
        """
        print("Scraper is starting...") # Print to console that scraper is running
        print("Version: " + self.version) # Print version of scraper
        return 0

    def scrape_site(self, data: tuple, link: str=""):
        """
        This will get the data from the link we are adding to the scraper.
        """
        site_scraper = SiteScraper(data)
        print("Site scraping will start soon...")

        if (data[0] == "races" and
        data[1] in range(1950, datetime.now().year + 1) and
        data[2] == "All"):
            site_scraper.race_season_summary_scrape(link)
        else:
            print("I don't know what to do with this data yet.")
            sys.exit(1)
        return 0
