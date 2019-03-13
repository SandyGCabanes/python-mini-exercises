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
Instead of using the .txt file from above take this Training_01.txt file,
and count how many of each “category” of each image there are.
This text file is actually a list of files corresponding to the SUN database
scene recognition database, and lists the  file directory hierarchy for the
images. Once you take a look at the first line or two of the file, it will be
clear which part represents the scene category.
To do this, you’re going to have to remember a bit about string parsing in
Python 3. I talked a little bit about it in this post.
"""
#using Training_01.txt
print ("Training_01.txt")
import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

with open('C:/Users/sandy/Docs - Private/+python/practicepython.org/Training_01.txt', 'r') as textfile:
    line = textfile.readline()
    numlines = 0
    listlines = []
    while line:
        #print(line)
        listlines.append(line)
        numlines += 1
        line = textfile.readline()
    #print('numlines=', numlines)
    ##numlines= 19850

    #print (listlines)
    ##['/a/abbey/sun_aqswjsnjlrfzzhiz.jpg\n', ...'/y/youth_hostel/sun_ammfvvfoiqxeovyl.jpg\n']

    #lstring =str("".join(listlines))
    ##produces a string with no '' marks but with line breaks

# parse first using split
i=0
y = []
while i <len(listlines):
    new_element = (listlines[i].split("/"))
    y.append(new_element)
    i+=1
print("checking","len(y)",len(y))

"""
#check if y list was constructed correctly:
print ("y=")
print (y) #each string is replaced by a list of strings, correctly done

print ("y[0]", y[0])
print ("len(y[0])",len(y[0])) #returns 4, which means y is correctly done
"""

# get the third item in each element and create new list ynew, print
# discovered through trial and error: index of list within list (list[index])[index2]
ind = 0   #index of each LIST element in y, up to len(y)
ynew = []
#loop inside y
while ind < len(y):
    #loop inside ylist
    ind2 = 0  #index of item within each element y[ind], up to len(ylist)
    while ind2 < len(y[ind]):
        if ind2 == 2:
            ynew.append(str((y[ind])[ind2])) #discovered through trial and error
        if ind2!= 2:
            pass
        ind2+=1
    ind +=1

#checking for correct outputs
#print("len(ynew)",len(ynew))
  ##returns correct length
#print("ynew", ynew)
  ##returns correct list
#print("len(ynew[0])",len(ynew[0]))
  ##returns 5 for 'abbey'
#print ("len(ynew[19849])",len(ynew[19849]))
  ## returns 12
#print("set(ynew)=",set(ynew))
  ##returns set(ynew)= {...'attic', 'inn', 'firing_range'}
#print("len(set(ynew))=",len(set(ynew)))
##returns len(set(ynew))= 362
print ("no. of categories=", len(set(ynew)))










