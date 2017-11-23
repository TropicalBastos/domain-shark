import domainchecker as domain
import os

default_wordlist = os.path.join(os.path.dirname(__file__), "../wordlists/common.txt")

def parse_words(prefix = "", suffix = "", input = "", custom_list = None):
    try:
        print("Getting lines from wordlist...")
        lines = []
        wordlist = default_wordlist

        if(len(input) > 0):
            wordlist = input
        
        if(custom_list != None and isinstance(custom_list, list)):
            lines = custom_list
        else:
            with open(wordlist) as f:
                lines = f.read().splitlines()
        
        if(len(prefix) > 0):
            print("Prefixing '" + prefix + "' onto queued domains")
            prefixed_lines = []
            for line in lines:
                prefixed_lines.append(prefix + line)
            lines = prefixed_lines

        if(len(suffix) > 0):
            print("Suffixing '" + suffix + "' onto queued domains")
            suffixed_lines = []
            for line in lines:
                suffixed_lines.append(line + suffix)
            lines =suffixed_lines

        return lines
    except Exception, e:
        print(str(e))
        exit()