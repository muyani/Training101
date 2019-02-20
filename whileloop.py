# a while loop tells python to
# repeat execution of a certain statement or
# block of statements until a
# specified condition is false


i = 0
numbers = [0,1,2,3,4,5]
#
# while len(numbers)> 0:
#     print(numbers)
#     numbers.pop()
#

#
# while i<10:
#     print("muyani")
#     i+=1

password_saved = "1234"

password = input("Enter your password")
tries = 1
maxTries = 3
while password != "1234" and tries < 3 :
    maxTries -= 1
    password = input("please enter correct password "+ maxTries + "tries left".format(maxTries))

    tries +=1

if tries >= 3:
    print("Pin blocked,your card is held")
else:
    print("hurray correct password entered")


