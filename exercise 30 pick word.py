#sandygcabanes
#practicepython.org
#exercise 30 pick word
"""
Pick Word
Exercise 30 (and Solution)
This exercise is Part 1 of 3 of the Hangman exercise series.
The other exercises are: Part 2 and Part 3.
In this exercise, the task is to write a function that picks a random word
from a list of words from the SOWPODS dictionary. Download this file and save
it in the same directory as your Python code. This file is Peter Norvig’s
compilation of the dictionary of words used in professional Scrabble
tournaments. Each line in the file contains a single word.
Hint: use the Python random library for picking a random word.
Check out:
Exercise 22: read from a file
Exercise 9: generating a random number
Exercise 3: accessing an element of a list

"""
#using C:/Users/sandy/Desktop/data_copies/sowpods.txt  2906kb
print ("sowpods.txt")
import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

# create new list: listlines containing all the words
with open('C:/Users/sandy/Desktop/data_copies/sowpods.txt', 'r') as textfile:
    line = textfile.readline()
    numlines = 0
    listlines = []
    while line:
        #print(line)
        listlines.append(line)
        numlines += 1
        line = textfile.readline()
    #print('numlines=', numlines)
    ##numlines= 267751

    #delete line breaks per item
    #item.replace("\n", "") should work, based on forums
    i = 0
    while i< len(listlines):
        listlines[i] = listlines[i].replace("\n", "")
        i += 1


    """
    #check if line breaks are deleted
    first2 =(listlines[0]),str(listlines[1])
    last2 = (listlines[len(listlines)-2]), (listlines[len(listlines)-1])
    print("first2", first2)
    print("last2", last2)
    """

#choose a random word from the 267751 options
import random

index_word= random.randint(1, numlines)
print ("index_word", index_word)
picked_word = listlines[index_word]
print ("picked_word", picked_word)
list_picked_word = list(picked_word)
print (list_picked_word)
print ("len(list_picked_word)", len(list_picked_word))












