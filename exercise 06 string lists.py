#sandygcabanes
#practicepython.org
#exercise 06 string lists
"""Exercise 06 and solution
Ask the user for a string and print out whether this string is a palindrome or
not. (A palindrome is a string that reads the same forwards and backwards.)"""

new_str = str(input("Type in any string: "))
list_a = list(new_str)
len_a = len(new_str)
list_b = []
i = len_a -1
while i != -1:
    list_b.append(list_a[i])
    i -= 1
print("Your input string in a list format:  ", list_a)
print("Reverse of that list:  ", list_b)

if list_a == list_b:
    print("That string is a palindrome.")
else:
    print("That string is not a palindrome.")
