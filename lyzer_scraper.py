"""
This is module acts as the main entry point for our web scraper program.
"""

# System imports
import sys

from scraper.cli_parser import get_link
from scraper.installer import Installer
from scraper.url_scraper import UrlScraper
from scraper.web_scraper import WebScraper


def main():
    """
    This is the main function for our web scraper program.
    """
    scraper = WebScraper() # Instance of the scraper class
    installer = Installer() # Instance of the installer class
    scraper.start() # Start the scraper
    installer.introduce() # Introduce the installer to the user
    installer.install_data_directory() # Install the data directory

    # Installs the data files for the scraper
    data_files = ["races.json"]
    for data_file in data_files:
        installer.install_data_file(data_file)

    link = get_link(sys.argv) # Get the link passed to the scraper

    # Example Link -> "https://www.formula1.com/en/results.html/2022/races.html"
    url_scraper = UrlScraper(link) # Instance of the url scraper class
    url_elements = url_scraper.start()
    url_year = url_scraper.get_year_from_url()
    url_data = url_scraper.generate_url_data(url_elements, url_year)
    print("Type of Link ->", url_data[0])

    print("\nConfiguring scraper for site...")
    print("Data I got from url ->", url_data)
    scraper.scrape_site(url_data, link) # Scrape the site
    return 0 # Exit code 0

if __name__ == "__main__":
    EXIT_CODE = main() # Call main function
    sys.exit(EXIT_CODE) # Exit program
