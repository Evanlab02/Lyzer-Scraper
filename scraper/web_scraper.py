"""
This module will contain a class that will be used to scrape data from the web.
"""

from scraper.installer import Installer

class Scraper:
    """
    This class will be used to scrape data from the web.
    """

    def __init__(self):
        """
        This is the constructor for the scraper class.
        """
        self.version = "0.1.0" # Version of the scraper class
        self.installer = Installer() # Instance of the installer class

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
        return 0