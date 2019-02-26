#sandygcabanes
#practicepython.org
#exercise 09 guessing game one
"""Guessing Game One
Exercise 9 (and Solution)
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they
guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken,
and when the game ends, print this out.
"""

import random

play = str(input("Play guessing game? Type Y or type exit:"))
if play == "exit":
    print ("End of game. You have played 0 times.")
else:
    i = 1
    while play != "exit":
        player = int (input ("Type in your number guess, between 1 and 9:"))
        num = random.randint(1,9)
        if player == num:
            print ("Congratulations! Your guess is right!")
        else:
            if player < num:
                print ("Answer is {}. You guessed too low.".format(num))
            elif player > num:
                print ("Answer is {}. You guessed too high.".format(num))
        play = str(input("Play again? Type Y or type exit:"))
        if play == "exit":
            print ("You have played {} time/s".format(i))
            print ("End of game.")
        else:
            i += 1






