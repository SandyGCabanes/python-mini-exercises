#sandygcabanes
#practicepython.org
#exercise 31 guess letters
"""
Guess Letters
Exercise 31 (and Solution)
This exercise is Part 2 of 3 of the Hangman exercise series.
The other exercises are: Part 1 and Part 3.
Let’s continue building Hangman. In the game of Hangman, a clue word is given
by the program that the player has to guess, letter by letter. The player
guesses one letter at a time until the entire word has been guessed. (In the
actual game, the player can only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise,
write the logic that asks a player to guess a letter and displays letters in
the clue word that were guessed correctly. For now, let the player guess an
infinite number of times until they get the entire word. As a bonus, keep track
of the letters the player guessed and display a different message if the player
tries to guess that letter again. Remember to stop the game when all the letters
have been guessed correctly! Don’t worry about choosing a word randomly or
keeping track of the number of guesses the player has remaining - we will deal
with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on, until the player gets the word.

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
    i = 0
    while i< len(listlines):
        listlines[i] = listlines[i].replace("\n", "")
        i += 1

    #print("1st item=", listlines[0], "20th item=", listlines[19]) ##debugging


#Hangman game begins here
print("Welcome to Hangman")


numlines = len(listlines)
#print(numlines)  ##debugging

#picking the word out of the list

import random

index_word= random.randint(1, numlines)
picked_word = listlines[index_word]
list_picked_word = list(picked_word)
num_letters =len(list_picked_word)
print("picked_word", picked_word)


"""creating the blanks to be shown to gamer"""
newlist = []
for i in range(num_letters):
    newlist.append("_ ")
print("".join(newlist))
n=0

def guess_turn():
    """function to be called within matching function"""
    guess_l = str(input("Guess a letter:"))
    guess_l = guess_l.upper()
    return guess_l

"""guessing function, inner loop within the word, with 'if' filter outside for end of game"""
list_guesses = []
def matching(list_picked_word, num_letters, newlist):
    if newlist == list_picked_word:
        print ("End of game")
    else:
        i = 0
        guess_letter = guess_turn()
        while guess_letter in list_guesses:
            print ("Letter ", guess_letter, "is already used. Pick another.")
            guess_letter = guess_turn

        #matching the current guess with each letter in the list of picked word
        for i in range(num_letters):
            if (guess_letter) == list_picked_word[i]:
                newlist[i] = (guess_letter)
                #print ("newlist", newlist) ## debugging
                print ("  ".join(newlist))
                i +=1

            else:
                pass
                i += 1

        #keeping track of guesses
        list_guesses.append(guess_letter)
        print("letters guessed so far:", set(list_guesses))

        matching(list_picked_word, num_letters, newlist)

#playing the game:
matching(list_picked_word, num_letters, newlist)

