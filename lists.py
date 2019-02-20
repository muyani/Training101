emptyString =""
print(type(emptyString))
myFirstNumber = 0
emptyList = []
noiseMakers = ["Brian","Mike",9,True,emptyString]
daysOfTheWeek = ["Monday","Tuesday",
                 "wEDNESDAY","Thurday",
                 "Friday",
                 "Saturday","Sunday"]
print(daysOfTheWeek)
numberOfDaysInAWeek = len(daysOfTheWeek)
print(numberOfDaysInAWeek)


# list indexing


print(daysOfTheWeek[2])

# before colon symbolizes the starting position
# after colon sysmbolizes the end position but exclusive


sublist =daysOfTheWeek[3:4]
print(sublist)

details = ["Muyani",40,"johndoe@example.com","Nairobi"]
age = details[1]
location =details[3]

reverse = details[-3:3]
# reverse = details[-2:]


print ("Reverse",reverse)


numbers = [0,1,1,1,2,2,3,4,5,6,7,8,9,10]

print(set(numbers))

subnum = numbers[-3:-1]
print(subnum)
print(daysOfTheWeek)
daysOfTheWeek.append(numbers)
print(daysOfTheWeek[-1])

# daysOfTheWeek.clear()
daysOfTheWeek
print(daysOfTheWeek)

list1 = set([0,1])
list2 = [2,3]
list3 = list1+list2
list1.append(list2)
print(list1)
print(list3)
print(type(list1))

