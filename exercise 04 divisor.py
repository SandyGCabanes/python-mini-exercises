#sandygcabanes
#practicepython.org
#exercise 04 divisor
"""Exercise 4 (and Solution)
Create a program that asks the user for a number and then prints out a list
of all the divisors of that number. (If you don’t know what a divisor is, it is
a number that divides evenly into another number. For example, 13 is a divisor
of 26 because 26 / 13 has no remainder.)
"""

num = int(input("Type in any whole number: "))
divisor = 2
list_divisors = [1]
while divisor < num :
    if num % divisor == 0 :
        list_divisors.append (divisor)
    elif num % divisor >0 :
        pass
    divisor += 1
print ()
print ("Divisors of {} are:".format(num) , list_divisors)



