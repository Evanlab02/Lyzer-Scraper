"""
This is module acts as the main entry point for our web scraper program.
"""

# System imports
import os
import sys

from scraper.cli_parser import get_link
from scraper.data_compiler import compile_data
from scraper.file_parser import load_json_data, write_json_data
from scraper.installer import Installer
from scraper.url_scraper import UrlScraper
from scraper.web_scraper import WebScraper


def main(args: list):
    """
    This is the main function for our web scraper program.
    """
    scraper = WebScraper() # Instance of the scraper class
    installer = Installer() # Instance of the installer class
    scraper.start() # Start the scraper
    installer.introduce() # Introduce the installer to the user
    installer.install_data_directory() # Install the data directory

    # Installs the data files for the scraper
    data_files = [
        "races.json",
        "fastest_laps.json",
        "pit_stop_summary.json"
    ]

    for data_file in data_files:
        installer.install_data_file(data_file)

    link = get_link(args) # Get the link passed to the scraper

    # Example Link -> "https://www.formula1.com/en/results.html/2022/races.html"
    url_scraper = UrlScraper(link) # Instance of the url scraper class
    url_elements = url_scraper.start()
    url_year = url_scraper.get_year_from_url()
    url_data = url_scraper.generate_url_data(url_elements, url_year)
    print("Type of Link ->", url_data[0])

    print("\nConfiguring scraper for site...")
    print("Data I got from url ->", url_data)
    headers, data_rows = scraper.scrape_site(url_data, link) # Scrape the site

    if url_data[0] != "unknown":
        home_directory = installer.home_directory
        data_directory = os.path.join(home_directory, ".lyzer/")
        data_file = os.path.join(data_directory, url_data[0] + ".json")

        print("\nLoading data from file ->", data_file)
        json_data = load_json_data(data_file)

        print("Compiling data...")
        json_data = compile_data(url_data, headers, data_rows, json_data)

        print("Writing data to file ->", data_file)
        write_json_data(data_file, json_data)
        print("Data has been saved to file ->", data_file)
        print("Scraper shutting down...")

    return 0 # Exit code 0

if __name__ == "__main__":
    EXIT_CODE = main(sys.argv) # Call main function
    sys.exit(EXIT_CODE) # Exit program
