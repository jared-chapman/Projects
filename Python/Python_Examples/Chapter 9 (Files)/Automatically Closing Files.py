#Second, preferred syntax to open files.
#Syntax is:
#with open([file-path], [mode]) as [variable name]:
#   [your_code]
#Where variable name is the name the file object is assigned

#Same as Writing to Files.py, but fewer lines and don't have to manually close
#Can access file object (f) as long as you are in the with statement
with open("st.txt", "w") as f:
    f.write("Hi from Python!")
