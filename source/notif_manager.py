"""
This will manage the notifcation system for any outages or errors that occur
in the scraper.
"""
from time import sleep

import requests

from logs.console_logger import log_to_console
from source.file_parser import read_json_file

def start_notif_manager():
    """
    Start the notification manager.
    """
    config = read_json_file("config.json")
    lyzer_web_address = config["lyzerWebAddress"]
    notif_address = config["notifAddress"]
    log_to_console("Starting Notification Manager.")
    while True:
        try:
            response = requests.get(lyzer_web_address, timeout=5)
            if response.status_code == 200:
                log_to_console("Lyzer Web is online.")
                requests.post(notif_address,
                            data="Lyzer Web is online and responding.",
                            headers={
                                "Title": "Lyzer Web is online!",
                                "Priority": "1",
                                "Tags": "info"
                                },
                                timeout=5)
            else:
                log_to_console("Lyzer Web is offline.", "ERROR")
                requests.post(notif_address,
                            data="Lyzer Web is offline!",
                            headers={
                                "Title": "Lyzer Web is offline!",
                                "Priority": "urgent",
                                "Tags": "warning"
                            },
                            timeout=5)
        except requests.exceptions.ConnectionError:
            log_to_console("Lyzer Web is offline.", "ERROR")
            requests.post(notif_address,
                        data="Lyzer Web is offline!",
                        headers={
                            "Title": "Lyzer Web is offline!",
                            "Priority": "urgent",
                            "Tags": "warning"
                        },
                        timeout=5)
        sleep(1800)
