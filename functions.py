# a function is a block of code that is used to perform a related action

# creating /defining a funnction
def chapisha(sth):
    print(sth)

#
#
# calling/using the function
# chapisha("muyani")

#
# chapisha("Austine")
#
# function to calaculate total

def totalMarks(math,eng,kis,sci,ssr):
    totalMarks = math+eng+kis+sci+ssr
    return totalMarks


def average(t):
    avg = t/5
    return avg

def findgrade(average):
    if average >= 80 and average < 101:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "E"



