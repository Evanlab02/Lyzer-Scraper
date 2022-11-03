"""
This will contain all the logic to scrape race data from the web.
"""
from tabulate import tabulate

from scraper.web_driver import start_driver, stop_driver

class SiteScraper:
    """
    This class will contain all the logic to scrape race data.
    """

    def __init__(self, data: tuple):
        """
        This is the constructor for the race scraper.
        """
        self.data = data

    def get_table_head_and_body(self, soup):
        """
        This will get the table head and body.

        Args:
            soup (BeautifulSoup): The BeautifulSoup object.

        Returns:
            list: The table headers.
            list: The table rows.
        """
        for table in soup.findAll('table', attrs={'class':'resultsarchive-table'}):
            table_head = table.find('thead')
            table_headers = table_head.find_all('th')

            table_body = table.find('tbody')
            table_rows = table_body.find_all('tr')

        return table_headers, table_rows

    def get_headers(self, table_headers):
        """
        This will get the headers

        Args:
            table_headers (list): The table headers.

        Returns:
            list: The headers.
        """
        headers = []
        for header in table_headers:
            if header.text.strip() != "":
                headers.append(header.text)
        return headers

    def get_rows(self, table_rows):
        """
        This will get the rows.

        Args:
            table_rows (list): The table rows.

        Returns:
            list: The rows.
        """
        data_array = []

        for row in table_rows:
            row_data = []
            table_data = row.find_all('td')
            row_data = self.process_data_row(table_data)
            data_array.append(row_data)

        return data_array

    def process_data_row(self, data_rows):
        """
        This will process the row data.

        Args:
            data_rows (list): The data rows.

        Returns:
            list: The processed row data.
        """
        row_data = []
        for data_entry in data_rows:
            data_span = data_entry.find_all('span')

            if len(data_span) == 3:
                data_entry = f"{data_span[0].text} {data_span[1].text}"
            else:
                data_entry = data_entry.text.strip()
                data_entry = data_entry.replace("\n", "")

            if data_entry != "":
                row_data.append(data_entry)

        return row_data

    def race_season_summary_scrape(self, link: str):
        """
        This will scrape season race summary pages.

        Args:
            link (str): The link to the season race summary page.
        """
        print("\nI believe the url is a season race summary page.")
        print("Starting scrape...")
        print("Link: " + link)
        print()

        # Get the content from the link.
        driver, soup = start_driver(link)

        table_headers, table_rows = self.get_table_head_and_body(soup)
        headers = self.get_headers(table_headers)
        data_rows = self.get_rows(table_rows)

        stop_driver(driver)

        table = tabulate(data_rows, headers=headers, tablefmt="grid")
        print(table)
        return headers, data_rows
