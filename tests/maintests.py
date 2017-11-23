import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from src import main

class MainTestCase(unittest.TestCase):

    def test_checklimit(self):
        limit = main.check_limit(5000)
        self.assertEquals(limit, 500, 
        "Limits over 500 should default to 500")
        limit = main.check_limit(250)
        self.assertEquals(limit, 250, 
        "Limit checker in main.py not working as expected")

    def test_orderbylen(self):
        arr = ["testtest", "test", "testtesttest"]
        main.order_by_len(arr)
        expected = ["test", "testtest", "testtesttest"]
        self.assertEquals(arr, expected, 
        "Order by length function not ordering lists by length of string")


if __name__ == "__main__":
    unittest.main()