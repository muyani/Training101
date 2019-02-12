my_first_string = "hello world"

# capitalize the first letter of the string
print(my_first_string.capitalize())

# make every letter of the string capital
print(my_first_string.upper())
# make every letter of the string lower
print(my_first_string.lower())
# o = "o"
# count a specified letter in that string
print(my_first_string.count("o"))


# multiple assignment
first_name,second_name = "Muyani","Letina"
print (first_name)
print(second_name)
# concatenating two strings
fullname = first_name+" "+second_name
print(fullname)

first_letter = fullname[0]
last_letter = fullname[-1]
last_letter = fullname[len(fullname)-1]

print(first_letter.islower())
# determining the length of a string
length_of_my_fullname = len(fullname)
print(length_of_my_fullname)