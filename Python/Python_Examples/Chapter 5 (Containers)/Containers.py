#List is a container that stores objects in a specific order
#Lists are iterable and mutable

#Creates an empty list
fruit = list()
vegetable = []
print(fruit)

#Create list with items
fruit = ["Apple", "Orange", "Pear"]
print(fruit)

#Lists are iterable
print(fruit[1])

#lists are mutable
fruit[2] = "Banana"
print(fruit)

colors = ["Red", "Blue", "Green"]
print(colors)
lastItem = colors.pop()                 #pop returns last item in list and removesit from list
print(colors)
print(lastItem)


#Can add lists together
fruitAndColors = fruit + colors
print(fruitAndColors)

print("Banana" in fruit)                #Returns if an item is in a list
print("Black" not in fruit)             #Opposite



#Tuple is a container that stores onjects in a specific order.
#Tuples are immutable and interable

#Both declare a Tuple
my_tuple = tuple()
my_tuple = ()
#Declares a tuple with items in it
rndm = ("M. Jackson", 1958, True)
#An item must be followed by a comma, even if it is a single item.



#Dictionaries are containers with key-value pairs
#Dictionaries are mutable, but are not iterable

#Both declare a dictionary
my_dict = dict()
my_dict = ()

#Decalres Dictionary with key: value pairs in it
fruits = {"Apple":
          "Red",
          "Banana":
          "Yellow"}
print(fruits)

#add a value
fruits["Pear"] = "Green"
print(fruits)

#look up a key
print(fruits["Apple"])

#Check if key is in dictionary
print("Banana" in fruits)
#Doesn't work with values

#Delete key-value pair
del fruits["Apple"]
print(fruits)

#dictionary keys must be immutable.
#strings and tuples can be dictionary keys, but lists and dictionarys cannot
#any object can be a dictionary value


#Containers can be stored in containers (ex. lists of lists)
