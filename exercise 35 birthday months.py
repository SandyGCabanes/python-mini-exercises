#sandygcabanes
#practicepython.org
#exercise 35 birthday months
""" Exercise 35 and Solution
This exercise is Part 3 of 4 of the birthday data exercise series.
The other exercises are: Part 1, Part 2, and Part 4.

In the previous exercise we saved information about famous scientists’ names
and birthdays to disk. In this exercise, load that JSON file from disk,
extract the months of all the birthdays, and count how many scientists have
a birthday in each month.

Your program should output something like:

{
	"May": 3,
	"November": 2,
	"December": 1
}
"""

import time
today_date_time = time.asctime( time.localtime(time.time()) )
print(today_date_time)

#set of data, name and bday
btsbdays = {'Jungkook': 'Sept 1 1997', 'V': 'Dec 30 1995', 'Jimin': 'Oct 13 1995', 'Suga': 'Mar 9 1993', 'J-Hope': 'Feb 18 1994', 'Jin': 'Dec 4 1992', 'RM': 'Sept 12 1994'}

import json
with open("C:/Users/sandy/Desktop/data_copies/btsbdays.json", "w") as f:
    json.dump(btsbdays, f)

with open("C:/Users/sandy/Desktop/data_copies/btsbdays.json", "r") as f:
    bts_dict = json.load(f)
    print (type(bts_dict))    ## <class 'dict'>
    print (bts_dict)
    """{'Jungkook': 'Sept 1 1997', 'V': 'Dec 30 1995', 'Jimin': 'Oct 13 1995', 'Suga': 'Mar 9 1993', 'J-Hope': 'Feb 18 1994', 'Jin': 'Dec 4 1992', 'RM': 'Sept 12 1994'}"""

#creating a list from the dictionary bts_dict
bdays = bts_dict.values()
print ("bdays=", bdays)
bday_string = " ".join(bdays)
print (bday_string)
bdays_newlist = bday_string.split(" ")
print ("bdays_newlist", bdays_newlist)
bday_months = []
i = 0
while i < len(bdays_newlist):
    if bdays_newlist[i].isdigit():
        pass
    else:
        bday_months.append(bdays_newlist[i])
    i += 1
print("bday_months", bday_months)
from collections import Counter
c = Counter (bday_months)
print (c)

"""
bts_list = list(bts_dict)
print (bts_list)
only the keys are listed ['Jungkook', 'V', 'Jimin', 'Suga', 'J-Hope', 'Jin', 'RM']
"""
