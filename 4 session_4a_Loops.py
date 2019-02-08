#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 13:12:01 2018

@author: chase.kusterer

Working Directory:
/Users/chase.kusterer/Desktop/PyCourse
    
Purpose:
To supplement the loop content.

World Cup Results Source:
https://en.wikipedia.org/wiki/Argentina_at_the_FIFA_World_Cup
"""

###############################################################################
## for Loops
###############################################################################

lst = ['a', 'b', 'c', 'd', 'e']


# Printing the list
print(lst)


# Printing each element in lst
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])


print(lst[0], lst[1], lst[2], lst[3], lst[4])


# Looping each element in list
for element in lst:
    
    print(element)



# Looping with breaks
lst = [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]



# Looping each element in list
for element in lst:
    
    print(element)
    
    if element == 0:
        break



# Don't want the zero, try running your code like this:
for element in lst:

    if element == 0:
        break
    
    print(element)
    



###############################################################################
## while Loops
###############################################################################

x = 5

while x > 1:
    print(x)
    x = x - 1



# The above could alternatively be written like this:
x = 5

while x > 1:
    print(x)
    x -= 1



# Don't do this:
x = 5

while x > 1:
    print(x)

"""
Prof. Chase:
    If you accidentally create an infinite loop, press the red square to
    terminate the code, or press control + C
"""


# Liftoff Countdown

count = 10

while count > 0:
    print(count)
    count -= 1
    input("< Press ENTER to continue. >\n")

print("LIFTOFF!")



# Nested While Loops
x = 5
y = 10

while x > 0:
    while y > 0:
        print(x)
        print(y)
        
        x -= 1
        y -= 2


"""
Prof. Chase:
    The above example is simply to show that we can nest loops. We will
    not be going into great detail on this, and they are not a graded
    component of our course.
"""



# Example: Coffee and Customers

cups_of_coffee = 25
people      = 20

while cups_of_coffee  > 0 and people > 0:
        cups_of_coffee -= 1
        people -= 1


print(f"You have {cups_of_coffee} cups of coffee remaining.")
print(f"You have {people} people still waiting for coffee.")




# Enhanced Example: Coffee and Customers

cups_of_coffee = 25
people         = 20

while cups_of_coffee  > 0 and people > 0:
        cups_of_coffee -= 1
        people -= 1


if cups_of_coffee == 0 and people > 0:
    print(f"You have run out of coffee and {people} are still waiting.")

elif cups_of_coffee > 0 and people == 0:
    print(f"You have {cups_of_coffee} cups of coffee remaining.")

else:
    print("Something went wrong.")



# While loops with conditional statements


"""
Guess a number between 1 and 10. You have three chances.
"""


import random

number = random.randint(1,10)
guesses = 3

# Looping each element in list
while guesses > 0:
    print("\n What is your guess (1-10)?")
    
    choice = int(input("> "))

    if choice == number:
        print("\nYou win!")
        break
    
    elif choice != number:
        print("\nThat's incorrect, please guess again.")
        guesses -= 1

    else:
        print("\nSomething went wrong.")


print(f"\nYou are out of guesses. The number was {number}.")


# Refining the code

import random

number = random.randint(1,10)
guesses = 3



# Looping each element in list
while guesses > 0:
    print("\n What is your guess (1-10)?")
    
    choice = int(input("> "))

    if choice == number:
        print("\nYou win!")
        break
    
    elif choice != number:
        guesses -= 1
        
        if guesses == 0:
            print(f"\nYou are out of guesses. The number was {number}.")

        elif guesses >0:
            print(f"\nThat's incorrect, please guess again. You have {guesses} guesses remaining.")

    else:
        print("\nSomething went wrong.")


