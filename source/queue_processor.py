"""
This module is responsible for processing the queue and clearing the queue.
"""

from api.api_factory import scrape
from logs.file_logger import create_log
from source.file_parser import read_json_file, write_json_file

def clear_queue():
    """This will clear the queue."""
    create_log("Clearing queue.")
    queue = read_json_file("data/backlog.json")
    new_queue = []
    for array in queue:
        for item in array:
            scrape(item)
            new_queue.append(item)

    links = read_json_file("data/links.json")
    final_queue = new_queue.copy()
    for item in new_queue:
        if item in links:
            final_queue.remove(item)

    final_queue = [].append(final_queue)
    write_json_file("data/backlog.json", final_queue)
