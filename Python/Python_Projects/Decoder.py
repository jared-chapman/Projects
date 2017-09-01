"""
Simple program that decodes a users message by choosing random characters.
An exercise in loops
Interesting that number of tries needed caps out sooner than you might think
"""

import random

symbols=['a','b','c','d','e','f','g','h','i','j','k','l','m',
         'n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M',
         'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
         ' ',".","?","!","@",
         0,1,2,3,4,5,6,7,8,9]

def randomChar():
    return str(symbols[random.randint(0,66)])


def decode():
#---- Initial ----------------------
    message = input("Enter a word or phrase: ")
    messageLength = len(message)
    scramble = ""
    numberOfTries=0
    for i in range(messageLength):
        scramble += randomChar()
    print(scramble)
#---- Main Loop --------------------
    while message != scramble:
        tempScramble = ""
        numberOfTries += 1
        for i in range(messageLength):

            if scramble[i] == message[i]:
                tempScramble += message[i]
            else:
                tempScramble += randomChar()
        scramble = tempScramble
        print(scramble + ":   " + str(numberOfTries))





decode()
