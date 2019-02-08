#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 13:12:01 2018

@author: chase.kusterer

Working Directory:
/Users/chase.kusterer/Desktop/PyCourse
    
Purpose:
A case to get practice using while loops.
"""

"""
Recipe:
    3 eggs
    ½ cup of cheese
    1 slice of Spam

Inventory:
    144 eggs
    93 cups of cheese
    65 slices of Spam

Question 1: How many omelettes can we make?
Question 2: How many of each ingredient will we have left over?
"""


# Let's start with assigning our variables
eggs    = 144
cheese  = 93
spam    = 65

omelettes = 0


"""
This is a while loop that does two things:
    1) Takes away ingredients for each omelette created
    2) Adds to the omelette total
"""
 
while eggs >= 3 and cheese >= .5 and spam >= 1:
    eggs -= 3
    cheese -= .5
    spam -= 1
    omelettes = omelettes + 1

print(f"You can make a total of {omelettes} omelettes. \n")



# Some conditional statements for the remaining goods.
if eggs > 0:
    print(f"You have a total of {eggs} eggs remaining. \n")
else:
    print("You have run out of eggs. \n")

if cheese > 0:
    print(f"You have a total of {cheese} cups of cheese remaining. \n")
else:
    print("You have run out of cheese. \n")

if spam > 0:
    print(f"You have a total of {spam} cups of spam remaining. \n")
else:
    print("You have run out of spam. \n")



# Making an input for buying more eggs. This could be extended to other
# ingredients as well
print("Would you like to buy more eggs? \n")
buy_eggs = input("1 for Yes, 2 for No: ")



# Making a new variable called new_omelettes
new_omelettes = 0


if buy_eggs == "1":
    more_eggs = int(input("How many more eggs would you like to buy? "))
    eggs = eggs + more_eggs

    # Running the for loop again with an adjustment for new omelettes
    while eggs >= 3 and cheese >= .5 and spam >= 1:
        eggs -= 3
        cheese -= .5
        spam -= 1
        new_omelettes = new_omelettes + 1
        omelettes = omelettes + new_omelettes


print(f"Now you can make a total of {omelettes} omelettes. \n")
print(f"That's {new_omelettes} more! I hope you're hungry! \n")



# Our conditional goods checks again.
if eggs >= 0:
    print(f"You have a total of {eggs} eggs remaining. \n")
else:
    print("You have run out of eggs. \n")

if cheese >= 0:
    print(f"You have a total of {cheese} cups of cheese remaining. \n")
else:
    print("You have run out of cheese. \n")

if spam >= 0:
    print(f"You have a total of {spam} cups of spam remaining. \n")
else:
    print("You have run out of spam. \n")
