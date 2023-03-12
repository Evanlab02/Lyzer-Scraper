"""
This module is the entry point for the lyzer scraper program.
"""
import sys

from datetime import datetime

from api.api_factory import get_version, assign_endpoints
from logs.console_logger import log_to_console
from source.installer import (
    install_lyzer_data_files,
    uninstall_lyzer_data_files,
    update_season_data
)
from source.queue_processor import clear_queue
from source.site_scraper import get_all_links_for_urls
from web.flask_web_app import create_app, host_app

def main():
    """The main function of the lyzer scraper program."""
    program_version = get_version()[0]["data"]
    log_to_console(f"Lyzer {program_version}")
    install_lyzer_data_files()

    if len(sys.argv) > 1 and sys.argv[1] == "--uninstall":
        try:
            uninstall_lyzer_data_files()
        except OSError as error:
            log_to_console("Lyzer Scraper uninstall failed.", "ERROR")
            log_to_console(error, "ERROR")
    elif len(sys.argv) > 1 and sys.argv[1] == "--clear-backlog":
        log_to_console("Clearing backlog.", "WARNING")
        clear_queue()
    elif len(sys.argv) == 3 and sys.argv[1] == "--port":
        app = create_app()
        assign_endpoints(app)
        log_to_console("Hosting web app.")
        log_to_console(f"localhost:{sys.argv[2]}", "LINK")
        log_to_console("Ctrl-C to Shutdown")
        host_app(app, int(sys.argv[2]))
    elif len(sys.argv) == 2 and sys.argv[1] == "--update":
        log_to_console("Updating Lyzer Scraper.", "WARNING")
        log_to_console("This may take a while.", "WARNING")
        log_to_console("Please wait...", "WARNING")
        current_year = datetime.now().year
        update_season_data(current_year)
    elif len(sys.argv) >= 3 and sys.argv[1] == "--generate":
        urls = []
        for url in sys.argv[2:]:
            log_to_console(f"Getting links for {url}.")
            urls.append(url)
        log_to_console(get_all_links_for_urls(urls))
    else:
        app = create_app()
        assign_endpoints(app)
        log_to_console("Hosting web app.")
        log_to_console("localhost:8000", "LINK")
        log_to_console("Ctrl-C to Shutdown")
        host_app(app)


if __name__ == "__main__":
    main()
