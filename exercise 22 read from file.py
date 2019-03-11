#sandygcabanes
#practicepython.org
#exercise 22 read from file
"""
Read From File
Exercise 22 (and Solution)
Given a .txt file that has a list of a bunch of names, count how many of each
name there are in the file, and print out the results to the screen. I have
a nameslist.txt file for you, if you want to use it!

Extra:
Instead of using the .txt file from above (or instead of, if you want the
challenge), take this Training_01.txt file, and count how many of each
“category” of each image there are. This text file is actually a list of files
corresponding to the SUN database scene recognition database, and lists the
file directory hierarchy for the images. Once you take a look at the first line
or two of the file, it will be clear which part represents the scene category.
To do this, you’re going to have to remember a bit about string parsing in
Python 3. I talked a little bit about it in this post.
"""
#using nameslist.txt
with open('C:/Users/sandy/Docs - Private/+python/practicepython.org/nameslist.txt', 'r') as textfile:
    line = textfile.readline()
    numlines = 0
    Luke = 0
    Lea = 0
    Darth = 0
    while line:
        if list(line) == ['L', 'u', 'k', 'e', '\n'] :
            Luke += 1
        if list(line) == ['L', 'e', 'a', '\n']:
            Lea += 1
        if list(line) == ['D', 'a', 'r', 't', 'h', '\n']:
            Darth +=1
        if list(line) == ['D', 'a', 'r', 't', 'h']:
            Darth +=1
        else:
            'name not recognized'
        numlines += 1
        line = textfile.readline()
    print ('Luke=', Luke)
    print ('Lea=', Lea)
    print ('Darth=', Darth)
    print ('numlines', numlines)

