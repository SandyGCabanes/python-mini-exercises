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

while play == "Y":

    player_1 = str(input("Player 1: Type R for Rock, P for Paper, S for Scissors"))
    choices = ["R", "P", "S"]
    player_2 = str(input("Player 2: Type R for Rock, P for Paper, S for Scissors"))
    print ("Player 1 = {}. Player 2= {}.".format(player_1, player_2))

    if player_1 == player_2:
        print ("It's a tie!")
    elif player_1 == "R" and player_2 =="S":
        print ("Congratulations Player 1! You win!")
    elif player_1 == "R" and player_2 == "P":
        print ("Congratulations Player 2! You win!")
    elif player_1 == "S" and player_2 =="P":
        print ("Congratulations Player 1! You win!")
    elif player_1 == "S" and player_2 == "R":
        print ("Congratulations Player 2! You win!")
    elif player_1 == "P" and player_2 =="R":
        print ("Congratulations Player 1! You win!")
    elif player_1 == "P" and player_2 == "S":
        print ("Congratulations Player 2! You win!")

    play = input("Play again? Y/N")

print ("End of game")