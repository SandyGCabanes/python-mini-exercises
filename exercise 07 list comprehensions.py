#sandygcabanes
#practicepython.org
#exercise 07 list comprehensions
"""Exercise 7 (and Solution)
Let’s say I give you a list saved in a variable:
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
    Write one line of Python that takes this list a and makes a new list
    that has only the even elements of this list in it.
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
a_even = [num for num in a if num % 2 == 0]
#a_odd = [num for num in a if num % 2 == 1]
#print (a_even)
#print (a_odd)

