#Escaping
#Escape a character wiht a \
#No escape needed for ""s inside ''s or ''s within ""s

print("She said \"surely\"")
print("She said 'surely'")
print('She said "surely"')

#Slicing
#Syntax is [iterable][[start_index:end_index]]
#includes item at start index, but not end index
var = ["one",
       "two",
       "three",
       "four",
       "five",
       "six"]
print(var)
var = var[2:5]
print(var)
