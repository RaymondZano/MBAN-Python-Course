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
## Argentina in the World Cup
###############################################################################

# Argentina in the World Cup
ARG_wrld_cup = [2, 9, 'WD', 'WD', 'WD', 13, 10, 5, 'DNQ', 8,
                1, 11, 1, 2, 10, 6, 18, 6, 5, 2, 16]



# How did Argentina place in each World Cup leading up to their first
# championship?
for place in ARG_wrld_cup:
    
    print(place)
    
    if place == 1:
        break



# How many world cups is that?
lst = []

for place in ARG_wrld_cup:
    lst.append(place)
    
    if place == 1:
        print(len(lst))
        break


# What about world cups that they played in?

# Step 1: Performance to first championship (played)
for place in ARG_wrld_cup:

    if type(place) == int:
        print(place)


# Step 2: Performance to first championship (played)
        
for place in ARG_wrld_cup:
    
    if type(place) == int:
        print(place)
        
        if place == 1:
            break



# Number of world cups (played)
lst = []

for place in ARG_wrld_cup:
    
    if type(place) == int:
        lst.append(place)
        
        if place == 1:
            print(len(lst))
            break


"""
Summary:
    Argentina appeared in in 7 of the 11 World Cups leading up to
    their first championship.
    
    They withdrew three times and did not qualify one time.

"""



"""
Now let's compare Argentina with their rival Brazil.
"""

###############################################################################
## Argentina v. Brazil in World Cup
###############################################################################

# Brazil World Cup Data
BZL_wrld_cup = [6, 14, 3, 2, 5, 1, 1, 11, 1, 4, 3, 5, 5, 9,
                1, 2, 1, 5, 6, 4, 6]
ARG_wrld_cup = [2, 9, 'WD', 'WD', 'WD', 13, 10, 5, 'DNQ', 8,
                1, 11, 1, 2, 10, 6, 18, 6, 5, 2, 16]


# Building a DataFrame of Argentina and Brazil data
import pandas as pd


# Creating a disctionary below so that the pd.DataFrame
# has column names
rivals = pd.DataFrame({'ARG' : ARG_wrld_cup,
                       'BZL' : BZL_wrld_cup})



# Analyzing different aspects of the DataFrame
rivals.shape

print(rivals)

rivals.values

rivals.mean()
rivals.std()
rivals.head()



# No ARG because it's not numeric
rivals.describe()




# Let's drop the observations where Argentina did not play
rivals = rivals.drop([2, 3, 4, 8])




# Now let's change the column ARG to numeric
rivals['ARG'] = pd.to_numeric(rivals['ARG'])

rivals.describe()



# Let's make a calculation to see which team placed higher
# each World Cup
rivals['Diff'] = (rivals['ARG'] - rivals['BZL'])



# Step 1: Simple for loop to make sure we are iterating over the proper values
for val in rivals['Diff']:
    print(val)



# Step 2: Adapting the loop so that it does what it's intended to do
ARG_on_top = []

for val in rivals['Diff']:
    
    if val < 0:
        ARG_on_top.append(val)
     

# How many times has Argentina placed higher than Brazil in the World Cup?
print(len(ARG_on_top))


# What percentage is that?
print(len(ARG_on_top) / 
      len(rivals['Diff']))

ARG_win_pct = round(
        len(ARG_on_top) /
        len(rivals['Diff']
        ), 2)


print(f"""
Summary:
    Argentina places higher than their rival, Brazil, in nearly half
    of all the World Cups both teams have played in ({ARG_win_pct * 100}%).
    
    This statistic comes after {len(rivals['Diff'])} World Cups, where
    Argentina came out on top {len(ARG_on_top)} times and Brazil came
    out on top {len(rivals['Diff']) - len(ARG_on_top)} times.
    
    Let's see if Argentina can tie things up in 2022!

""")
