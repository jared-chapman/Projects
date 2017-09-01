"""
This web scraper asks the user for a list of words to check for, then
a website, then the number of times they can tolerate those words. It checks
the website and counts how many times those words appear. If they appear more
than the user can stand, it instead opens a nicer site. If the words are at a
tolerable level, it opens the user's site.
"""



import urllib.request
from bs4 import BeautifulSoup
from collections import Counter
import webbrowser

# This (hopefully) sets the user-agent to something that looks less like a bot
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
}

# These are the variables that are set in userInput() and used in the scrape
# These can probably be changed to be passed as parameters
badWords = []           # List of bad words
count = 0               # Number of bad words
cutoff = 0              # Number of bad words the user can tolerate
site = ""               # Website name

class Scraper:
    # Sets up scraper. This is needed. Not positive how it works
    def __init__(self, site):
        self.site = site
    # Scrape
    def scrape(self):
        # Global variables are declared here so they can be accesses locally
        global count
        global badWords
        global cutoff
        r = urllib.request.urlopen(self.site)                                   # makes a request to the site and returns its HTML and other data
        html = r.read()                                                         # returns the above response object's html
        parser = "html.parser"                                                  # These two lines do the hard work of reading and parsing the HTML
        sp = BeautifulSoup(html, parser)
        pageText = sp.getText().split(" ")                                      # Returns a list of the text of the page, split by spaces

        # Loop through above list amd then through the list of bad words to see if they match
        for word in pageText:
            for i in range(len(badWords)):
                if badWords[i].lower() == word.lower():
                    count += 1
        print("There were " + str(count) + " bad words on that site")

        #Handle whether the count was higher or lower than the cutoff
        if count <= cutoff:
            print("Opening your site")
            webbrowser.open(site)
        else:
            print("Opening something a little happier. :)")
            webbrowser.open("HTTPS://reddit.com/r/aww+happy")


def userInput():
    global badWords
    global site
    global cutoff
    done = False
    while done == False:
        toAdd = input("Enter a word you don't want to see right now. Press Enter to Continue: ")
        if (toAdd != ""):
            badWords.append(toAdd)
        else:
            done = True
    site = input("Enter a website you'd like to check: ")
    cutoff = int(input("What is the most you can tolerate?")) #Need to validate this
    print(badWords)
    Scraper(site).scrape()


userInput()
