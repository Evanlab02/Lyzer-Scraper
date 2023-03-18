"""Module will contain the logic to install the data files for the lyzer scraper program."""
import os

from api.api_controller import get_files
from api.backlog_controller import flex_scrape
from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.file_parser import (
    create_data_directory,
    create_text_file,
    create_json_file,
    read_json_file,
    write_json_file
)
from web.web_driver import start_flex_driver, stop_driver

def install_config_file():
    """
    Install config file for project to keep local secrets safe.
    """
    if not os.path.exists("config.json"):
        config = {
            "lyzerWebAddress": input("Enter the Lyzer-Web Address: "),
            "notifAddress": input("Enter the Notif-Web Address: ")
        }
        create_json_file("config.json", config)


def install_lyzer_data_files():
    """Install the data files for the lyzer scraper program."""
    create_data_directory("logs")

    if not create_text_file("logs/logs.txt"):
        log_to_console("There is an issue with the logs file.", "WARNING")

    create_log("Lyzer Scraper started.")
    create_data_directory("data")
    create_json_file("data/links.json", [])
    create_json_file("data/backlog.json", [])
    create_json_file("data/season_summaries.json", {})
    create_json_file("data/races.json", {})
    create_json_file("data/fastest_laps.json", {})
    create_json_file("data/pit_stop_data.json", {})
    create_json_file("data/starting_grids.json", {})
    create_json_file("data/qualifying.json", {})
    create_json_file("data/practice3.json", {})
    create_json_file("data/practice2.json", {})
    create_json_file("data/practice1.json", {})
    create_json_file("data/sprints.json", {})
    create_json_file("data/sprint_grids.json", {})
    create_json_file("data/drivers.json", {})
    create_json_file("data/teams.json", {})
    create_json_file("data/2023.json", [])
    create_json_file("data/incidents.json", {})
    create_json_file("data/requests.json", {})

def uninstall_lyzer_data_files():
    """Uninstall the data files for the lyzer scraper program."""
    try:
        log_to_console("Uninstalling Lyzer Scraper.", "WARNING")
        os.remove("data/links.json")
        os.remove("data/backlog.json")
        os.remove("data/season_summaries.json")
        os.remove("data/races.json")
        os.remove("data/fastest_laps.json")
        os.remove("data/pit_stop_data.json")
        os.remove("data/starting_grids.json")
        os.remove("data/qualifying.json")
        os.remove("data/practice3.json")
        os.remove("data/practice2.json")
        os.remove("data/practice1.json")
        os.remove("data/sprints.json")
        os.remove("data/sprint_grids.json")
        os.remove("data/drivers.json")
        os.remove("data/teams.json")
        os.remove("logs/logs.txt")
        os.rmdir("data")
        log_to_console("Lyzer Scraper uninstalled.", "SUCCESS")
    except OSError as error:
        log_to_console("Lyzer Scraper uninstall failed.", "ERROR")
        log_to_console(error, "ERROR")

def update_season_data(current_year: int):
    """
    This function will update the season data for the lyzer scraper program.

    args:
        current_year: The current year.
    """
    links = read_json_file("data/links.json")
    update_links = read_json_file(f"data/{current_year}.json")
    for link in update_links:
        if link in links:
            log_to_console(f"Removing {link} from links.json.", "WARNING")
            links.remove(link)
    write_json_file("data/links.json", links)

    files = get_files()

    for file in files:
        file_data = read_json_file(file)
        if str(current_year) in file_data.keys():
            log_to_console(f"Removing {current_year} data from {file}.", "WARNING")
            del file_data[str(current_year)]
        write_json_file(file, file_data)

    driver = start_flex_driver()
    for link in update_links:
        try:
            log_to_console("Updating data...", "WARNING")
            flex_scrape(link, driver)
        except AttributeError as exception:
            log_to_console(exception, "ERROR")
            log_to_console(f"Skipping Link {link}.", "WARNING")
    stop_driver(driver)
