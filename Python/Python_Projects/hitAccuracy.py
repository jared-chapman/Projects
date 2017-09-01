"""
This is a simple program for measuring how many times Mayweather knocks McGregor
Did you know they were fighting today? You'd think people would be talking about
a fight this big but I've barely heard anything. Weird.

Anyway it's really just an checking out global variables and classes. I've read
to avoid global variables for the sake of clarity, but I'm not sure how to do
that here and have the same effect. Am I being too java-y? Maybe (Hopefully)
future Jared will know the answer.
"""


class accuracyKeeper:
    hitKey = "a"
    missKey = "d"


    def setKeys(self):
        global hitKey
        global missKey
        self.hitKey = input("input the hit key: ")
        self.missKey = input("input the miss key: ")
        self.hitAccuracy()


    def hitAccuracy(self):
        hit = 0
        miss = 0
        total = 0
        count = input("Press " + self.hitKey + " for a hit and " + self.missKey + " for a miss: ")
        for i in range(len(count)):
            if(str(count[i]) == self.hitKey):
                hit += 1
            elif(count[i] == self.missKey):
                miss += 1
        count = hit + miss
        accuracy = hit/count
        print(str(hit) + " hit(s) in " + str(count) + " attempts")
        print (str(accuracy) + "% accuracy")

ak = accuracyKeeper()
ak.setKeys()
