"""
This module is the entry point for the lyzer scraper program.
"""
import os
import sys

from api.api_factory import get_version, assign_endpoints
from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.file_parser import create_data_directory, create_text_file, create_json_file
from web.flask_web_app import create_app, host_app

def main():
    """The main function of the lyzer scraper program."""
    program_version = get_version()["version"]
    log_to_console(f"Lyzer {program_version}")
    create_data_directory("logs")
    if not create_text_file("logs/logs.txt"):
        log_to_console("There is an issue with the logs file.", "WARNING")

    create_log("Lyzer Scraper started.")

    if create_data_directory("data"):
        create_log("Data directory created.")

    if create_json_file("data/links.json", []):
        create_log("Links data file created.")

    if create_json_file("data/backlog.json", []):
        create_log("Backlog data file created.")

    if create_json_file("data/season_summaries.json"):
        create_log("Season summary data file created.")

    if create_json_file("data/races.json"):
        create_log("Races data file created.")
        
    if len(sys.argv) > 1 and sys.argv[1] == "--uninstall":
        try:
            log_to_console("Uninstalling Lyzer Scraper.", "WARNING")
            os.remove("data/links.json")
            os.remove("data/backlog.json")
            os.remove("data/season_summaries.json")
            os.remove("data/races.json")
            os.remove("logs/logs.txt")
            os.rmdir("data")
            log_to_console("Lyzer Scraper uninstalled.", "SUCCESS")
        except OSError as error:
            log_to_console("Lyzer Scraper uninstall failed.", "ERROR")
            log_to_console(error, "ERROR")
    else:
        app = create_app()
        assign_endpoints(app)
        log_to_console("Hosting web app.")
        log_to_console("localhost:8080", "LINK")
        log_to_console("Ctrl-C to Shutdown")
        host_app(app)


if __name__ == "__main__":
    main()