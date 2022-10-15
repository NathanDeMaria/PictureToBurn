from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .browser import create_driver


def find_mp4(tweet_url: str) -> str:
    r"""
    Scrape the .mp4 URL out of a tweet link.

    :param tweet_url: URL for a tweet with a video.
    :return: URL of the mp4 itself.
    """
    with create_driver() as driver:
        driver.get(tweet_url)
        target_element = (By.TAG_NAME, "video")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(target_element))
        video = driver.find_element(*target_element)
        return video.get_attribute("src")
