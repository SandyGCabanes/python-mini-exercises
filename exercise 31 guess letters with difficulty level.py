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

    #print("1st item in listlines=", listlines[0], "100th item in listlines=", listlines[99]) ##debugging

    """ check the longest item to identify max range for difficulty() function"""
    """
    i = 0
    number_of_letters_list = []
    while i<len(listlines):
        n_item = len(listlines[i])
        number_of_letters_list.append(n_item)
        i +=1
    new_set = set(number_of_letters_list)
    print (new_set)  #{2,3,4,5,6,7,8,9,10,11,12,13,14,15}
    print("longest_word =", max(new_set), "letters") #15 letters
    """

#Hangman game begins here
print("Welcome to Hangman! Input level of difficulty.")

# input level of difficulty:
level = str(input("Choose from 1-easy, 2-medium, 3-hard, 4-any: "))
#print("level:", level)

def difficulty(chosen_level, motherlist):
    #going through each word in the motherlist to create childlist or sublist
    i = 0
    childlist = []
    if chosen_level == '1':
        wordlength = [2,3,4,5,6]
    elif chosen_level == '2':
        wordlength = [7,8,9,10,11]
    elif chosen_level =='3':
        wordlength = [12,13,14,15]
    elif chosen_level == '4':
        wordlength = [x for x in range(2,16)]
    while i < len(motherlist):
        if len(motherlist[i]) in wordlength:
            childlist.append(motherlist[i])
        else:
            pass
        i += 1

    #print("first item in childlist=", childlist[0])
    #print("last item in childlist=", childlist[len(childlist)-1])
    return childlist

difficulty(level, listlines) #returns childlist from motherlist
listwords = difficulty(level, listlines) #childlist is now the list of words
numlines = len(listwords)
#print("numlines in listwords, now childlist", numlines) ##debugging

#picking the word out of the list
import random
index_word= random.randint(1, numlines)
picked_word = listwords[index_word]
list_picked_word = list(picked_word)
num_letters =len(list_picked_word)
#print("picked_word", picked_word)    ##debugging

"""creating the blanks or clue to be shown to gamer"""
newlist = []
for i in range(num_letters):
    newlist.append("_ ")
print("".join(newlist))


def guess_turn():
    """function to be called within matching function"""
    guess_l = str(input("Guess your letter:"))
    guess_l = guess_l.upper()
    return guess_l

"""setting up the list of wrong letters guessed so far"""
wrong_letters = []

"""guessing function, inner loop within the word, outer loop while guess is incorrect"""
def matching(list_picked_word, num_letters, newlist, wrong_guesses):
    if newlist == list_picked_word:
        print("Congratulations! You guessed the word.")
    elif newlist != list_picked_word:
        i = 0
        guess_letter = guess_turn()
        # guess another letter in case it was used before
        if guess_letter in wrong_letters:
            print ("Already taken. Guess another:")
            matching(list_picked_word, num_letters, newlist,wrong_guesses)
        else:
            pass
        # matching each letter of the random word
        for i in range(num_letters):
            if (guess_letter) == list_picked_word[i]:
                newlist[i] = (guess_letter)
                #print ("newlist", newlist) ## debugging
                print ("".join(newlist))
                i +=1
            else:
                pass
                i += 1
        if guess_letter in newlist:
            wrong_guesses = wrong_guesses
            print ("wrong guesses left=", wrong_guesses)
            print ("".join(newlist))
            matching(list_picked_word, num_letters, newlist,wrong_guesses)
        elif guess_letter not in newlist:
            #to remind wrong letters played so far
            wrong_letters.append(guess_letter)
            print ("wrong guesses so far", set(wrong_letters))
            #reminder for wrong guesses left
            wrong_guesses -= 1
            print ("wrong guesses left=", wrong_guesses)
            print ("".join(newlist))
            if wrong_guesses == 0:
                print ("No. of guesses used up. Word=", "".join(list_picked_word))
            else:
                matching(list_picked_word, num_letters, newlist,wrong_guesses)


#playing the game:
matching(list_picked_word, num_letters, newlist, 6)

