marks = int(input("Enter your marks "))


# # if else
# if marks >= 350 :
#     print("Congratulations you have qualified")
# else:
#     print("Sorry You have failed")


# grading system
average = marks/5
if average >= 80 and average < 101:
    print("A")
elif average >=70 and average < 80:
    print("B")
elif average >=60 and average < 70:
    print("C")
elif average >=50 and average < 60:
    print("D")
else:
    print("E")