"""
Used for simulating Dice rolls and checking them against a difficulty
"""

import random


#Rolls a D(x) die
def D(number, die):
    result = 0
    for i in range(number):
        result += random.randint(1,die)
    return result

#Pass in a list[number of dice to be rolled, size of dice and get their roll
def modify(modifier):
    total = 0
    numberOfDice = modifier[0]
    sizeOfDice = modifier[1]
    for i in range(numberOfDice):
        total += D(sizeOfDice)
    return total

#Check a D20 + a modifier against a difficulty
def check(difficulty, modifier=[0,0]):
    roll=D(20)
    mod = modify(modifier)
    total = roll+mod
    if total>=difficulty:
        return 1
    else:
        return 0

#run check() loopCount times and return the percentage of successes
def average(difficulty, loopCount, modifier=[0,0]):
    successes = 0
    for i in range(loopCount):
        successes += check(difficulty, modifier)
    percentage = (successes/loopCount)*100
    return percentage

def stats():
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    for i in range(10000):
        _roll = D(1,6)
        if _roll == 1:
            one+=1
        if _roll == 2:
            two+=1
        if _roll == 3:
            three+=1
        if _roll == 4:
            four+=1
        if _roll == 5:
            five+=1
        if _roll == 6:
            six+=1
    print(one)
    print(two)
    print(three)
    print(four)
    print(five)
    print(six)
