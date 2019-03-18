#sandygcabanes
#practicepython.org
#exercise 28 max of three
"""Max Of Three
Exercise 28 (and Solution)
Implement a function that takes as input three variables, and returns the
largest of the three. Do this without using the Python max() function!
The goal of this exercise is to think about some internals that Python normally
takes care of for us. All you need is some variables and if statements!
"""

num1 = int(input("input first number:  "))
num2 = int(input("input second number:  "))
num3 = int(input("input third number:  "))

if (num1 > num2) and (num1 > num3):
   max = num1
elif (num2 > num1) and (num2 > num3):
   max = num2
elif (num3 > num1) and (num3> num2):
    max = num3
elif (num1 == num2):
    if num1 > num3:
        max = num1
    elif num3 > num1:
        max = num3
elif (num2 == num3):
    if num2 > num3:
        max = num2
    elif num3 > num2:
        max = num3
elif (num1 == num3):
    if num1 > num2:
        max = num1
    elif num2 > num1:
        max = num2
print ("max of {}, {}, {} is ".format(num1, num2, num3), max)

