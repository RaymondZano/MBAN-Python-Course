#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 18:20:30 2018

@author: chase.kusterer

Working Directory:
/Users/chase.kusterer/Desktop/PyCourse

Purpose:
This is a case study designed to practice list operations

"""


###############################################################################
## Activity Part 1: F&B for Winter Ball
###############################################################################

"""
Megan Moose is planning the food and beverage for the Winter Ball. So far
she has four items on her list.
"""


chips = 50
salsa = 25
still_water = 100
sparkling_water = 100


winter_ball = [['bags of chips', 50],
               ['jars of salsa', 25],
               ['liters still water', 25],
               ['liters sparkling water', 25]]


winter_ball[1]


food = winter_ball[0:2]
beverage = winter_ball[2:]

print(food)
print(beverage)



###############################################################################
## Activity Part 2: Adding Items to the F&B List
###############################################################################

"""
Megan receives an email asking her to add the following items to the
list:
    * 2 cans of ground coffee
    * 40 bottles of red wine
    * 40 bottles of white wine
    * enough salad for 300 people, which she assumes is 1 kilogram for
      every 8 people

She needs to insert the items so that all food is at the beginning of
the list, and all beverages are at the end of the list.

"""


print(winter_ball)

# Inserting foods at the beginning of the list

""" Use this space to finish append the rest of the beverages."""
winter_ball.append(['coffee',2])
winter_ball.append(['red wine',40])
winter_ball.append(['white wine',40])
# Inserting beverages at the end of the list
winter_ball.append(['bottles red wine', 40])



""" Use this space to finish append the rest of the beverages."""

"""
Note: If you accidentally add an item in the wrong place, remember
      that you can delete that item using 'del'
"""
winter_ball.insert(0,['salad',300/8])


###############################################################################
## Activity Part 3: Changing Quantities in our List
###############################################################################

"""
Megan receives an email requesting that we change:
    * the amount of salsa to 50 jars
    * the number of bottles of red wine to 50
    * the number of bottles of white wine to 30

Please help her to do so.
"""


# Let's start by making a new list so we can do back if we make a
# mistake
winter_ball_2 = winter_ball

print(winter_ball_2)



# Changing quantities
print(winter_ball_2[2])
print(winter_ball_2[2][1])


winter_ball_2[2][1] = 50


""" Use this space to finish inserting the rest of the beverages."""

print(winter_ball_2)



###############################################################################
## Activity Part 4: Adding Even More Items to the List
###############################################################################

"""
After completing the list, Megan receives another email stating that we
need to add five more foods and three more beverages to the list. Please
help her to do so.

"""


""" Use this space to finish insert or append the rest of the foods.
    Remember, foods go at the beginning of the list and beverages go
    at the end of the list."""



###############################################################################
## Activity Part 5: Our Final F&B List
###############################################################################

print(f"""
Our list is completed! Here are the food/beverages and their quantities:
    {winter_ball_2[0][0]} : {winter_ball_2[0][1]}
    {winter_ball_2[1][0]} : {winter_ball_2[1][1]} 
    {winter_ball_2[2][0]} : {winter_ball_2[2][1]} 
    {winter_ball_2[3][0]} : {winter_ball_2[3][1]} 
    {winter_ball_2[4][0]} : {winter_ball_2[4][1]} 
    {winter_ball_2[5][0]} : {winter_ball_2[5][1]}  
""")

""" Adjust this list with the foods/beverages you have added."""



###############################################################################
## Bonus Material
###############################################################################

"""
Prof Chase:
    Lists may be confusing, but they are the backbone of Python data
    structures. If we take our winter_ball_2 dataset one step further
    using the DataFrame function from the pandas library, we get
    something that should look incredibly similar if you are an Excel
    user.
    
"""    

import pandas as pd

winter_ball_df = pd.DataFrame(winter_ball_2)
winter_ball_df.to_excel("Winter_Ball_List.xlsx",
                        header = False,
                        index = False)