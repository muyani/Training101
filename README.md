# Python 101
These are files for learning basic python programming with examples and comments as description of what every line does.

## Day One
### what to cover
- Why Programming without practice is so pointless.
- A small History and Explanation about Python.
- Python milestones i.e from 2.7 to 3.7.
- Python as a General purpose language.
- Python as an Interpreted language.
- Python as an interactive language.
- Python as an object oriented language.
- What you need in the course. 
- Naming conventions in Python.
- Python Reserved words.
- Python Syntax.
- Hello World in Python.

  ## What is Python?
- Python is a Free open-source general purpose programming language with applications in web development (Websites and Online Systems), software development (Desktop Apps), API Development and Mobile App development (Kivy’s Framework). 
NB: Python 2 is no longer supported we therefore shall use Python 3
   ## Why Python?
Today there are so many programming languages to choose from and every one of them differs in ease-of-use, complexity and application. If you are just getting started to Program, we recommend a language with friendly syntax i.e Human readable, easy to setup and has wide variety of applications. Python is best fit for all the above and is definitely here to stay.
  ## Installing Python
      Linux / Unix / OSX 
        - sudo apt-get python3
      Windows 
        - Download & Install python3.6.x.exe.
        Make sure you check the tab for adding to path
        Open Command Prompt and type “python” to confirm it is added to the global variables

## Rules of Naming Identifiers in Python
- They can not contain spaces e.g “total marks”. Should instead be “totalMarks”(camel case) or “total_marks” (snake case).
- They can not start with a number e.g “5totalMarks”.
- They can not contain special characters i.e “!@#$%^&*()” .
- They can not contain keywords e.g “sql, functions, class..”. Please note that keywords differ from language to language, i.e SELECT is a keyword in SQL but not in Python, Class is a keyword in Python but not SQL and IF is a keyword in both. Be keen in identifying this


## Virtual Environment
A virtual environment is a folder created inside your project folder that contains the Libraries/Modules that are required in the particular project.
You will learn more about Virtual environments once you start using external libraries in the
 future clases.
##### To Create a Virtual Environment
Open Pycharm and click on File->Settings. Click on dropdown on Project Interpreter then click show all, Add on the plus button to click a new one.

## Create a new Project
All Python Files have the .py extensions and are interpreted by the python.exe we have in our global variable. 
   - Open Pycharm and click on File->New Project. Change the project name in the popup that appears by changing untitled to “Training”. And click ok.
   - We shall only do this once as project refers to a folder, therefore all the files we will create in the next coming days will be saved  there.

## Create your first python file (helloworld.py)
  - Right click on the Training Folder->New->Python File.
  - In the Popup that appears type “hello” then click okay.
## Print Function in Python
- Use print() function. This is an inbuilt function in Python to display values in the console window in Pycharm.
- Syntax: print(“Hello John”) . This should display the word “Hello John”
NB: Note that using double or single quotes does not matter .
- Then run the program to show the above.
- The console is the only interface we shall use in the Python Basics class. In the Python for Web Part of this training we shall use an interface created using HTML and CSS.

## create a file called Variables.py
- Add 5 numbers and display them in the console using Print. i.e print(56+72+67+93+78)
NB: Note we did not need to add double or single quotes when adding numbers. That only applies to words (string).
- print(“Total Marks is ”, 56+72+67+93+78) - You can also concatenate two parts or more using commas. 
- If you had to do various tasks using the results of 56+72+67+93+78, you would have to repeat the entire calculation, which makes it very bulky in a large program.
- We therefore use variables for this. Variables are temporary storage locations used to store data. So in the above case: we would have total = 56+72+67+93+78, and print(total)

## Day Two
## what will be covered
- Variables.
- Declaration and Assignment of variables in python.
- Standard Data types.
- Checking type of variables.
- Typecasting variables(knowing what and when to typecast).
- Arithmetic operators in python.
- Comparison Operators in python.
- Logical Operators in python.
- Decison Making in python.

## various data types in Python
- Strings
- Numbers (Integers/Float/Double)
- List
- Tuples
- Dictionary
- Boolean

## String
-  This is a variable used to hold all types of  characters. 
#### Example
``` python
 firstName = “John”
 secondName = “Doe”
```




  
## Day Three
### What will be covered 
- Lists
- List methods.
- Tuples
- Dictionaries
- Dictionary methods
- Loops.

