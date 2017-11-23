import whois
import re
from alphabet_detector import AlphabetDetector

keywords = ["vevo", ":", "...", u"\u2026", "(", ")", "?", "'", "#", "!"]
suffixes = [".co.uk", ".com"]
regex = r'^[^a-z0-9]+$'
max_length = 25
ad = AlphabetDetector()

def format_domain(domain, suffix):
    suffix = suffix.lower()
    domain = domain.replace(" ", "").lower()
    invalid = False

    #replace all keywords which are unwanted in our domain
    for word in keywords:
        domain = domain.replace(word, "")

    if(len(domain) > max_length):
        return False

    if(not ad.is_latin(domain)):
        return False

    for s in suffixes:
        if s in domain:
            invalid = True

    if(invalid):
        return False

    #make it into a more valuable sought after domain
    domain = re.sub(regex, "", domain)

    return domain + suffix

#returns a list of available domains
def domains_available(wordlist):
    available = []
    for word in wordlist:
        if(check_domain(word)):
            available.append(format_domain(word, ".com"))
    return available

def check_domain(domain):
    temp_domain = domain
    domain = format_domain(domain, ".com")
    if(not isinstance(domain, basestring)):
        print("Domain for " + temp_domain + " not valid, skipping...")
        return
    print("Checking domain: " + domain)
    try:
        results = whois.whois(domain)
        if(results != None):
            print(domain + " not available...")
            return False
    except whois.parser.PywhoisError:
        print(domain + " AVAILABLE!")
        return True
        