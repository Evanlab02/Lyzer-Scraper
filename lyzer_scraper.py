"""
This is module acts as the main entry point for our web scraper program.
"""

# System imports
import sys

from flask import Flask, request
from rich import print as rich_print
from waitress import serve

from src.cli_parser import get_link
from src.installer import Installer
from src.url_scraper import UrlScraper
from src.web_scraper import WebScraper

def start_lyzer_scraper(version: str) -> str:
    rich_print(f"[green]Version: [/green] {version}") # Print version of scraper
    home_directory = install_self()
    return home_directory


def start_web_server(home_directory: str):
    """
    This function will start the web server.
    """
    app = Flask(__name__)

    @app.route("/links", methods=["POST"])
    def links():
        """
        This function will handle the links endpoint.
        """
        content_type = request.headers["Content-Type"]
        if content_type == "application/json":
            links = request.json
            codes = []
            for link in links:
                exit_code = full_scrape(["web-app", "--link", link], home_directory)
                codes.append(exit_code)
            return {"exit_codes": codes}

        return {"error": "Invalid Content-Type"}

    rich_print("Server hosted at http://localhost:8080")
    serve(app, host="0.0.0.0", port=8080)


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


def start_web_scraper() -> WebScraper:
    """
    This function will create the web scraper object.

    Returns:
        WebScraper: Returns the web scraper object.
    """
    scraper = WebScraper() # Instance of the scraper class
    return scraper


def install_self():
    """
    This function will install the program.
    """
    installer = Installer() # Instance of the installer class
    installer.install_data_directory() # Install the data directory

    data_files = [
        "races.json",
        "fastest_laps.json",
        "pit_stop_summary.json",
        "links.json"
    ]

    for data_file in data_files:
        installer.install_data_file(data_file)

    return installer.home_directory


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


if __name__ == "__main__":
    home_dir = start_lyzer_scraper("0.4.0")
    start_web_server(home_dir)
