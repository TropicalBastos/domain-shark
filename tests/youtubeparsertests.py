from selenium import webdriver
import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from src import youtubeparser as youtube

filedir = os.path.dirname(__file__)
phantomPath = os.path.join(filedir, "../bin/phantomjs")
driver = webdriver.PhantomJS(phantomPath)
url = "https://socialblade.com/youtube/top/trending/top-500-channels-30-days/most-subscribed"
driver.get(url)
root = youtube.get_first_row(driver)

class YoutubeParserTestCase(unittest.TestCase):

    def test_getfirstrow(self):
        self.assertIsInstance(root.text, basestring, 
        "Socialblade scraper is picking up the wrong information")

    def test_processnextchannel(self):
        next_el = youtube.process_next_channel_by_div(root)
        self.assertIsInstance(next_el.text, basestring, 
        "Youtube parser does not get the next element properly")

    def test_getchannels(self):
        max = 3
        channels = youtube.get_channels(root, max)
        self.assertEquals(len(channels), max,
        "Youtube parser not getting channels")



if __name__ == "__main__":
    unittest.main()