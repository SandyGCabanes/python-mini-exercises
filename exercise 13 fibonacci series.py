#sandygcabanes
#practicepython.org
#exercise 13 fibonacci series
"""Fibonacci
Exercise 13 (and Solution)
Write a program that asks the user how many Fibonnaci numbers
to generate and then generates them. Take this opportunity
to think about how you can use functions.
Make sure to ask the user to enter the number of
numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers
where the next  number in the sequence is the sum of
the previous two numbers  in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
Practice functions!
"""

n = int(input("Enter how many Fibonacci numbers to generate."))
print (n)
if n == 1:
    print ([1])

elif n == 2:
    print ([1,1])
elif n >2:
    fibolist = [1,1]
    i = 2
    while i < n :
        newitem = fibolist[i-1] + fibolist[i-2]
        fibolist.append(newitem)
        i += 1
    print (fibolist)
