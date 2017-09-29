"""
Create and present all stats for a new Dungeon Crawl Classic Character
"""

import roll

class Character(object):

    def __init__(self):
        """
        Assign stats
        """

        #Base Stats
        self.strength        = roll.D(3, 6)
        self.agility         = roll.D(3, 6)
        self.stamina         = roll.D(3, 6)
        self.personality     = roll.D(3, 6)
        self.intelligence    = roll.D(3, 6)
        self.luck            = roll.D(3, 6)

        #Ability Modifiers       0     1     2    3  4  5  6  7  8 9 10 11 12 13 14 15 16 17 18
        abilityScoreModifier = (None, None, None,-3,-2,-2,-1,-1,-1,0, 0, 0, 0, 1, 1, 1, 2, 2, 3)
        self.strengthModifier        = abilityScoreModifier[self.strength]
        self.agilityModifier         = abilityScoreModifier[self.agility]
        self.staminaModifier         = abilityScoreModifier[self.stamina]
        self.personalityModifier     = abilityScoreModifier[self.personality]
        self.intelligenceModifier    = abilityScoreModifier[self.intelligence]
        self.luckModifier            = abilityScoreModifier[self.luck]

        if self.strengthModifier >= 0:
            self.strengthModModifier = "+"
        else:
            self.strengthModModifier = ""

        if self.agilityModifier >= 0:
            self.agilityModModifier = "+"
        else:
            self.agilityModModifier = ""

        if self.staminaModifier >= 0:
            self.staminaModModifier = "+"
        else:
            self.staminaModModifier = ""

        if self.personalityModifier >= 0:
            self.personalityModModifier = "+"
        else:
            self.personalityModModifier = ""

        if self.intelligenceModifier >= 0:
            self.intelligenceModModifier = "+"
        else:
            self.intelligenceModModifier = ""

        if self.luckModifier >= 0:
            self.luckModModifier = "+"
        else:
            self.luckModModifier = ""

        #Luck Modifier
        self.luckAffectsList = (
            "Empty",
            "Harsh winter: All attack rolls",
            "The bull: Melee attack rolls",
            "Fortunate date: Missile fire attack rolls",
            "Raised by wolves: Unarmed attack rolls",
            "Conceived on horseback: Mounted attack rolls",
            "Born on the battlefield: Damage rolls",
            "Path of the bear: Melee damage rolls",
            "Hawkeye: Missile fire damage rolls",
            "Pack hunter: Attack and damage rolls for 0-level starting weapon",
            "Born under the loom: Skill checks (including thief skills)",
            "Fox’s cunning: Find and disable traps",
            "Four-leafed clover: Find secret doors",
            "Seventh son: Spell checks",
            "The raging storm: Spell damage",
            "Righteous heart: Turn unholy checks",
            "Survived the plague: Magical healing*",
            "Lucky sign: Saving throws",
            "Guardian angel: Savings throws to escape traps",
            "Survived a spider bite: Saving throws against poison",
            "Struck by lightning: Reflex saving throws",
            "Lived through famine: Fortitude saving throws",
            "Resisted temptation: Willpower saving throws",
            "Charmed house: Armor Class",
            "Speed of the cobra: Initiative",
            "Bountiful harvest: Hit points (applies at each level)",
            "Warrior’s arm: Critical hit tables**",
            "Unholy house: Corruption rolls",
            "The Broken Star: Fumbles**",
            "Birdsong: Number of languages",
            "Wild child: Speed (each +1/-1 = +5’/-5’ speed)")
        self.luckAffectsRoll = roll.D(1, 30)
        self.luckAffects = self.luckAffectsList[self.luckAffectsRoll]

        #HP
        self.hitPoints = roll.D(1, 4) + self.staminaModifier

        #Saving Throws
        self.fortitudeMod   = 0
        self.reflexMod      = 0
        self.willpowerMod   = 0
        self.fortitudeThrow = self.fortitudeMod + self.staminaModifier
        self.reflexThrow    = self.reflexMod    + self.agilityModifier
        self.willpowerThrow = self.willpowerMod + self.personalityModifier

        #Occupation / Inventory
        self.occupationRoll             = roll.D(1,100)
        self.occupationTable            = ["Empty",
                            "Alchemist",
                            "Animal trainer",
                            "Armorer",
                            "Astrologer",
                            "Barber",
                            "Beadle",
                            "Beekeeper",
                            "Blacksmith",
                            "Butcher",
                            "Caravan guard",
                            "Cheesemaker",
                            "Cobbler",
                            "Confidence artist",
                            "Cooper",
                            "Costermonger",
                            "Cutpurse",
                            "Ditch digger",
                            "Dwarven apothecarist",
                            "Dwarven blacksmith",
                            "Dwarven blacksmith",
                            "Dwarven chest-maker",
                            "Dwarven herder",
                            "Dwarven miner",
                            "Dwarven miner",
                            "Dwarven mushroom-farmer",
                            "Dwarven rat-catcher",
                            "Dwarven stonemason",
                            "Dwarven stonemason",
                            "Elven artisan",
                            "Elven barrister",
                            "Elven chandler",
                            "Elven falconer",
                            "Elven forester",
                            "Elven forester",
                            "Elven glassblower",
                            "Elven navigator",
                            "Elven sage",
                            "Elven sage",
                            "Farmer*",
                            "Farmer*",
                            "Farmer*",
                            "Farmer*",
                            "Farmer*",
                            "Farmer*",
                            "Farmer*",
                            "Farmer*",
                            "Farmer*",
                            "Fortune-teller",
                            "Gambler",
                            "Gongfarmer",
                            "Grave digger",
                            "Grave digger",
                            "Guild beggar",
                            "Guild beggar",
                            "Halfling chicken butcher",
                            "Halfling dyer",
                            "Halfling dyer",
                            "Halfling glovemaker",
                            "Halfling gypsy",
                            "Halfling haberdasher",
                            "Halfling mariner",
                            "Halfling moneylender",
                            "Halfling trader",
                            "Halfling vagrant",
                            "Healer",
                            "Herbalist",
                            "Herder",
                            "Hunter",
                            "Hunter",
                            "Indentured servant",
                            "Jester",
                            "Jeweler",
                            "Locksmith",
                            "Mendicant",
                            "Mercenary",
                            "Merchant",
                            "Miller/baker",
                            "Minstrel",
                            "Noble",
                            "Orphan",
                            "Ostler",
                            "Outlaw",
                            "Rope maker",
                            "Scribe",
                            "Shaman",
                            "Slave",
                            "Smuggler",
                            "Soldier",
                            "Squire",
                            "Squire",
                            "Tax collector",
                            "Trapper",
                            "Trapper",
                            "Urchin",
                            "Wainwright",
                            "Weaver",
                            "Wizard’s apprentice",
                            "Woodcutter",
                            "Woodcutter",
                            "Woodcutter"]
        self.occupationWeaponTable      = ["None",
                            "Staff",
                            "Club",
                            "Hammer (as club)",
                            "Dagger",
                            "Razor (as dagger)",
                            "Staff",
                            "Staff",
                            "Hammer (as club)",
                            "Cleaver (as axe)",
                            "Short sword",
                            "Cudgel (as staff)",
                            "Awl (as dagger)",
                            "Dagger",
                            "Crowbar (as club)",
                            "Knife (as dagger)",
                            "Dagger",
                            "Shovel (as staff)",
                            "Cudgel (as staff)",
                            "Hammer (as club)",
                            "Hammer (as club)",
                            "Chisel (as dagger)",
                            "Staff",
                            "Pick (as club)",
                            "Pick (as club)",
                            "Shovel",
                            "Club",
                            "Hammer",
                            "Hammer",
                            "Staff",
                            "Quill (as dart)",
                            "Scissors (as dagger)",
                            "Dagger",
                            "Staff",
                            "Staff",
                            "Hammer",
                            "Bow",
                            "Dagger",
                            "Dagger",
                            "Pitchfork (as spear)",
                            "Pitchfork (as spear)",
                            "Pitchfork (as spear)",
                            "Pitchfork (as spear)",
                            "Pitchfork (as spear)",
                            "Pitchfork (as spear)",
                            "Pitchfork (as spear)",
                            "Pitchfork (as spear)",
                            "Pitchfork (as spear)",
                            "Dagger",
                            "Club",
                            "Trowel (as dagger)",
                            "Shovel (as staff)",
                            "Shovel (as staff)",
                            "Sling",
                            "Sling",
                            "Hand axe",
                            "Staff",
                            "Staff",
                            "Awl (as dagger)",
                            "Sling",
                            "Scissors (as dagger)",
                            "Knife (as dagger)",
                            "Short sword",
                            "Short sword",
                            "Club",
                            "Club",
                            "Club",
                            "Staff",
                            "Shortbow",
                            "Shortbow",
                            "Staff",
                            "Dart",
                            "Dagger",
                            "Dagger",
                            "Club",
                            "Longsword",
                            "Dagger",
                            "Club",
                            "Dagger",
                            "Longsword",
                            "Club",
                            "Staff",
                            "Short sword",
                            "Knife (as dagger)",
                            "Dart",
                            "Mace",
                            "Club",
                            "Sling",
                            "Spear",
                            "Longsword",
                            "Longsword",
                            "Longsword",
                            "Sling",
                            "Sling",
                            "Stick (as club)",
                            "Club",
                            "Dagger",
                            "Dagger",
                            "Handaxe",
                            "Handaxe",
                            "Handaxe",
                            ]
        self.occupationTradeGoodTable   = ["None",
                                "Oil, 1 flask",
                                "Pony",
                                "Iron helmet",
                                "Spyglass",
                                "Scissors",
                                "Holy symbol",
                                "Jar of honey",
                                "Steel tongs",
                                "Side of beef",
                                "Linen, 1 yard",
                                "Stinky cheese",
                                "Shoehorn",
                                "Quality cloak",
                                "Barrel",
                                "Fruit",
                                "Small chest",
                                "Fine dirt, 1 lb.",
                                "Steel vial",
                                "Mithril, 1 oz.",
                                "Mithril, 1 oz.",
                                "Wood, 10 lbs.",
                                "Sow**",
                                "Lantern",
                                "Lantern",
                                "Sack",
                                "Net",
                                "Fine stone, 10 lbs.",
                                "Fine stone, 10 lbs.",
                                "Clay, 1 lb.",
                                "Book",
                                "Candles, 20",
                                "Falcon",
                                "Herbs, 1 lb.",
                                "Herbs, 1 lb.",
                                "Glass beads",
                                "Spyglass",
                                "Parchment and quill pen",
                                "Parchment and quill pen",
                                "Hen*",
                                "Hen*",
                                "Hen*",
                                "Hen*",
                                "Hen*",
                                "Hen*",
                                "Hen*",
                                "Hen*",
                                "Hen*",
                                "Tarot deck",
                                "Dice",
                                "Sack of night soil",
                                "Trowel",
                                "Trowel",
                                "Crutches",
                                "Crutches",
                                "Chicken meat, 5 lbs.",
                                "Fabric, 3 yards",
                                "Fabric, 3 yards",
                                "Gloves, 4 pairs",
                                "Hex doll",
                                "Fine suits, 3 sets",
                                "Sailcloth, 2 yards",
                                "5 gp, 10 sp, 200 cp",
                                "20 sp",
                                "Begging bowl",
                                "Holy water, 1 vial",
                                "Herbs, 1 lb.",
                                "Herding dog**",
                                "Deer pelt",
                                "Deer pelt",
                                "Locket",
                                "Silk clothes",
                                "Gem worth 20 gp",
                                "Fine tools",
                                "Cheese dip",
                                "Hide armor",
                                "4 gp, 14 sp, 27 cp",
                                "Flour, 1 lb.",
                                "Ukulele",
                                "Gold ring worth 10 gp",
                                "Rag doll",
                                "Bridle",
                                "Leather armor",
                                "Rope, 100’",
                                "Parchment, 10 sheets",
                                "Herbs, 1 lb.",
                                "Strange-looking rock",
                                "Waterproof sack",
                                "Shield",
                                "Steel helmet",
                                "Steel helmet",
                                "100 cp",
                                "Badger pelt",
                                "Badger pelt",
                                "Begging bowl",
                                "Pushcart***",
                                "Fine suit of clothes",
                                "Black grimoire",
                                "Bundle of wood",
                                "Bundle of wood",
                                "Bundle of wood",
                                ]
        self.occupation                 = self.occupationTable[self.occupationRoll]
        self.weapon                     = self.occupationWeaponTable[self.occupationRoll]
        self.tradeGoods                 = self.occupationTradeGoodTable[self.occupationRoll]
        self.gold                       = roll.D(5, 12)
        self.randomItemTable            = ["None",
                                            "Backpack",
                                            "Candle",
                                            "Chain, 10’",
                                            "Chalk, 1 piece",
                                            "Chest, empty",
                                            "Crowbar",
                                            "Flask, empty",
                                            "Flint & steel",
                                            "Grappling hook",
                                            "Hammer, small",
                                            "Holy symbol",
                                            "Holy water, 1 vial**",
                                            "Iron spikes, each",
                                            "Lantern",
                                            "Mirror, hand-sized",
                                            "Oil, 1 flask***",
                                            "Pole, 10-foot",
                                            "Rations, per day",
                                            "Rope, 50’",
                                            "Sack, large",
                                            "Sack, small",
                                            "Thieves’ tools",
                                            "Torch, each",
                                            "Waterskin",
                                            ]
        self.randomItem                 = self.randomItemTable[roll.D(1,24)]
        self.inventory = [self.weapon, self.tradeGoods, self.randomItem]


        if "Dwarven" in self.occupation:
            self._class = "Dwarf"
        elif "Elven" in self.occupation:
            self._class = "Elf"
        elif "Halfling" in self.occupation:
            self._class = "Halfling"
        else:
            self._class = "Choose a Class"



    def printStats(self):
        print("Class:        " + self._class)
        print("Strength:     " + "(" + self.strengthModModifier + str(self.strengthModifier) + ")  "+ str(self.strength) )
        print("Agility:      " + "(" + self.agilityModModifier + str(self.agilityModifier) + ")  " + str(self.agility) )
        print("Stamina:      " + "(" + self.staminaModModifier + str(self.staminaModifier) + ")  " + str(self.stamina) )
        print("Personality:  " + "(" + self.personalityModModifier + str(self.personalityModifier) + ")  "+ str(self.personality) )
        print("Intelligence: " + "(" + self.intelligenceModModifier + str(self.intelligenceModifier) + ")  "+ str(self.intelligence) )
        print("Luck:         " + "(" + self.luckModModifier + str(self.luckModifier) + ")  "+ str(self.luck) )
        print("Luck Affects: " + self.luckAffects)
        print("Occupation    " + str(self.occupation))
        print("Inventory     " + str(self.gold) + " Copper Pieces")
        for i, item in enumerate(self.inventory):
            #print(self.inventory[i])
            print("              " + self.inventory[i])



c = Character()
c.printStats()
