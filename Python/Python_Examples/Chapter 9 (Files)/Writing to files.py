#open a file with the open function
#Takes two parameters, a string representing the path, and a string representing the mode to open the file in
#File paths shouldn't be typed manually as different OS's label them differently
#Instead, use the built-in os module. Takes each location in a file as a parameters

#Filepath parameter
import os
filepath = os.path.join("C",
                        "Users",
                        "jared",
                        "Desktop",
                        "Python Examples",
                        "Chapter 9 (Files)",
                        "Example.py")
print(filepath)

#Mode parameter
#R - read only
#W - for writing only. Overwrites file if it exists. Creates a new file if it doesn't
#W+ - for reading and writing. Overwrites file if it exists. Creates a new file if it doesn't



#open function returns an object, called a file object
#Which can be used to read or write to a file .
#If you open a file with the open function, you must cles it with the close function.

#Opens a file, writes text to it, then closes the file
st = open("st.txt", "w")
st.write("Hi from Python!")
st.close
