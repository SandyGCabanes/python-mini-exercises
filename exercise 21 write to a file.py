#sandygcabanes
#practicepython.org
#exercise 21 write to a file
"""Write To A File
Exercise 21 (and Solution)
Take the code from the How To Decode A Website exercise (if you didn’t do it
or just want to play with some different code, use the code from the solution),
 and instead of printing the results to a screen, write the results to a
 txt file. In your code, just make up a name for the file you are saving to.
Extras:
Ask the user to specify the name of the output file that will be saved.
"""

#url https://news.yahoo.com/
import requests
url = 'https://news.yahoo.com/'
r = requests.get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, "lxml")
string_=""

for story_heading in soup.find_all(class_="Lh(15px) Fw(b) LineClamp(3,45px) D(i)--sm1024 Pend(10px)--sm1024"):

    with open("C:/users/sandy/Desktop/yahoo_news.txt", "a+") as open_file: # include whole path #choose a+ instead of a
        open_file.write(str(string_))    #convert object to str to write to file

    if story_heading.a:
        string_ = (str(story_heading.a.text.replace("\n", " ").strip())) +("\n")

    else:
        string_ = (str(story_heading.contents[0].strip())) +("\n")


""" to check if file exists
import os.path
if os.path.isfile("C:/users/sandy/Desktop/yahoo_news.txt"):
   print("yahoo_news.txt")
"""



