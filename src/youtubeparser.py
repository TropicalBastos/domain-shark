from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = "https://socialblade.com/youtube/top/trending/top-500-channels-30-days/most-subscribed"

def process_next_channel_by_div(prev):
    return prev.find_element_by_xpath("following-sibling::div")

def get_first_row(driver):
    return driver.find_element_by_css_selector(".cas-wide-container + div + div + div")

def get_channels(root, max = 500):
    channels = []
    current = root
    print("Getting channels...")
    for i in range(max):
        try:
            current = process_next_channel_by_div(current)
            channelCell = current.find_element_by_css_selector("div:nth-child(3)")
            channel = channelCell.find_element_by_tag_name("a").text
            #print(channel)
            channels.append(channel)
        except NoSuchElementException:
            print("NoSuchElementException! breaking loop")
            break
    return channels