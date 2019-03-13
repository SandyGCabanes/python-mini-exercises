#sandygcabanes
#practicepython.org
#exercise 24 draw a game board with n x n dimensions
"""Draw A Game Board
Exercise 24 (and Solution)
This exercise is Part 1 of 4 of the Tic Tac Toe exercise series.
The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look
like this:

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes
(8x8 for chess, 19x19 for Go, and many more).
Ask the user what size game board they want to draw, and draw it for them to
the screen using Python’s print statement.
Remember that in Python 3, printing to the screen is accomplished by
  print("Thing to show on screen")
Hint: this requires some use of functions, as were discussed previously on
this blog and elsewhere on the Internet, like this TutorialsPoint link.
"""

import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

print ("draw a game board")
dim =  input(str("Input dimensions of board n x n, with n="))
print ("You wanted a board with dimensions:", dim, "x", dim)

# defining the board dimensions
def board(dimensions):
    i = 1
    dimensions = int(dimensions)
    while i<dimensions+1:
        print (" ---" *dimensions)
        print("|   "*(dimensions+1))
        i += 1
    print (" ---" *dimensions)

print ("Your board:")
board(dim)
