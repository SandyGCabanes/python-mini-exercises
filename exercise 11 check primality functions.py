#sandygcabanes
#practicepython.org
#exercise 11 check primality functions
"""Check Primality Functions
Exercise 11 (and Solution)
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.)
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
"""

a = int(input("Type in any whole number: "))

def prime_number (num):
  divisor = 2
  list_divisors = []
  while divisor < num :
      if num % divisor == 0 :
          list_divisors.append (divisor)
      elif num % divisor >0 :
          pass
      divisor += 1

  if list_divisors == []:
      print ("Number {} is a prime number.". format(num))
  else:
      print ("Number {} has the following divisor/s:".format(num))
      print (list_divisors)

prime_number(a)






