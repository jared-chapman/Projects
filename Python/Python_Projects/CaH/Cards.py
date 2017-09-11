"""
Using the other text files for data, return a random black card, with random
white cards either in the blanks, or after the question mark
"""


import re
import random

class cards(object):
    blackCards = list()
    whiteCards = list()


    def __init__(self):
        # This runs when class is instantiated
        self.whiteCards = self.fixWhiteCards()
        self.blackCards = self.fixBlackCards()


    def fixWhiteCards(self):
        whiteCards          = open('wcards.txt', 'r')                           #Get full text from file
        whiteCardsFullText  = whiteCards.read()                                  #""
        whiteCardsList      = whiteCardsFullText.split(">")                     #Turns full text into list seperated by >

        del whiteCardsList[0]                                                   #Removes garbage first item
        for i in range(len(whiteCardsList)):                                    #Get rid of <
            whiteCardsList[i] = whiteCardsList[i][:-2]
        return whiteCardsList

    def fixBlackCards(self):
        blackCards0         = open('bcards.txt', 'r')                           #Get full text
        blackCards1         = open('bcards1.txt', 'r')
        blackCards2         = open('bcards2.txt', 'r')
        blackCardsFullText  = blackCards0.read() + blackCards1.read() + blackCards2.read()
        blackCardsList      = blackCardsFullText.split(">")                     #Turns full text into list seperated by >

        del blackCardsList[0]                                                   #Removes garbage first item
        for i in range(len(blackCardsList)):                                    #Formatting
            blackCardsList[i] = blackCardsList[i][:-1]
        return blackCardsList

    def randomPhrase(self):
        #Delare Variables
        phrase          = ""
        blackCard       = self.blackCards[0]
        insertPosition1 = len(blackCard)
        insertPosition2 = len(blackCard)
        whiteCard1      = ""
        whiteCard2      = ""

        #Get Random blackCard
        randomB = random.randint(1,len(self.blackCards)-1)
        #print(randomB)                                                         #Debugging
        blackCard = self.blackCards[randomB]                                    #Gets a random black card
        #print(blackCard)                                                       #Debugging

        #Get Random whiteCard1
        randomW1 = random.randint(1,len(self.whiteCards)-1)
        #print(randomW1)                                                        #Debugging
        whiteCard1 = self.whiteCards[randomW1]                                  #Get a random white card
        whiteCard1 = "-" + whiteCard1 + "-"                                     #Format with hyphens
        #print(whiteCard1)

        #Set the phrase
        if not "_" in blackCard:                                                #If Q - A and not fill in the blank...
            phrase = blackCard + " " + whiteCard1 + "."                         #Just add whiteCard to end of blackCard
        else:                                                                   #But if it has at least one blank...
            insertPosition1 = blackCard.index("_")                              #Return the position of the blank
            blackCard = blackCard[:insertPosition1] + blackCard[insertPosition1+10:] #Remove Blanks
            #print(blackCard)                                                   #Debugging
            insertPosition2 = len(blackCard)                                    #This is so if there is no second blank, a "" will be added at the end of phrase
            if "_" in blackCard:                                                #Hopefuly keeps the weird bug from happening
                whiteCard2 = whiteCard1                                         #Sets them equal so we can loop
                while whiteCard2 == whiteCard1:                                 #While they're the same (Which they will be at least once)
                    whiteCard2 = self.whiteCards[random.randint(1,len(self.whiteCards)-1)]    #Make sure whiteCard2 is random
                whiteCard2 = "-" + whiteCard2 + "-"                             #Format with Hyphens
                insertPosition2 = blackCard.index("_")                          #Return the position of the blank
                blackCard = blackCard[:insertPosition2] + blackCard[insertPosition2+10:]    #Remove Blanks
                #print(blackCard)                                               #Debugging
                #print(insertPosition1)                                         #Debugging
                #print(insertPosition2)                                         #Debugging
        #Build phrase
        phrase = blackCard[:insertPosition1] +\
                 whiteCard1 +\
                 blackCard[insertPosition1:insertPosition2] +\
                 whiteCard2 +\
                 blackCard[insertPosition2:]
        return phrase


    def userLoop(self):
        print(self.randomPhrase())
        userInput = input("Press Enter for another. Q to quit ")
        while userInput.lower() != "q":
            print(self.randomPhrase())
            userInput = input("Press Enter for another. Q to quit ")


a = cards()
a.userLoop()
