#sandygcabanes
#practicepython.org
#exercise 25 guessing game two
"""Guessing Game Two
Exercise 25 (and Solution)
In a previous exercise, we’ve written a program that “knows” a number and asks
a user to guess it. This time, we’re going to do exactly the opposite. You,
the user, will have in your head a number between 0 and 100. The program will
guess a number, and you, the user, will say whether it is too high, too low,
or your number.
At the end of this exchange, your program should print out how many guesses
it took to get your number.
As the writer of this program, you will have to choose how your program will
strategically guess. A naive strategy can be to simply start the guessing at 1,
and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an
optimal guessing strategy. An alternate strategy might be to guess 50
(right in the middle of the range), and then increase / decrease by 1 as needed.
After you’ve written the program, try to find the optimal strategy!
(We’ll talk about what is the optimal one next week with the solution.)
"""
import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

print ("Computer to guess number between 1 and 100")
n = int(input("Enter number computer will guess:"))  # n = number to guess
print ("n=", n)  # check

guess = 50
print ("computer guess=", guess)
inp =input("Enter H if number is higher than guess. \n Enter L if number is lower than guess. \n  Enter C if guess is correct. H/L/C")

def game_function(inp, a, b):
    i = 1
    a = a -1
    b = b +1
    guess = round(int((a+b)/2))
    while inp == "h" or inp == "l":
        if inp == "h":
            #print ("inp=", inp)
            a = int(guess)
            b = b
            #print ("i=", i, "n>guess loop")
        elif inp == "l":
            #print ("inp=", inp)
            a = a
            b = int(guess)
            #print ("i=", i , "n<guess loop")
        guess = int((a+b)/2)
        print ("computer guess=", guess)
        inp =input("Enter H if number is higher than guess. \n Enter L if number is lower than guess. \n  Enter C if guess is correct. H/L/C")
        i = i + 1
    if inp == "c":
        print ("Computer guessed after {} tries. n = {}".format (str(i), str(n)))

game_function(inp, 1, 100)


