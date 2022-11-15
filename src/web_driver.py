"""
Contains all the logic for the web driver.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def start_driver(link: str):
    """
    This will start the web driver.

    Args:
        link (str): The link to scrape.

    Returns:
        webdriver: The web driver.
        BeautifulSoup: The BeautifulSoup object.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.get(link)

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    return driver, soup

def stop_driver(driver):
    """
    Stops the web driver.

    Args:
        driver (webdriver): The web driver to stop.
    """
    driver.quit()
