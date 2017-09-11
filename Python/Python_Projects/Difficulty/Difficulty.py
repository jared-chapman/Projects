"""
This is a work in progress. The goal is to be able to input an ability with values
and a calculator with corresponding values, then use the calculator to find the
difficulty of the ability. Additionally, store the attributes of the abilities and
call them for reference.
"""


import pickle
import os


#Here we want to create a list of dictionaries. Each item in the list is a
#Dictionary representing an ability and its stats
abilities = []

class Calculator(object):
    def __init__(self, damageMod, healingMod, _rangeMod, targetsMod, badassnessMod, createItemMod):
        self.damageMod      = damageMod
        self.healingMod     = healingMod
        self._rangeMod      = _rangeMod
        self.targetsMod     = targetsMod
        self.badassnessMod  = badassnessMod
        self.createItemMod  = createItemMod

    def calculate(self, ability):
        difficulty = (self.damageMod * ability.damage) +\
                     (self.healingMod * ability.healing) +\
                     (self._rangeMod * ability._range) +\
                     (self.targetsMod * ability.targets) +\
                     (self.badassnessMod * ability.badassness) +\
                     (self.createItemMod * ability.createItem)
        return difficulty


"""Defalt Calculator Values"""
c = Calculator(1, 2, 2, 3, -1, 3)
""""""""""""""""""""""""""""""

class Ability(object):
    def __init__(self, name, damage, healing, _range, targets, badassness, createItem):
        self.name = name
        self.damage = damage
        self.healing = healing
        self._range = _range
        self.targets = targets
        self.badassness = badassness
        self.createItem = createItem

def loadAbilities():
    """
    Unpickles abilities and saves them as dictionaries in the abilities list
    """
    global abilities
    if os.path.getsize('abilityData.pk1') > 0:
        with open('abilityData.pk1', 'rb') as input:
            if len(abilities) == 0:
                abilities = pickle.load(input)



def printAbilityNames():
    """
    Prints the newest item in abilities if the list isn't empty
    TODO: Make this print a matrix of saved abilities
    """
    if len(abilities) > 0:
        print(abilities[len(abilities)-1]["name"])


"""Defalt Calculator Values"""
c = Calculator(1, 2, 2, 3, -1, 3)
""""""""""""""""""""""""""""""


def updateCalculator():
    """
    Asks user for input to update the Calculator values
    """
    global c
    damageMod = input("Enter Damage Modifier")
    healingMod = input("Enter Healing Modifier")
    _rangeMod = input("Enter Range Modifier")
    targetMod = input("Enter Target Modifier")
    badassnessMod = input("Enter Badassness Modifier")
    createItemMod = input("Enter Create Item Modifier")
    c = Calculator(int(damageMod), int(healingMod), int(_rangeMod), int(targetMod), int(badassnessMod), int(createItemMod))

def inputAbility():
    """
    Asks user for input on ability stats, and returns the difficulty using the
    set calculator.
    """
    global c
    global abilities
    name = input("Enter new ability name: ")
    damage = input("Enter Damage: ")
    healing = input("Enter Healing: ")
    _range = input("Enter Range: ")
    targets = input("Enter Targets: ")
    badassness = input("Enter badassness: ")
    createItem = input("CreateItem: ")
    a = Ability(name, int(damage), int(healing), int(_range), int(targets), int(badassness), int(createItem))
    print(name + " Difficulty: " + str(c.calculate(a)))
    save = input("Save? 1=Yes, 2=no ")
    if (save):
        abilities.append({"name": name,
                          "damage": damage,
                          "healing": healing,
                          "range": _range,
                          "targets": targets,
                          "badassness": badassness,
                          "createItem": createItem})
        with open('abilityData.pk1', 'wb') as output:                           #Pickles Ability
            pickle.dump(abilities, output, pickle.HIGHEST_PROTOCOL)

inputAbility()
print(abilities[len(abilities)-1]["name"])
