import requests
import sys
import urlparse
import re

turl = sys.argv[1]

def check_url(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

def find_subd(url):
    with open("./sub_file.txt",'r') as word_file:
        for fline in word_file:
            line = fline.strip() #to strip white space characters
            test_url = line + "." + turl
            if check_url(test_url):
                print("Found subdomain: " + test_url)
            else:
                print("Error check url")


def find_hidden_subs(url):
    resp = check_url(url)
    hlinks = re.findall('(?:href=")(.*?"', resp.content)

    for link in hlinks:
        lnk = urlparse.urljoin(turl,link)

        if turl in link:
            print(lnk) #to make sure the target url is in that current link