Lists is a collection of more than 1 variable. They need NOT be of the same Datatype.
Imagine fetching data from a row in a database. For example records belonging to a person you can have it  in a list.
A list is defined using square brackets and each value is referenced using an index starting from 0, 1, 2 and so forth.
Example is: 
``` python
person = [“John Doe”, 30, “john@mail.com”, “Nairobi”]
```
To access the name we use:
``` python
person[0]
```
 To access the age: 
 ``` python
 person[1]
 ```
 
 TASK: Create a List of days of the Week. Print the whole list and Print this day.

## List operations
Functions on lists : 
``` python
len(list)
```
- Gives the length of the list.
``` python
list1 + list2 
```
- Concatenate two list

``` python
list1 * 4
```
Repetition 

Membership 
``` python
“Wednesday” in daysOfTheWeek #(Returns a Boolean)
```
Delete element in a list 
``` python
del list1[2]
 ```
Update list 
``` python
list [2] = 65
```

## List slicing
Get values in a section, range or a specific index using colon.
Start daysOfTheWeek[n:p] - where n represents the index of the value in the list you want to start from. p -1 represents the index of the value in the list you want to end.

## Tuple

Defined exactly same way as a list except you use round brackets. Create the same exact daysOfTheWeek using tuples.
Perform all operations possible as you did on lists.
What is the difference between a list and a tuple?
 ## Dictionary
 
 Let say you have a very large list/tuple for you to access values you have to count through the index. This can become very hard and impossible for large lists.
 
Therefore dictionaries solve this using key:value pairs. Defined inside curly braces.

Example:
``` python
person = {“name” : “John Doe”, “age”:30, “location”: “Nairobi”, “email” :”johndoe@mail.com”}
```
Accessing a dictionary:
``` python
person[‘name’] = John doe
```
## Do the following task
``` python
taskList = [23, “Jane”, [“Lesson 23”, 560, {“currency” : “KES”}], 987, (76,”John”)]
```

- Determing type of variable is taskList using an inbuilt function
- Print KES 
- Print 560 
- Use a function to determine the length of taksList 
- Reverse 987 to display 789 NOT using an inbuilt  function  
- Change the name “John” to “Jane” - N/A

## Comparison Operators
Conditional Operators check the following:
- < less than
- > greater than 
- == (Check equlity)
- != (Check Inequlity)
- <> (Check equlity)

## Logical Operators
The logical Operators :
- or - At least one condition is true.
- and - All conditions have to be true.
- not - Reverse the state of its operands

## IF ELSE statements
In most programs you will be encountered with a situation where you have to take a certain path if the results of a condition is TRUE or take another if FALSE.

We use IF and ELSE Statement to make such a decision.
``` python
if (avaerageMarks < 50):
  print(“Pass”)
else:
    print(“Fail”)

```

## IF ELIF statements
In most programs you will be encountered with a situation where you have to more than 2 possible conditions.
We use IF and ELIF Statement to make such a decision and finish with an Else statemnt.
For this you use the grading system :
A > 79 , B - 60 to 78, C -  59 to 49, D - 48 to 40, E - less 40
The program should output the right grade


## While loops
Should you want to execute a statement UNTIL a certain condition is false:
``` python
while i <= 10:
  print(i)
  i = i + 1 or i += 1

```

## a moment please ..

For example you have already inputed marks of 500 students and you want to generate and display grade for each student, which approach would you take? Let everyone try this for 5 students….

With the knowledge we have now, when you want to do a certain task multiple times, you will have to rewrite the statement multiple times right?


##  Functions
We should create a function that ‘findgrade’ by 
taking in marks of each subject as parameters
calculating total from the parameters(subjects) passed
calculating the average from the total
using if statement to find grade 
             now!!
what if I want to get total marks! and average?

``` python
def totalMarks(m,e,s,sci,sco):
	total = m +e +s+sci+sco
	return total 
def avgMarks(total):
	avg = total / 5
	return avg
def findGrade(avg):
	if avg > 80:
		return “A”
```
    
And now to call/use the functions

``` python
total =totalMarks(2,3,45,6,7)

average = avgMarks(total)

grade = findGrade(average)
```
At this point in time you are now ready to handle the 5 tasks.

To better test your understanding, avoid google the questions directly. Refer to this documentation for syntax referencing.


























  


