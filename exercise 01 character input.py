#sandygcabanes
#practicepython.org
#exercise 01 character input
"""Exercise 1 (and Solution)
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
Extras:
Add on to the previous program by asking the user for another number
and printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
"""

name = input("Please type your name:  ")
age = int(input("Please input your age:  "))
no_copies = int(input("Please input no. of times we print."))

year_born= 2019 - age
year_100 = year_born + 100

copy_number = 1
while copy_number < no_copies +1:
    print ("Hi {}! You will turn 100 on {}.".format(name, year_100))
    copy_number +=1

