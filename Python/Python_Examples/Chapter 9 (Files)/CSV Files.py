#Can work with CSV(Comma Seperated Values) files.
#Can use with statement to open a CSV file, but CSV module needs to be inside with statement to convert object into CSV object
#CSV module has a method called 'writer' that accepts a file object and a delimiter
#The 'writer' method returns a csv object
#CSV object has a method called 'writerow'
#'writerow' method accepts a list as a parameter, and you can use it to write a CSV file.
#Every element in the list gets written, seperated by the delimiter you pass into 'writerow' method, to a row in the CSV file
#The 'writerow' method only creates one row, so it would have to be called twice to write two rows, etc.

import csv
with open("st.csv", "w") as f:
    w = csv.writer(f,
                   delimiter=",")
    w.writerow(["one",
                "two",
                "three"])
    w.writerow(["four",
                "five",
                "six"])

#Can use CSV module to read contents of a file with the reader method
with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
#this code iterates through the csv object using a for loop
#Each time around the loop, you call the join method on a comma to add a comme between
#Each piece of data in the file and print the contents (as they appear, seperated by a comma)
