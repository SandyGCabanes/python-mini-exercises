#sandygcabanes
#practicepython.org
#exercise 36 birthday plots
"""Birthday Plots
Exercise 36 (and Solution)
This exercise is Part 4 of 4 of the birthday data exercise series.
The other exercises are: Part 1, Part 2, and Part 3.
In the previous exercise we counted how many birthdays there are in each month
in our dictionary of birthdays.

In this exercise, use the bokeh Python library to plot a histogram of which
months the scientists have birthdays in! Because it would take a long time
for you to input the months of various scientists, you can use my scientist
birthday JSON file. Just parse out the months (if you don’t know how,I suggest
looking at the previous exercise or its solution) and draw your histogram.
"""

import time
today_date_time = time.asctime( time.localtime(time.time()) )
print(today_date_time)

#set of data, name and bday
btsbdays = {'Jungkook': 'Sep 1 1997', 'V': 'Dec 30 1995', 'Jimin': 'Oct 13 1995', 'Suga': 'Mar 9 1993', 'J-Hope': 'Feb 18 1994', 'Jin': 'Dec 4 1992', 'RM': 'Sep 12 1994'}

import json
with open("C:/Users/sandy/Desktop/data_copies/btsbdays.json", "w") as f:
    json.dump(btsbdays, f)

with open("C:/Users/sandy/Desktop/data_copies/btsbdays.json", "r") as f:
    bts_dict = json.load(f)
    print (type(bts_dict))    ## <class 'dict'>
    print (bts_dict)
    ##{'Jungkook': 'Sep 1 1997', 'V': 'Dec 30 1995', 'Jimin': 'Oct 13 1995', 'Suga': 'Mar 9 1993', 'J-Hope': 'Feb 18 1994', 'Jin': 'Dec 4 1992', 'RM': 'Sep 12 1994'}"""

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
print (c)  ## Counter({'Sep': 2, 'Dec': 2, 'Oct': 1, 'Mar': 1, 'Feb': 1})

from bokeh.plotting import figure, show, output_file
output_file("exercise36.html")

x_categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
c = dict(c)
x = list(c.keys())
y = list(c.values())

p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width = 0.5)
show(p)





