#sandygcabanes
#practicepython.org
#exercise 14 remove duplicates
"""List Remove Duplicates
Exercise 14 (and Solution)
Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.
Extras:
Write two different functions to do this - one using a loop and
constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that
in a different function.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# using loop and set
def remove_dup(list_):
    i=0
    while i < len(list_):
        new_list = list(set(x for x in list_ if list_.count(list_[i]) ==1))
        i += 1
    new_list.sort()
    print ("result using remove_dup:")
    print (new_list)

remove_dup(a)

# using loop only
def remove_dup2(lis2_):
    i = 1
    new_lis2 = [lis2_[0]]
    while i < len(lis2_):
        if lis2_.count(lis2_[i]) == 1:
            new_lis2.append(lis2_[i])
        else:
            pass
        i += 1

    print ("result using remove_dup2:")
    print (new_lis2)
remove_dup2(a)


