#Pass "r" as the mode parameter to read a file
with open("st.txt", "r") as f:
    print(f.read())

#Can only read contents once without re-opening and closing file,
#Best to save contents to a variable

my_list = list()

with open("st.txt", "r") as f:
    my_list.append(f.read())

print(my_list)
