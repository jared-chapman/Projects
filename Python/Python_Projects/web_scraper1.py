#This web scrapers gathers the links to articles on google news
#From tutorial

import urllib.request                           #Works with URLs
from bs4 import BeautifulSoup                   #parses HTML

class Scraper:
    def __init__(self, site):                   #takes website to scrape from as a parameter
        self.site = site

    def scrape(self):                           #will scrapte data
        r = urllib.request.urlopen(self.site)   #urlopen() makes a request to a website and returns a Response object that contains it's HTML and additional data
        html = r.read()                         #returns the Response object's HTML. This puts all HTML from the website into the variable html
        parser = "html.parser"                  #these two lines do all the hard work as far as parsing the HTML
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):            #find_all returns an iterable containg the tag objects it found. This loops through all tag objects
            url = tag.get("href")               #each tag has many variables, but this assigns the value of the variable "href" to url
            if url is None:                     #if a tag doesn't contain an href variable
                continue                        #basically do nothing
            if "html" in url:                   #but if a tag does have an href variable
                print("\n" + url)               #print the url



news = "https://news.google.com/"
Scraper(news).scrape()
