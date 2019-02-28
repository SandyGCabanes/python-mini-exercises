#sandygcabanes
#practicepython.org
#exercise 15 reverse word order
"""Reverse Word Order
Exercise 15 (and Solution)  A Popular Interview Question
Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string,
except with the words in backwards order. For example, say I type the string:
My name is Michele
Then I would see the string:  Michele is name My
Concepts: splitting strings and joining strings
SPLITTING
teststring = "  this      has a lot    of   spaces and    tabs"
result = teststring.split()
'this', 'has', 'a', 'lot', 'of', 'spaces', 'and', 'tabs']
JOINING
listofstrings = ['a', 'b', 'c']
result = "**".join(listofstrings)
a**b**c
"""

stringa = "Concentration and deep work"
print (stringa)
lista = stringa.split()
#print (lista)
listrev = []
def reverse_list(list_):
    n = len(list_)
    while n > 0:
        listrev.append(list_[n-1])
        n -= 1
    #print ("reversed list: listrev")
    #print (listrev)

reverse_list(lista)
print(" ".join(str(item) for item in listrev))




