#sandygcabanes
#practicepython.org
#exercise 29 tic tac toe game
"""Tic Tac Toe Game
Exercise 29 (and Solution)
This exercise is Part 4 of 4 of the Tic Tac Toe exercise series.
The other exercises are: Part 1, Part 2, and Part 3.

In 3 previous exercises, we built up a few components needed to build a
Tic Tac Toe game in Python:

Draw the Tic Tac Toe game board
Checking whether a game board has a winner
Handle a player move from user input
The next step is to put all these three components together to make a
two-player Tic Tac Toe game! Your challenge in this exercise is to use the
functions from those previous exercises all together in the same program
to make a two-player game that you can play with a friend. There are a lot of
choices you will have to make when completing this exercise, so you can go as
far or as little as you want with it.

Here are a few things to keep in mind:

a) You should keep track of who won - if there is a winner, show a congratulatory
message on the screen.
b) If there are no more moves left, don’t ask for the next player’s move!
c) As a bonus, you can ask the players if they want to play again and keep a
running tally of who won more - Player 1 or Player 2.
"""


import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

print ("Tic Tac Toe Game. Player 1 starts. \n")

game = [['0', '0', '0'],
        ['0', '0', '0'],
        ['0', '0', '0']]

def gameboard():
    print (" ---" *3)
    print ("| " + (game[0][0]) + " | " + (game[0][1]) + " | " + (game[0][2]) + " |")
    print (" ---" *3)
    print ("| " + (game[1][0]) + " | " + (game[1][1]) + " | " + (game[1][2]) + " |")
    print (" ---" *3)
    print ("| " + (game[2][0]) + " | " + (game[2][1]) + " | " + (game[2][2]) + " |")
    print (" ---" *3)

gameboard()

instruction= print("Please input row and column.")

def turn(player):
    print (player)
    row= input("First, input row= ")
    col= input("Next, input col= ")

    row = int(row)-1  #transform string input into index
    col = int(col)-1
    rowcol = [row, col]  #transform to list

    if game[row][col] == "x" or game[row][col] =="o":
        print("Already taken. Please try again.")
        turn(player)
    else:
        if player == "player1":
            game[row][col] = "x"
        elif player == "player2":
            game[row][col] = "o"
        gameboard()

turn("player1")
turn("player2")
turn("player1")
turn("player2")
turn("player1")
turn("player2")


print ("check tic tac toe")

def player1wins(matrix):
    """game is a list of 3 lists with 3 items each"""
    if ((game[0][0] == "x" and game[0][1] == "x" and game [0][2]=="x") or
        (game[1][0] == "x" and game[1][1] == "x" and game [1][2]=="x") or
        (game[2][0] == "x" and game[2][1] == "x" and game [2][2]== "x") or
        (game[0][0] == "x" and game[1][0] == "x" and game [2][0]== "x") or
        (game[0][1] == "x" and game[1][1] == "x" and game [2][1]== "x") or
        (game[0][2] == "x" and game[1][2] == "x" and game [2][2]== "x") or
        (game[0][0] == "x" and game[1][1] == "x" and game [2][2]== "x") or
        (game[0][2] == "x" and game[1][1] == "x" and game [2][0]== "x")):
        return True
    else:
        return False


def player2wins(game):
    """game is a list of 3 lists with 3 items each"""
    if ((game[0][0] == "o" and game[0][1] == "o" and game [0][2]== "o") or
        (game[1][0] == "o" and game[1][1] == "o" and game [1][2]== "o") or
        (game[2][0] == "o" and game[2][1] == "o" and game [2][2]== "o") or
        (game[0][0] == "o" and game[1][0] == "o" and game [2][0]== "o") or
        (game[0][1] == "o" and game[1][1] == "o" and game [2][1]== "o") or
        (game[0][2] == "o" and game[1][2] == "o" and game [2][2]== "o") or
        (game[0][0] == "o" and game[1][1] == "o" and game [2][2]== "o") or
        (game[0][2] == "o" and game[1][1] == "o" and game [2][0]== "o")):
        return True

    else:
        return False

def check_so_far(game):
    cond1 = player1wins(game)
    cond2 = player2wins(game)

    if ((cond1 == False) and
        (cond2 == False)):
        return False

    elif cond1 == True:
        print ("player 1 wins")
        return True
    elif cond2 == True:
        print ("player 2 wins")
        return True

def check_who_wins(game):
    cond1 = player1wins(game)
    cond2 = player2wins(game)

    if ((cond1 == False) and
        (cond2 == False)):
        print ("It's a tie.")

    elif cond1 == True:
        print ("player 1 wins")

    elif cond2 == True:
        print ("player 2 wins")

if check_so_far(game) == True:
    print ("End of game")
else:
    turn("player1")
    turn("player2")

check_who_wins(game)

