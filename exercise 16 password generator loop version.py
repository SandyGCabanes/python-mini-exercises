#sandygcabanes
#practicepython.org
#exercise 16 password generator
"""Password Generator
Exercise 16 (and Solution)
Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters,
uppercase letters, numbers, and symbols. The passwords should be random,
generating a new password every time the user asks for a new password.
Include your run-time code in a main method.
Extra:
Ask the user how strong they want their password to be.
For weak passwords, pick a word or two from a list.
you will need to use Python’s random module
"""

lenpw = int(input ("Password generator:" + "\n" + "Longer password = stronger password." + "\n" +  "How many characters?"))

alphalow = "abcdefghijklmnopqrstuvwxyz"
alphacap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeric = "1234567890"
symbols =  "!@#$%^&*"

import random

def makepw(length):
    passwd = ""
    for i in range(length):
        choices = str(alphalow + alphacap + numeric + symbols)
        passwd +=  random.choice(choices)
    print(passwd)

makepw(lenpw)















