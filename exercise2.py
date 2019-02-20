taskList = [23,"Jane",["Lesson 23",560,{"currency":"KES"}],987,(76,"John")]
# 1. Determine the type of variable taskList using an inbuilt function
print(type(taskList))


# 2. Print "KES"

print(taskList[2][2]["currency"])

# 3. Print 560

print(taskList[2][1])


# 4. use a function to determine the length of taskList
print (len(taskList))

# 5.Reverse 987 to 789 using an inbuilt function



# print(int(d[::-1]))
taskList.pop(3)
taskList.insert(3,789)
print(taskList)

# 6. change name "John" to "Jane"
# not possible

