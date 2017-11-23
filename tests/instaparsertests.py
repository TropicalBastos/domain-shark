from selenium import webdriver
import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from src import instaparser as insta

filedir = os.path.dirname(__file__)
phantomPath = os.path.join(filedir, "../bin/phantomjs")
driver = webdriver.PhantomJS(phantomPath)
url = "https://socialblade.com/instagram/top/500/followers"
driver.get(url)

class InstagramParserTestCase(unittest.TestCase):

    def test_getallaccounts(self):
        elements = insta.get_all_accounts(driver)
        self.assertIsInstance(elements[0].text, basestring, 
        "Insta parser not getting accounts")

    def test_getaccounts(self):
        max = 3
        accounts = insta.get_accounts(driver, max)
        self.assertEquals(len(accounts), max, 
        "Insta parser not pulling through any channel data")


if __name__ == "__main__":
    unittest.main()