import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from src import wordparser

class WordParserTestCase(unittest.TestCase):

    def test_parsewords(self):
        prefix = "test"
        suffix = "123"
        wordlist = ["apple", "boat", "sky"]
        lines = wordparser.parse_words(prefix, suffix, "", wordlist)
        expected = ["testapple123", "testboat123", "testsky123"]
        self.assertEquals(lines, expected, 
        "Word parser does not parse words as expected")


if __name__ == "__main__":
    unittest.main()