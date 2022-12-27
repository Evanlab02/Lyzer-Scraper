"""Module will contain the logic to install the data files for the lyzer scraper program."""
import os

from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.file_parser import create_data_directory, create_text_file, create_json_file

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
