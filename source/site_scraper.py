"""
This module will contain the logic to parse the site and return the data.
"""
from bs4 import BeautifulSoup
from logs.file_logger import create_log
from source.file_parser import read_json_file, write_json_file
from source.url_parser import parse_url
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
    selected_items = soup.findAll("a",
    {"class": "resultsarchive-filter-item-link FilterTrigger selected"}
    )
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
        elif index == 2 and category == "DRIVERS":
            driver = value.find("span", {"class": "clip"}).text
            site_data["driver"] = driver
            create_log(f"Selected driver: {driver}")
        elif index == 2 and category == "Teams":
            team = value.find("span", {"class": "clip"}).text
            site_data["team"] = team
            create_log(f"Selected team: {team}")
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

def get_all_links_for_urls(urls: list[str]):
    """
    This will get all links related to a array of urls.

    Args:
        urls (list[str]): Urls to give context to the driver.

    Returns:
        list: The links for the years.
    """
    links = []
    for url in urls:
        get_all_links_for_url(links, url)
    return filter_links(links)
        

def get_all_links_for_url(links: list[str], url: str):
    """
    This will get all links related to a specific url.

    Args:
        links (list[str]): The urls gathered so far.
        url: The url to check for relation.
    """

    url_data = parse_url(url)
    driver, soup = start_driver(url_data)
    create_log("Started Driver.")
    
    selected_items = soup.findAll("a",
        {"class": "resultsarchive-filter-item-link FilterTrigger"}
    )

    for value in selected_items:
        links.append(value.get("href"))

    selected_items = soup.findAll("a",
        {"class": "side-nav-item-link ArchiveLink"}
    )

    for value in selected_items:
        links.append(value.get("href"))

    stop_driver(driver)
    create_log("Stopped Driver.")

def filter_links(links: list[str]):
    """
    This will filter out any duplicates and links that have already
    been scraped by the service.
    """
    filtered_links = []
    data_links = read_json_file("data/links.json")
    for link in links:
        link = f"https://www.formula1.com{link}"
        if not link in data_links:
            filtered_links.append(link)
    filtered_links = list(set(filtered_links))
    write_json_file("temp.json", filtered_links)
    return filtered_links
