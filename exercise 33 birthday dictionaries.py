#sandygcabanes
#practicepython.org
#exercise 33 birthday dictionaries
"""Birthday Dictionaries
Exercise 33 (and Solution)
This exercise is Part 1 of 4 of the birthday data exercise series.
The other exercises are: Part 2, Part 3, and Part 4.

For this exercise, we will keep track of when our friend’s birthdays are,
and be able to find that information based on their name. Create a dictionary
(in your file) of names and birthdays. When you run your program it should ask
the user to enter a name, and return the birthday of that person back to them.
The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
"""

import time
today_date_time = time.asctime( time.localtime(time.time()) )
print(today_date_time)

keys_bts = ['Jungkook', 'V', 'Jimin', 'Suga', 'J-Hope', 'Jin', 'RM']
values_bts = ['Sept 1 1997', 'Dec 30 1995', 'Oct 13 1995', 'Mar 9 1993', 'Feb 18 1994', 'Dec 4 1992', 'Sept 12 1994']
dict_bts = dict(zip(keys_bts, values_bts))
#print (dict_bts)

#creating a list from the dictionary
bts_keys = dict_bts.keys()
print ("Welcome to the bts birthday dictionary.  We know the birthdays of:", "\n".join(dict_bts.keys()))
bts_member = str(input("Whose birthday do you want to look up?"))
print ("{}'s birthday is on {}".format(bts_member, dict_bts[bts_member]))

