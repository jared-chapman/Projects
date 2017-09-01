#1
shows = ["The Walking Dead",
         "Entourage",
         "The Sopranos",
         "The Vampire Diaries"]
for i in shows:
     print(i)

#2
for i in range(25, 51):
    print(i)

#3
for i, show in enumerate(shows):
    print(i, show)

#4 Not gonna mess with input
"""
x = 0
while x = 0:
    print("Type q to quit")
    in = input
    if in = "q":
        x=1;
"""

#5
products = []                               #Declares master
first =  [8,    19, 148,    4]              #First list
second = [9,    1,  33,     83]             #Second list
for i in range(0,4):                        #Loop 4 times(0-3)
    products.append(first[i]*second[i])     #Append product to products list
print(products)
