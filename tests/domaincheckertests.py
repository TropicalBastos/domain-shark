import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from src import domainchecker

class DomainCheckerTestCase(unittest.TestCase):

    def test_formatter(self):
        domain = "test"
        suffix = ".com"
        result = domainchecker.format_domain(domain, suffix)
        self.assertEqual(result, "test.com", 
        "Domain formatter does not return a valid result, should be a domain (string)")

    def test_checker(self):
        #never going to be a taken domain
        domain = "ceoyubciqtiecgv"
        available = domainchecker.check_domain(domain)
        self.assertTrue(available, 
        "Domain checker has failed in recognising available domains")

    def test_available(self):
        wordlist = ["bcuyidcbdc", "idbcugdckbhjd", "idbcuidytc"]
        result = domainchecker.domains_available(wordlist)
        self.assertIsInstance(result, list, 
        "Available domains should return a list")


if __name__ == "__main__":
    unittest.main()