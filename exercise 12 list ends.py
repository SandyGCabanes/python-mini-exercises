#sandygcabanes
#practicepython.org
#exercise 12 list ends
"""List Ends
Exercise 12 (and Solution)
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""

a = [5, 10, 15, 20, 25]
def listends(new_list):
    first = new_list[0]
    last = new_list[len(new_list)-1]
    listends = [first, last]
    print(listends)

listends(a)


