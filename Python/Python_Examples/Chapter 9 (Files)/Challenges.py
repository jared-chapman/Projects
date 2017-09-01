#1
import csv
with open("CSV_test.csv", "r") as f:
    w = csv.reader(f, delimiter=",")
    for row in w:
       print(",".join(row))

#2 skip
#3
full_list = list()
listOne = ("Item one", "Item two", "Item three")
listTwo = ("Item four", "Item five", "Item six")
listThree = ("Item seven", "Item eight", "Item nine")
full_list.append(listOne)
full_list.append(listTwo)
full_list.append(listThree)
print(full_list)

with open("CSV_test.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    i=0
    for row in full_list:
        w.writerow(full_list[i])
        i += 1
