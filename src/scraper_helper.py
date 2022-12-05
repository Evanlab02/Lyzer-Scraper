"""
This module will be used to store functions to help with scraping.
"""
from rich import print as rich_print

from src.cli_parser import get_link
from src.url_scraper import UrlScraper
from src.web_scraper import WebScraper

def start_web_scraper() -> WebScraper:
    """
    This function will create the web scraper object.

    Returns:
        WebScraper: Returns the web scraper object.
    """
    scraper = WebScraper() # Instance of the scraper class
    return scraper

def full_scrape(args: list, home_directory: str):
    """
    This is the main function for our web scraper program.

    Args:
        args (list): List of arguments passed to the program.

    Returns:
        int: Returns 0 if the program runs successfully.
    """

    try:
        exit_code = 0
        link = get_link(args) # Get the link passed to the scraper
        if link == "Unexpected Error 2":
            exit_code = 2
        elif link == "No link passed.":
            exit_code = 3
        elif link == "":
            rich_print("[red]No link passed.[/red]")
            exit_code = 4

        if exit_code == 0:
            rich_print(f"[cyan]Link ->[/cyan] {link}")
            url_data = scrape_link(link) # Scrape the link passed to the scraper

            if url_data[0] == 5:
                exit_code = 5
            elif url_data[0] == 6:
                exit_code = 6
            else:
                try:
                    web_scraper = start_web_scraper()
                    headers, data_rows = web_scraper.scrape_site(url_data, link)
                    bundled_data = {
                        "headers": headers,
                        "data_rows": data_rows,
                        "url_data": url_data,
                        "home_directory": home_directory,
                        "link": link
                    }
                    web_scraper.compile_and_save_data(bundled_data)
                except RuntimeError as error:
                    rich_print(f"[red]RuntimeError: {error}[/red]")
                    exit_code = 7
        return exit_code
    except KeyboardInterrupt:
        return 1


def scrape_link(link: str) -> tuple:
    """
    This function will scrape the link passed to the program.

    Args:
        link (str): The link to scrape.

    Returns:
        tuple: Returns a tuple containing the scraped data and the scraped link.
    """
    try:
        scraper = UrlScraper(link) # Instance of the scraper class
        url_elements = scraper.start()
        url_year = scraper.get_year_from_url()
        url_data = scraper.generate_url_data(url_elements, url_year)
        return url_data
    except IndexError:
        rich_print("[red]Invalid Link.[/red]")
        return (5, 5, 5)
    except ValueError:
        return (6, 6, 6)
