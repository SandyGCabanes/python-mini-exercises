#sandygcabanes
#practicepython.org
#exercise 20 element search
"""Element Search
Exercise 20 (and Solution)
Write a function that takes an ordered list of numbers (a list where the
elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the list
and returns (then prints) an appropriate boolean.
Extras:
Use binary search.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = 9
c = 55

print("using list comprehension")
def check_num_ifin_alist(num, alist):
    if num in alist:
        print("True")
    else:
        print("False")
check_num_ifin_alist(b,a)
check_num_ifin_alist(c,a)

#binary search defined as sub-dividing and looping until num is within sub-list
print("using binary search")
def bincheck_num_ifin_alist(num,alist):
    """binary search loop method"""
    end = len(alist) -1
    start = 0
    num_in_alist = False
    while (num_in_alist == False and end>start):
        mid = (end + start)//2       # mid changes after loop
        if num == alist[mid]:        # if num is the middle, then True
            num_in_alist = True

        elif num < alist[mid]:
            end = mid -1     # list starts at 0 and ends in the middle

        elif num > alist[mid]:
            start = mid +1   # list starts at middle and ends the same

        else:
            num_in_alist = False
    return num_in_alist

print(bincheck_num_ifin_alist(b,a))
print(bincheck_num_ifin_alist(c,a))