from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import sys
import domainchecker as domain
import youtubeparser as youtube
import instaparser as instagram
import wordparser


def write_list_to_file(the_list, path = os.path.join(os.path.dirname(__file__), "../log/domains.log")):
    print("Writing results to " + path)
    with open(path, "w") as fp:
        for domain in the_list:
            fp.write(domain.encode('utf-8') + "\n")

def check_limit(limit):
    if(limit > 500):
        print("500 is the maximum limit, changing limit to 500")
        return 500
    return limit

def order_by_len(domain_list):
    domain_list.sort(key = len)

if __name__ == "__main__":
    driver = None
    limit = None
    platform = "youtube"

    if(len(sys.argv) < 1):
        print("A max channel limit must be supplied")
        exit()

    if(len(sys.argv) >= 3):
        if(sys.argv[2] == "instagram"):
            platform = "instagram"
        if(sys.argv[2] == "dictionary"):
            platform = "dict"

    try:
        limit = check_limit(int(sys.argv[1]))
    except Exception:
        print("Wrong format for max channel limit, must supply an integer")
        exit()

    if(platform == "dict"):
        prefix_bool = False
        suffix_bool = False
        custom_wordlist_bool = False
        prefix = ""
        suffix = ""
        custom_wordlist = ""

        #check and assign for the --prefix/--suffix arg
        for arg in sys.argv:
            if(prefix_bool):
                prefix = arg
                prefix_bool = False
            if(suffix_bool):
                suffix = arg
                suffix_bool = False
            if(custom_wordlist_bool):
                custom_wordlist = os.getcwd() + "/" + arg
                custom_wordlist_bool = False
            if(arg == "--prefix"):
                prefix_bool = True
                continue
            if(arg == "--suffix"):
                suffix_bool = True
                continue
            if(arg == "--input"):
                custom_wordlist_bool = True
                continue

        lines = wordparser.parse_words(prefix, suffix, custom_wordlist)
        available_domains = domain.domains_available(lines)
        order_by_len(available_domains)
        write_list_to_file(available_domains)
        exit()


    try:
        filedir = os.path.dirname(__file__)
        phantomPath = os.path.join(filedir, "../bin/phantomjs")
        driver = webdriver.PhantomJS(phantomPath)
        print("Web driver initialised")
    except Exception:
        print("Oops, failed to initialise web driver")
        exit()

    accounts = []

    if(platform == "youtube"):

        driver.get(youtube.url)

        #get the very first row of channels
        firstRow = youtube.get_first_row(driver)

        #get each subsequent row with the channels
        accounts = youtube.get_channels(firstRow, limit)
    
    else:

        driver.get(instagram.url)
        accounts = instagram.get_accounts(driver, limit)

    #grab list of available domains and log them
    available_domains = domain.domains_available(accounts)
    order_by_len(available_domains)
    write_list_to_file(available_domains)

    #finally release the resource
    driver.close()