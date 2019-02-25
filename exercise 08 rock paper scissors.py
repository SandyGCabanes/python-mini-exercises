#sandygcabanes
#practicepython.org
#exercise 08 rock paper scissors
"""Exercise 8 (and Solution)
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
(using input), compare them, print out a message of congratulations
to the winner, and ask if the players want to start a new game)
Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock
"""

play = str(input("Play Rock Paper Scissors? Y/N"))
import random
while play == "Y":

    player_ = str(input("Type R for Rock, P for Paper, S for Scissors"))
    choices = ["R", "P", "S"]
    computer_ = str(random.choice(choices))
    print ("Your choice = {}. Computer choice = {}.".format(player_, computer_))

    if player_ == computer_:
        print ("It's a tie!")
    elif player_ == "R" and computer_ =="S":
        print ("You win!")
    elif player_ == "R" and computer_ == "P":
        print ("You lose!")
    elif player_ == "S" and computer_ =="P":
        print ("You win!")
    elif player_ == "S" and computer_ == "R":
        print ("You lose!")
    elif player_ == "P" and computer_ =="R":
        print ("You win!")
    elif player_ == "P" and computer_ == "S":
        print ("You lose!")

    play = input("Try again? Y/N")

print ("End of game")