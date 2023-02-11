"""
This module is responsible for processing the queue and clearing the queue.
"""

from api.backlog_controller import scrape
from logs.console_logger import log_to_console
from logs.file_logger import create_log
from source.file_parser import read_json_file, write_json_file

def clear_queue():
    """This will clear the queue."""
    create_log("Clearing queue.")
    queue = read_json_file("data/backlog.json")
    new_queue = []
    for array in queue:
        for item in array:
            try:
                scrape(item)
                new_queue.append(item)
            except AttributeError as exception:
                log_to_console(exception, "ERROR")
                log_to_console(f"Skipping Link {item}.", "WARNING")

    links = read_json_file("data/links.json")
    final_queue = new_queue.copy()
    for item in new_queue:
        if item in links:
            final_queue.remove(item)

    data = []
    data.append(final_queue)
    write_json_file("data/backlog.json", data)
