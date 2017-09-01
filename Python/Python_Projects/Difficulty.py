"""
Used to determine the difficulty of an ability in the incredibly
popular tabletop game Adventures Unlimited.
"""



def rate(name, damage, healing, _range, targets, badassness, createItem):
    abilityName = name
    difficulty    = 0

    #Edit these values 
    damageMod     = 2
    healingMod    = 1
    rangeMod      = 2
    targetsMod    = 2
    badassnessMod = -1
    createItemMod = 3

    difficulty = (damageMod * damage) +\
                 (healingMod * healing) +\
                 (rangeMod * _range) +\
                 (targetsMod * targets) +\
                 (badassnessMod * badassness) +\
                 (createItemMod * createItem)

    if(damageMod > 0 & healingMod > 0):
        difficulty += 3
    if(abilityName == ""):
        abilityName = "Difficulty: "

    print("\n" + abilityName + ": " + str(difficulty) + "\n")





def userLoop():
    while True:
        name        = (input("Name: "))
        damage      = int(input("Damage: "))
        healing     = int(input("Healing: "))
        _range      = int(input("Range: "))
        targets     = int(input("targts: "))
        badassness  = int(input("badassness: "))
        createItem  = int(input("createItem: "))
        rate(name, damage, healing, _range, targets, badassness, createItem)

userLoop()
