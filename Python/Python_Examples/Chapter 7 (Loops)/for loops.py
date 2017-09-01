#for [variable name] in [iterable name]: [instructions]
name = "Ted"
for i in name:
    print(i)
#In each loop, [variable name] gets assigned to an item in the [iterable name]
#Can iterate through Strings, Lists, Tuples, Keys in Dictionaries (but not in order)

#Can use for loops to change items in a mutable container
tv = ["GOT",
      "Narcos",
      "Vice"]
print(tv)
i = 0
for show in tv:             #i has to be declared and manually updated within the loop
    new = tv[i]             #Because for loops don't incriment a variable, rather cycle through
    new = new.upper()       #items in a list
    tv[i] = new
    i += 1
print(tv)

#This syntax fixes that problem, and is more similar to java, gml, js, etc.
television = ["Parks and Rec",
              "The Office",
              "Jane the Virgin"]
print(television)
for i, show in enumerate(television):       #This syntax builds in incrementation of i(or whatever variable)
    new = television[i]
    new = new.upper()
    television[i] = new
print(television)

#Can use for loops to move data between mutable iterables
all_shows = []
tv = ["The Path",
      "Mad Men",
      "The Get Down"]
movies = ["Once",
          "The Life Aquatic",
          "Split"]
for show in tv:
    show = show.upper()
    all_shows.append(show)
for mv in movies:
    mv = mv.upper()
    all_shows.append(mv)
print(all_shows)
