#sandygcabanes
#practicepython.org
#exercise 32 hangman with additions
"""
Hangman
Exercise 32 (and Solution)
This exercise is Part 3 of 3 of the Hangman exercise series.
The other exercises are: Part 1 and Part 2.
You can start your Python journey anywhere, but to finish this exercise you will
have to have finished Parts 1 and 2 or use the solutions (Part 1 and Part 2).
In this exercise, we will finish building Hangman. In the game of Hangman, the
player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before
they lose the game.
In Part 1, we loaded a random word list and picked a word from it. In Part 2,
we wrote the logic for guessing the letter and displaying that information to
the user. In this exercise, we have to put it all together and add logic for
handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point.
Now add the following features:

Only let the user guess 6 times, and tell the user how many guesses they
have left. Keep track of the letters the user guessed. If the user guesses a
letter they already guessed, don’t penalize them - let them guess again.
Optional additions:
When the player wins or loses, let them start a new game.
Rather than telling the user "You have 4 incorrect guesses left", display some
picture art for the Hangman. This is challenging - do the other parts of the
exercise first!
Your solution will be a lot cleaner if you make use of functions to help you!

I'm adding level of difficulty aside from above for debugging purposes.
"""
#using C:/Users/sandy/Desktop/data_copies/sowpods.txt  2906kb
#print ("sowpods.txt")
import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

# create new motherlist from text file: listlines containing all the words
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

"""setting up the list of wrong letters guessed so far"""
wrong_letters = []

#picking the word out of the list
def picking_word(numlines):
    import random
    index_word= random.randint(1, numlines)
    picked_word = listwords[index_word]
    list_picked_word = list(picked_word)
    return list_picked_word

    num_letters =len(list_picked_word)
    print("picked_word", picked_word)    ##debugging, will be hashed on actual play

def clue(num_letters):
    """creating the blanks or clue to be shown to gamer"""
    newlist = []
    for i in range(num_letters):
        newlist.append("_ ")
    print("".join(newlist))
    return newlist


def guess_turn():
    """function to be called within matching function"""
    guess_l = str(input("Guess your letter:"))
    guess_l = guess_l.upper()
    return guess_l



"""image showing function"""
def showhm(guesses_left):
    from PIL import Image
    if guesses_left == 6:
        image = Image.open('C:/Users/sandy/Desktop/data_copies/hm7.jpg')
        image.show ()
    if guesses_left == 5:
        image = Image.open('C:/Users/sandy/Desktop/data_copies/hm6.jpg')
        image.show ()
    if guesses_left == 4:
        image = Image.open('C:/Users/sandy/Desktop/data_copies/hm5.jpg')
        image.show ()
    if guesses_left == 3:
        image = Image.open('C:/Users/sandy/Desktop/data_copies/hm4.jpg')
        image.show ()
    if guesses_left == 2:
        image = Image.open('C:/Users/sandy/Desktop/data_copies/hm3.jpg')
        image.show ()
    if guesses_left == 1:
        image = Image.open('C:/Users/sandy/Desktop/data_copies/hm2.jpg')
        image.show ()
    if guesses_left == 0:
        image = Image.open('C:/Users/sandy/Desktop/data_copies/hm1.jpg')
        image.show ()

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
            showhm(wrong_guesses)
            print ("wrong guesses left=", wrong_guesses)
            print ("".join(newlist))
            matching(list_picked_word, num_letters, newlist,wrong_guesses)
        elif guess_letter not in newlist:
            #to remind wrong letters played so far
            wrong_letters.append(guess_letter)
            print ("wrong guesses so far", set(wrong_letters))
            #reminder for wrong guesses left
            wrong_guesses -= 1
            showhm(wrong_guesses)
            print ("wrong guesses left=", wrong_guesses)
            print ("".join(newlist))
            if wrong_guesses == 0:
                print ("No. of guesses used up. Word=", "".join(list_picked_word))
            else:
                matching(list_picked_word, num_letters, newlist,wrong_guesses)


#playing the game:
picking_word(numlines)
list_picked_word = picking_word(numlines)           # argument for matching ()
num_letters =len(list_picked_word)                  # argument for matching ()
newlist = clue(num_letters)                         # argument for matching ()
matching(list_picked_word, num_letters, newlist, 6)

start_again= input("Start a new game? Y/N")
start_again= start_again.upper()

if start_again == "Y":
    print("Welcome back to Hangman!  Choose your level of difficulty.")
    level = str(input("Choose from 1-easy, 2-medium, 3-hard, 4-any: "))
    difficulty(level, listlines)              #returns childlist from motherlist
    listwords = difficulty(level, listlines)  #assign childlist to listwords
    numlines = len(listwords)                 #argument for picking_word ()
    wrong_letters = []                        # reset list of wrong letters
    list_picked_word = picking_word(numlines) # argument for matching ()
    num_letters =len(list_picked_word)        # argument for matching ()
    newlist = clue(num_letters)               # argument for matching ()
    matching(list_picked_word, num_letters, newlist, 6)
else:
    pass


