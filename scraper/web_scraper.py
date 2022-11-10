"""
This module will contain a class that will be used to scrape data from the web.
"""

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
        self.version = "0.2.0" # Version of the scraper class
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

        if not data[1] in range(1950, datetime.now().year + 1):
            print("There is no data for this year.")

        if (data[0] == "races" and data[2] == "All"):
            print("\nI believe the url is a season race summary page.")
        elif (data[0] == "races" and data[2] != "All"):
            print("\nI believe the url is a race result page.")
        elif (data[0] == "fastest_laps" and data[2] != "All"):
            print("\nI believe the url is a fastest lap page.")
        elif (data[0] == "pit_stop_summary" and data[2] != "All"):
            print("\nI believe the url is a pit stop summary page.")
        else:
            print("\nI don't know what format this url is in.")
            print("I will try to scrape it anyway.")
            print("I will not be able to save the data to a file.")

        headers, data_rows = site_scraper.site_scrape(link)
        return headers, data_rows
