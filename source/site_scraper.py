"""
This module will contain the logic to parse the site and return the data.
"""
from bs4 import BeautifulSoup

from logs.file_logger import create_log
from web.web_driver import start_driver, stop_driver

def parse_site(site_data: dict):
    """
    Parse the site and return the data.
    
    Args:
        url (str): The url to parse.
    """
    driver, soup = start_driver(site_data)
    create_log("Started Driver.")
    get_selected_items(site_data, soup)
    get_table_head_and_body(site_data, soup)
    get_headers(site_data)
    get_rows(site_data)
    stop_driver(driver)
    create_log("Stopped Driver.")


def get_selected_items(site_data: dict, soup: BeautifulSoup):
    """
    Get the selected year from the site.
    
    Args:
        site_data (dict): The site data.
    """
    selected_items = soup.findAll("a", {"class": "resultsarchive-filter-item-link FilterTrigger selected"})
    for index, value in enumerate(selected_items):
        if index == 0:
            year = value.find("span", {"class": "clip"}).text
            site_data["year"] = year
            create_log(f"Selected year: {year}")
        elif index == 1:
            category = value.find("span", {"class": "clip"}).text
            site_data["category"] = category
            create_log(f"Selected category: {category}")
        elif index == 2 and category == "Races":
            location = value.find("span", {"class": "clip"}).text
            site_data["location"] = location
            create_log(f"Selected location: {location}")
    return site_data


def get_table_head_and_body(site_data: dict, soup: BeautifulSoup):
        """
        This will get the table head and body.
        Args:
            site_data (dict): The site data.
            soup (BeautifulSoup): The BeautifulSoup object.
        """
        table_headers = []
        table_rows = []
        for table in soup.findAll('table', attrs={'class':'resultsarchive-table'}):
            table_head = table.find('thead')
            table_headers = table_head.find_all('th')
            table_body = table.find('tbody')
            table_rows = table_body.find_all('tr')
        site_data["table headers"] = table_headers
        site_data["table rows"] = table_rows


def get_headers(site_data: dict):
    """
    This will get the headers
    Args:
        site_data (dict): The site data.
    """
    table_headers = site_data["table headers"]
    headers = []
    for header in table_headers:
        if header.text.strip() != "":
            headers.append(header.text)
    site_data["headers"] = headers
    create_log(f"Headers: {headers}")


def get_rows(site_data: dict):
        """
        This will get the rows.
        Args:
            table_rows (list): The table rows.
        Returns:
            list: The rows.
        """
        data_array = []
        table_rows = site_data["table rows"]
        for row in table_rows:
            row_data = []
            table_data = row.find_all('td')
            row_data = process_data_row(table_data)
            data_array.append(row_data)

        site_data["rows"] = data_array
        del site_data["table headers"]
        del site_data["table rows"]
        create_log(f"Rows: {data_array}")


def process_data_row(data_rows):
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
                name = data_span[0].text
                surname = data_span[1].text
                data_entry = f"{name} {surname}"
            else:
                data_entry = data_entry.text.strip()
                data_entry = data_entry.replace("\n", "")

            if data_entry != "":
                row_data.append(data_entry)

        return row_data
