from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def get_percentage_of_currently_broken_machines(url:str) -> str:
    browser = webdriver.Firefox()  
    browser.get(url)
    sleep(2)
    stats = browser.find_element(
    By.CSS_SELECTOR,
    'div.stats-list'
    )
    percentage_of_broken:str = stats.find_element(
        By.CSS_SELECTOR,
        'p.stats-row-broken').text
    return percentage_of_broken


