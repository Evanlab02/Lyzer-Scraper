"""
Contains all the logic for the web driver.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def start_driver(url_data: dict):
    """
    This will start the web driver.
    Args:
        link (str): The link to scrape.
    Returns:
        webdriver: The web driver.
        BeautifulSoup: The BeautifulSoup object.
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    options.add_argument("--window-size=1400x1080")
    options.add_argument("--mute-audio")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.get(url_data["url"])

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    return driver, soup

def stop_driver(driver):
    """
    This will stop the web driver.
    Args:
        driver (webdriver): The web driver.
    """
    driver.quit()
