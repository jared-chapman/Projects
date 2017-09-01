#Define a function with [def functionName(paramaters):]
def double(x):
    return x*2

#Call a function with [functionName(paramaters)]
result = double(3)
print(result)




#A function doesn't have to have parameters
def sayMyName():
    return "Jared"

name = sayMyName()
print(name)


#A function can have multiple parameters, and doesn't have to return
def multiply(a,b):
    print(a*b)

multiply(3,4)

#A function can have optional parameters
#Optional parameters are defined with the function
def pow(q, w=2):
    """
    :q: int to be squared
    :w: to the power of
    :return: int q to the power of w, or squared if blank
    """
    return q**w
print(pow(4,4))     #4 to the power of 4
print(pow(5))       #5 to the power of 2

#Built-in Functions
print(len("Hello"))
print(str(100))     #int to string
print(int("4"))     #string to int
print(float(100))   #int to float
