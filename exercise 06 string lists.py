#sandygcabanes
#practicepython.org
#exercise 06 string lists
"""EExercise 6 (and Solution)
Ask the user for a string and print out whether this string is a palindrome
or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

str_a = input("type in a string: ")
list_a = list (str_a)
print (list_a)
list_a_rev = list(reversed(list_a))
print(list_a_rev)

if list_a == list_a_rev:
    print ("String a is a palindrome.")
else:
    print ("String a is not a palindrome.")







