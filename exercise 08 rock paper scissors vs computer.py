#sandygcabanes
#practicepython.org
#exercise 08 rock paper scissors vs computer
"""Exercise 8 (and Solution)
Make a Rock-Paper-Scissors game vs computer. (Hint: Ask for player play
(using input), compare with computer, print out a message of congratulations
to the winner, and ask if the player wants to start a new game.)
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
        print ("Congratulations! You win!")
    elif player_ == "R" and computer_ == "P":
        print ("Sorry! You lose.")
    elif player_ == "S" and computer_ =="P":
        print ("Congratulations! You win!")
    elif player_ == "S" and computer_ == "R":
        print ("Sorry! You lose.")
    elif player_ == "P" and computer_ =="R":
        print ("Congratulations! You win!")
    elif player_ == "P" and computer_ == "S":
        print ("Sorry! You lose.")

    play = input("Try again? Y/N")

print ("End of game")