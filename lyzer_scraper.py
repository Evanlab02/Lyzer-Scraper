"""
This is module acts as the main entry point for our web scraper program.

File: lyzer_scraper.py
"""

# System imports
from rich import print as rich_print
from waitress import serve

from src.installer import Installer
from src.web_app_factory import create_web_app

def start_lyzer_scraper(version: str) -> str:
    """
    This function will start the lyzer scraper program.

    Args:
        version (str): The version of the program.

    Returns:
        str: The home directory of the program.
    """
    rich_print(f"[green]Version: [/green] {version}") # Print version of scraper
    home_directory = install_self()
    return home_directory


def start_web_server(home_directory: str):
    """
    This function will start the web server.
    """
    app = create_web_app(home_directory)
    rich_print("Server hosted at http://localhost:8080")
    serve(app, host="0.0.0.0", port=8080)


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
        "links.json",
        "starting_grid.json"
    ]

    for data_file in data_files:
        installer.install_data_file(data_file)

    return installer.home_directory


if __name__ == "__main__":
    home_dir = start_lyzer_scraper("0.5.0")
    start_web_server(home_dir)
