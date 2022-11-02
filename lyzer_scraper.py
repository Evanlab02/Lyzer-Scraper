"""
This is module acts as the main entry point for our web scraper program.
"""

# System imports
import sys

from scraper.web_scraper import Scraper

def main():
    """
    This is the main function for our web scraper program.
    """
    scraper = Scraper() # Instance of the scraper class
    scraper.start() # Start the scraper
    return 0 # Exit code 0

if __name__ == "__main__":
    EXIT_CODE = main() # Call main function
    sys.exit(EXIT_CODE) # Exit program
