#Range creates a sequence of integers and can iterate through them
#Includes first parameter, but not second
for i in range(1,11):
    print(i)

#While loops continue as long as expression is true
#while [expression]: {code}
x=10
while x>0:
    print(x)
    x-=1
print("Happy New Year!")


#Break will terminate loop
y=10
while y>0:
    print(y)
    y-=1
    if y==4:
        break
""" problem?
#Continue will stop current iteration and move to the next one
z = 0
while z<10:
    if z==4:
        continue
    z+=1
    print(z)
"""
#nested loop
name = ["a",
        "b",
        "c"]
for i in range(1,3):
    print(i)
    for letter in name:
        print(letter)

#Can nest for in why and vice-versa
