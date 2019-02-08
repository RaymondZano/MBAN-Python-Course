#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 09:16:59 2018

@author: chase.kusterer

Working Directory:
/Users/chase.kusterer/Desktop/PyCourse
    
Purpose:
This script is a case study on functions.
"""

"""
Anticipating that there may be many requests to add items to the Winter
Ball list, Megan Moose is in need of a solution. Help her to design a
function that adds foods to the beginning of the list, and beverages
to the end of the list.
"""

###################
# Starting with a simple function
###################

winter_ball = [['kilograms of salad', 37.5],
               ['bags of chips', 50],
               ['jars of salsa', 50],
               ['liters still water', 25],
               ['liters sparkling water', 25],
               ['cans of ground coffee', 2],
               ['bottles red wine', 50],
               ['bottles white wine', 30]]



"""
Define a function that takes two required arguments (item and amt) and
one optional argument (lst), which has a default value of an empty list.
"""
    
def list_maker(item, qty, lst = []):
    """ This function updates an item or
    appends new item to the Winter Ball menu."""
    
    lst.append([str(item), int(qty)])
    
    return lst



""" Add 25 liters of orange juice to the list """
list_maker(item = 'orange juice',
           qty = 25,
           lst = winter_ball)



""" Add 25 liters of apple juice to the list """
list_maker(item = 'apple juice',
           qty = 25,
           lst = winter_ball)



###################
# Enhancing our situation to fit with the original requirements
###################

"""
Enhance the function so that foods are inserted at the beginning of the
function and beverages are appended at the end of the function.
"""

def list_maker(item, qty, lst=[], food = True):
    """ This function _________  """
    
    if food == True:
        lst.insert(0, [item, qty,['food','dessert',]])
        return lst

    elif food == False:
        lst.append([item, qty],'beverage')
        return lst

    else:
        print("Food must be True or False.")



""" Add 125 bunches of grapes to the list """
list_maker(item = _________,
           qty = _________,
           food = _________,
           lst = _________)


""" Add 50 bunches of bananas to the list """




""" Add 35 liters of tomato juice to the list """




""" Add 30 cantaloupes to the list """




# Check to see that your list is complete
print(winter_ball)

print(f"""
Our list is completed! Here are the food/beverages and their quantities:
    {winter_ball[0][0]} : {winter_ball[0][1]}
    {winter_ball[1][0]} : {winter_ball[1][1]} 
    {winter_ball[2][0]} : {winter_ball[2][1]} 
    {winter_ball[3][0]} : {winter_ball[3][1]} 
    {winter_ball[4][0]} : {winter_ball[4][1]} 
    {winter_ball[5][0]} : {winter_ball[5][1]}
    {winter_ball[6][0]} : {winter_ball[6][1]}
    {winter_ball[7][0]} : {winter_ball[7][1]} 
    {winter_ball[8][0]} : {winter_ball[8][1]} 
    {winter_ball[9][0]} : {winter_ball[9][1]} 
    {winter_ball[10][0]} : {winter_ball[10][1]} 
    {winter_ball[11][0]} : {winter_ball[11][1]}  
    {winter_ball[12][0]} : {winter_ball[12][1]} 
    {winter_ball[13][0]} : {winter_ball[13][1]} 
""")

