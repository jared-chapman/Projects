"""
Used for simulating Dice rolls and checking them against a difficulty
"""

import random


#Rolls a D(x) die
def D(die):
    return random.randint(1, die)

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



print(average(10, 10000, [5,6]))


print(D(6))
print(modify([3,6]))
