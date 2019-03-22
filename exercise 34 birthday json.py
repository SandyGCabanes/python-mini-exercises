#sandygcabanes
#practicepython.org
#exercise 34 birthday json
"""Exercise 34 (and Solution)
This exercise is Part 2 of 4 of the birthday data exercise series.
The other exercises are: Part 1, Part 3, and Part 4.

In the previous exercise we created a dictionary of famous scientists’
birthdays. In this exercise, modify your program from Part 1 to load the
birthday dictionary from a JSON file on disk, rather than having the dictionary
defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to the
dictionary, and update the JSON file you have on disk with the scientist’s name.
If you run the program multiple times and keep adding new names, your JSON file
should keep getting bigger and bigger.
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

#creating a list from the dictionary
bts_keys = bts_dict.keys()
print ("Welcome to the bts birthday dictionary.  We know the birthdays of:", "\n".join(bts_dict.keys()))
bts_member = str(input("Whose birthday do you want to look up?"))
print ("{}'s birthday is on {}".format(bts_member, bts_dict[bts_member]))

# add a member and his birthday
bts_dict["member_name"] = "member_bday"
print (bts_dict)

"""bday.json file before and after adding
bday.json before
{"Jungkook": "Sept 1 1997", "V": "Dec 30 1995", "Jimin": "Oct 13 1995", "Suga": "Mar 9 1993", "J-Hope": "Feb 18 1994", "Jin": "Dec 4 1992", "RM": "Sept 12 1994"}
bday.json after
{"Jungkook": "Sept 1 1997", "V": "Dec 30 1995", "Jimin": "Oct 13 1995", "Suga": "Mar 9 1993", "J-Hope": "Feb 18 1994", "Jin": "Dec 4 1992", "RM": "Sept 12 1994", "member_name": "member_bday"}
"""