"""
This module will contain the class that will be used to scrape data from the given url.
"""

import sys

class UrlScraper:
    """
    This class will be used to scrape data from the given url.
    """

    def __init__(self, url: str=""):
        """
        This is the constructor for the url scraper class.

        Args:
            url (str, optional): The url to scrape. Defaults to "".
        """
        self.url = url # The url to scrape
        self.url_elements = [] # The elements of the url

    def start(self):
        """
        This will get the elements of the url.

        Returns:
            list: The elements of the url.
        """
        self.url_elements = self.url.split("/")

        self.url_elements.pop(0) # Remove the first element
        self.url_elements.pop(0) # Remove the second element
        self.url_elements.pop(0) # Remove the third element
        self.url_elements.pop(0) # Remove the fourth element
        self.url_elements.pop(0) # Remove the fifth element

        print("Link elements ->", self.url_elements)

        return self.url_elements

    def get_year_from_url(self):
        """
        This will get the year from the url.

        Returns:
            int: The year from the url.
        """
        year = self.url_elements[0]
        try:
            year = int(year)
        except ValueError:
            print("The year is not a valid integer.")
            sys.exit(2)
        return year

    def generate_url_data(self, url_elements: list, year: int):
        """
        This will generate the url data.

        Args:
            url_elements (list): The elements of the url.
            year (int): The year from the url.
        """
        if "races" in url_elements[1] and len(url_elements) == 2:
            print("Year ->", year)
            location = "All"
            print("Location ->", location)
            return "races", year, location

        if (
            "races" in url_elements[1]
            and len(url_elements) == 5
            and url_elements[4] == "race-result.html"
            ):
            print("Year ->", year)
            location = url_elements[3]
            print("Location ->", location)
            return "races", year, location.capitalize()

        if (
            "races" in url_elements[1]
            and len(url_elements) == 5
            and url_elements[4] == "fastest-laps.html"
            ):
            print("Year ->", year)
            location = url_elements[3]
            print("Location ->", location)
            return "fastest_laps", year, location.capitalize()

        if (
            "races" in url_elements[1]
            and len(url_elements) == 5
            and url_elements[4] == "pit-stop-summary.html"
            ):
            print("Year ->", year)
            location = url_elements[3]
            print("Location ->", location)
            return "pit_stop_summary", year, location.capitalize()

        return "unknown", year, "unknown"
