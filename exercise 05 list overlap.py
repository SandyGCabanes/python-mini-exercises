#sandygcabanes
#practicepython.org
#exercise 05 list overlap
"""Exercise 5 (and Solution)
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
Extras:
Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out
at this point - we’ll get to it soon)
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

i = 0
newlist = []
while i < len(b):
    for element in a:
        if element == int(b[i]):
           newlist.append (b[i])
        else:
           pass
    i += 1
n = 1
if newlist.count(newlist[n]) > 1:
    newlist.remove(newlist[n])
else:
    pass
n +=1

print ("Common to a and b are:", newlist)



