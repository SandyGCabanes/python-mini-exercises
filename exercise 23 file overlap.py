#sandygcabanes
#practicepython.org
#exercise 23 file overlap
"""Exercise 23 (and Solution)
Given two .txt files that have lists of numbers in them, find the numbers that
are overlapping. One .txt file has a list of all prime numbers under 1000,
and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other
 number. And yes, happy numbers are a real thing in mathematics - you can look
 it up on Wikipedia. The explanation is easier with an example, which I will
 describe below.)
Topics:
Reading a file, in Exercise 21
Number types and converting to integers from strings, in Exercise 1
Lists, in Exercise 3 and Exercise 5
"""
print ("happynumbers.txt", "primenumbers.txt")
import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

happy = 'C:/Users/sandy/Docs - Private/+python/practicepython.org/happynumbers.txt'
prime = 'C:/Users/sandy/Docs - Private/+python/practicepython.org/primenumbers.txt'

#read happy text file and import to newhappy list
# no index needed if using readline
with open(happy, 'r') as open_file:
    line = open_file.readline()
    line = line.replace("\n","")
    numlines = 0
    newhappy = []
    while line:
        newhappy.append(line)
        numlines += 1
        line = open_file.readline()
        line = line.replace("\n","")
print("newhappy first=",newhappy[0])
print("newhappy last=",newhappy[len(newhappy)-1])


#read prime text file and import to newprime list
# no index needed if using readline
with open(prime, 'r') as open_file:
    line = open_file.readline()
    line = line.replace("\n","")
    numlines = 0
    newprime = []
    while line:
        newprime.append(line)
        numlines += 1
        line = open_file.readline()
        line = line.replace("\n","")
print("newprime first=",newprime[0])
print("newprime last=",newprime[len(newprime)-1])


# check for overlaps between newhappy and newprime, print
i = 0
overlaps = []
while i < len(newhappy):
    for element in newhappy:
        if int(element) == int(newprime[i]):
           overlaps.append (newprime[i])
        else:
           pass
    i += 1
print ("Common to happynumbers and primenumbers are:", overlaps)
