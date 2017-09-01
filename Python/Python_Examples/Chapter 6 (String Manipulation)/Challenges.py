#1
var = "Camus"
for i in range(len(var)):
    print(var[i])

#2 skip
#3
var = "aldous Huxley was born in 1894".capitalize()
print(var)

#4
var = "Where now? Who now? Why now?"
print(var)
var = var.split("?")
print(var)

#5
var = ["The"
       "fox"
       "jumped"
       "over"
       "the"
       "fence"
       "."]
var = " ".join(var) #This doesn't work, but I think it's a problem with atom
print(var)

#6
var = "A screaming comes across the sky"
var = var.replace("s", "$")
print(var)

#7
var = "Hemingway"
print(var)
var = var.index("m")
print(var)

#8
var = "And god said \"Let there be pizza!\""
print(var)

#9
var = "Three"
print(var)
var = var + var + var
print(var)
var = "Three"
var = var*3
print(var)

#10
var = "It was a bright cold day in April, and the clocks were striking thirteen."
print(var)
commaIsAt = var.index(",")
var = var[0:commaIsAt]
print(var)
