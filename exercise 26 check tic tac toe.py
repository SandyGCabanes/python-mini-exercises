#sandygcabanes
#practicepython.org
#exercise 26 check tic tac toe
"""Check Tic Tac Toe
Exercise 26 (and Solution)
This exercise is Part 2 of 4 of the Tic Tac Toe exercise series.
The other exercises are: Part 1, Part 3, and Part 4. As you may have guessed,
we are trying to build up to a full tic-tac-toe board. However, this is
significantly more than half an hour of coding, so we’re doing it in pieces.
Today, we will simply focus on checking whether someone has WON a game of
Tic Tac Toe, not worrying about how the moves were made.
If a game of Tic Tac Toe is represented as a list of lists, like so:
game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in
that space, and a 2 means that player 2 put their token in that space.
Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe
game board, tell me whether anyone has won, and tell me which player won,
if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or
a diagonal. Don’t worry about the case where TWO people have won - assume that
in every board there will only be one winner.

Here are some more examples to work with:

winner_is_2 = [[2, 2, 0],   [2, 1, 0],  [2, 1, 1]]
winner_is_1 = [[1, 2, 0],   [2, 1, 0],  [2, 1, 1]]
winner_is_also_1 = [[0, 1, 0],  [2, 1, 0],  [2, 1, 1]]
no_winner = [[1, 2, 0], [2, 1, 0],  [2, 1, 2]]
also_no_winner = [[1, 2, 0],    [2, 1, 0],  [2, 1, 0]]
"""

import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

print ("check tic tac toe")

def player1wins(matrix):
    """matrix is a list of 3 lists with 3 items each"""
    if ((matrix[0][0] == 1 and matrix[0][1] == 1 and matrix [0][2]==1) or
        (matrix[1][0] == 1 and matrix[1][1] == 1 and matrix [1][2]==1) or
        (matrix[2][0] == 1 and matrix[2][1] == 1 and matrix [2][2]==1) or
        (matrix[0][0] == 1 and matrix[1][0] == 1 and matrix [2][0]==1) or
        (matrix[0][1] == 1 and matrix[1][1] == 1 and matrix [2][1]==1) or
        (matrix[0][2] == 1 and matrix[1][2] == 1 and matrix [2][2]==1) or
        (matrix[0][0] == 1 and matrix[1][1] == 1 and matrix [2][2]==1) or
        (matrix[0][2] == 1 and matrix[1][1] == 1 and matrix [2][0]==1)):
            return True
    else:
        return False


def player2wins(matrix):
    """matrix is a list of 3 lists with 3 items each"""
    if ((matrix[0][0] == 2 and matrix[0][1] == 2 and matrix [0][2]==2) or
        (matrix[1][0] == 2 and matrix[1][1] == 2 and matrix [1][2]==2) or
        (matrix[2][0] == 2 and matrix[2][1] == 2 and matrix [2][2]==2) or
        (matrix[0][0] == 2 and matrix[1][0] == 2 and matrix [2][0]==2) or
        (matrix[0][1] == 2 and matrix[1][1] == 2 and matrix [2][1]==2) or
        (matrix[0][2] == 2 and matrix[1][2] == 2 and matrix [2][2]==2) or
        (matrix[0][0] == 2 and matrix[1][1] == 2 and matrix [2][2]==2) or
        (matrix[0][2] == 2 and matrix[1][1] == 2 and matrix [2][0]==2)):
            return True

    else:
        return False

def check_who_wins(matrix):
    cond1 = player1wins(matrix)
    cond2 = player2wins(matrix)

    if ((cond1 == False) and
        (cond2 == False)):
        print ("It's a tie.")

    elif cond1 == True:
        print ("player 1 wins")

    elif cond2 == True:
         print ("player 2 wins")

winner_is_2 = [[2, 2, 0],   [2, 1, 0],  [2, 1, 1]]
winner_is_1 = [[1, 2, 0],   [2, 1, 0],  [2, 1, 1]]
winner_is_also_1 = [[0, 1, 0],  [2, 1, 0],  [2, 1, 1]]
no_winner = [[1, 2, 0], [2, 1, 0],  [2, 1, 2]]
also_no_winner = [[1, 2, 0],    [2, 1, 0],  [2, 1, 0]]


print ("matrix = winner is 2")
check_who_wins(winner_is_2)


print ("matrix = winner_is_1")
check_who_wins(winner_is_1)


print ("matrix = winner_is_also_1")
check_who_wins(winner_is_also_1)


print ("matrix = no_winner")
check_who_wins(no_winner)


print ("matrix = also_no_winner")
check_who_wins(also_no_winner)


