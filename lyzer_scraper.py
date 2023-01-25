"""
This module is the entry point for the lyzer scraper program.
"""
import sys

from api.api_factory import get_version, assign_endpoints
from logs.console_logger import log_to_console
from source.installer import install_lyzer_data_files, uninstall_lyzer_data_files
from source.queue_processor import clear_queue
from web.flask_web_app import create_app, host_app

def main():
    """The main function of the lyzer scraper program."""
    program_version = get_version()[0]["version"]
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
    else:
        app = create_app()
        assign_endpoints(app)
        log_to_console("Hosting web app.")
        log_to_console("localhost:8080", "LINK")
        log_to_console("Ctrl-C to Shutdown")
        host_app(app)


if __name__ == "__main__":
    main()
