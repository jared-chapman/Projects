"""
This web scraper scrapes the first page of reddit and returns the number of
titles that contain any of the "bad words" inputed by the users. Note this
doesn't count the number of times a word appears, but how many titles contain
at least one of the words
"""

import urllib.request
from bs4 import BeautifulSoup
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
}

count = 0
badWords = []

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all(class_ = "outbound"):
            global count
            url = tag.getText()
            if url is None:
                continue
            for i in range(len(badWords)):
                if badWords[i].lower() in url.lower():
                    count += 1
                    break
            print(url)
        print(count)



def scrapeReddit():
    global badWords
    done = False
    while done == False:
        toAdd = input("Enter a word you'd like to check. Press Enter to Continue: ")
        if (toAdd != ""):
            badWords.append(toAdd)
        else:
            done = True
    print(badWords)
    site = "https://reddit.com/r/all"
    Scraper(site).scrape()



scrapeReddit()
