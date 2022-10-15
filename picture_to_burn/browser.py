from contextlib import contextmanager
from typing import Iterator

from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def _build_options() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs: dict = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options


@contextmanager
def create_driver() -> Iterator[webdriver.Chrome]:
    """Build a driver that'll work on this docker image"""
    options = _build_options()
    try:
        driver = webdriver.Chrome(options=options)
        yield driver
    finally:
        driver.close()
