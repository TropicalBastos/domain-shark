from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = "https://socialblade.com/instagram/top/500/followers"

def get_all_accounts(driver):
    return driver.find_elements_by_css_selector(".table-cell a")

def get_accounts(driver, max = 500):
    elements = get_all_accounts(driver)
    accounts = []
    print("Getting instagram accounts...")
    for i in range(max):
        accounts.append(elements[i].text)
    return accounts