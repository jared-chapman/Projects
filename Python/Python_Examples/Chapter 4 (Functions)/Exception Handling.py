#Catch error after input
a = 4
b = 0

try:
    print(a/b)
except ZeroDivisionError:
    print("b cannot be 0")


#Catch error with input
try:
    x=6
    y=0
    print(x/y)
except (ZeroDivisionError, ValueError):
    print("Invalid Input")

#Don't use variables defind in a try statement in an except statement
#Exception could occour before variable is defined
