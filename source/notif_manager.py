"""
This will manage the notifcation system for any outages or errors that occur
in the scraper.
"""
from time import sleep

import requests

from logs.console_logger import log_to_console

def start_notif_manager():
    """
    Start the notification manager.
    """
    log_to_console("Starting Notification Manager.")
    while True:
        try:
            response = requests.get("http://localhost:80/version", timeout=5)
            if response.status_code == 200:
                log_to_console("Lyzer Web is online.")
                requests.post("https://ntfy.sh/lyzer-tech",
                            data="Lyzer Web is online and responding.",
                            headers={
                                "Title": "Lyzer Web is online!",
                                "Priority": "1",
                                "Tags": "info"
                                },
                                timeout=5)
            else:
                log_to_console("Lyzer Web is offline.", "ERROR")
                requests.post("https://ntfy.sh/lyzer-tech",
                            data="Lyzer Web is offline!",
                            headers={
                                "Title": "Lyzer Web is offline!",
                                "Priority": "urgent",
                                "Tags": "warning"
                            },
                            timeout=5)
        except requests.exceptions.ConnectionError:
            log_to_console("Lyzer Web is offline.", "ERROR")
            requests.post("https://ntfy.sh/lyzer-tech",
                        data="Lyzer Web is offline!",
                        headers={
                            "Title": "Lyzer Web is offline!",
                            "Priority": "urgent",
                            "Tags": "warning"
                        },
                        timeout=5)
        sleep(1800)
