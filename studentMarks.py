from functions import *

total = totalMarks(85,56,78,45,67)


avg = average(total)

grade = findgrade(avg)
print(grade)
print(total)


# Define Function to reverse name
def reverseName(name):
    x = name[::-1]
    return x



# Get name from user
myName = input("What is your name:")


# pASS ARGUMENT NAME TO BE REVERSED
reversedN = reverseName(myName)

print(reversedN)












