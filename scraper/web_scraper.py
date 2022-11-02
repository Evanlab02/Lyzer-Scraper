"""
This module will contain a class that will be used to scrape data from the web.
"""

import sys

from datetime import datetime

from scraper.installer import Installer
from scraper.race_scraper import RaceScraper

class Scraper:
    """
    This class will be used to scrape data from the web.
    """

    def __init__(self, args: list=[""]):
        """
        This is the constructor for the scraper class.
        """
        self.version = "0.1.0" # Version of the scraper class
        self.installer = Installer() # Instance of the installer class
        self.args = args # Arguments passed to the scraper
        self.link = "" # List of links to scrape
        self.file = "" # File to store data in

    def start(self):
        """
        This will start the scraper.
        """
        print("Scraper is running...") # Print to console that scraper is running
        print("Version: " + self.version) # Print version of scraper
        return 0

    def install(self, data_directory: str=".lyzer/"):
        """
        This will install the scraper.
        """
        self.installer.introduce() # Introduce the installer to the user
        self.installer.install_data_directory(data_directory) # Install the data directory
        races_file = "races.json" # The file where in all race data will be stored
        self.installer.install_data_file(races_file, data_directory)
        return 0

    def process_args(self):
        """
        This will process the arguments passed to the scraper.

        Returns:
            list: The list of links that were passed to the scraper.
        """
        self.args.pop(0) # Remove the first argument
        for index, arg in enumerate(self.args):
            if arg == "-l" or arg == "--link":
                self.link = (self.args[index + 1])
        return self.link

    def get_details(self):
        """
        This will get the details of the link we are adding to the scraper.
        """
        # "https://www.formula1.com/en/results.html/2022/races.html"
        
        print("Getting details of link...")
        print("Link ->", self.link)

        link_elements = self.link.split("/")

        link_elements.pop(0) # Remove the first element
        link_elements.pop(0) # Remove the second element
        link_elements.pop(0) # Remove the third element
        link_elements.pop(0) # Remove the fourth element
        link_elements.pop(0) # Remove the fifth element

        print("Link elements ->", link_elements)
        year = link_elements[0]

        try:
            year = int(year)
        except ValueError:
            print("The year is not a valid integer.")
            sys.exit(2)

        if "races" in link_elements[1] and len(link_elements) == 2:
            print("Year ->", year)
            location = "All"
            print("Location ->", location)
            return "races", year, location
        else:
            print("I don't know what to do with this link yet.")
            sys.exit(1)

    def scrape_site(self, data: tuple):
        """
        This will get the data from the link we are adding to the scraper.
        """
        print("\nConfiguring scraper...")
        print("Data ->", data)

        if data[0] == "races" \
            and data[1] in range(1950, datetime.now().year + 1) \
                and data[2] == "All":
            race_scraper = RaceScraper(data)
            race_scraper.general_scrape(self.link)
        else:
            print("I don't know what to do with this data yet.")
            sys.exit(1)
        return 0
