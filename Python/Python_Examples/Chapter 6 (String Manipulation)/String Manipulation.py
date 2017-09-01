#Strings spanning multiple lines must be surrounded in triple quotes
#Strings are iterable, too!
var = "Jared"
print(var[0])
print(var[-2])

#Strings are immutable
#Concatenation
var = "cat " + "in " + "the " + "hat"
print(var)

#String mutliplication
var = "Hello! " * 3
print(var)

#change case
var = "heLlO"
print(var)
var = var.upper()
print(var)
var = var.lower()
print(var)

#capitalize first letter of String
var = "four score and seven years ago."
print(var)
var = var.capitalize()
print(var)

#Format
#looks for {} in string and replaces with parameter
var = "William {}".format("Faulkner")
print(var)
#Can use multiples
var = "{} was born in {}".format("Jared",
                                 "1992")
print(var)

#Split (makes a list)
var = "Hello.Yes"
print(var)
var = var.split(".")
print(var)

#join
var = "abc"
print(var)
var = "+".join(var)
print(var)

#Can turn a list of strings into a single string
var = ["one"
         "two"
         "three"
         "four"
         "five"]
print(var)
var = " ".join(var)
print(var)

#Strip space from lead and tail
var = "    the   "
print(var)
var = var.strip()
print(var)

#replace
var = "all animals are equal"
print(var)
var = var.replace("a", "@")
print(var)

#Find an index
var = "abcdefghijklmnopqrstucwxyz"
print(var)
var = var.index("m")
print(var)
