#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 18:11:26 2018

@author: chase.kusterer

Working Directory:
/Users/chase.kusterer/Desktop/PyCourse

Purpose:
    To introduce pandas and matplotlib
"""

###############################################################################
# Importing libraries and base dataset
###############################################################################

import pandas as pd


# Checking the arguments for pd.to_numeric()
pd.to_numeric()



# Testing pd.to_numeric()
x = '7.9484141'

pd.to_numeric(x)

print(x)



# Checking the documentation on pd.datetools()
help(pd.datetools)



# Testing pd.cut()
x = range(100)

y = pd.cut(x, 5)

print(y)

print(pd.value_counts(y))


###############################################################################
# matplotlib Essentials
###############################################################################

import pandas as pd
import matplotlib.pyplot as plt

file ='diamonds_missing_values.xlsx'
diamonds = pd.read_excel(file)



plt.hist(x = 'price',
         data = diamonds)#lazy printing - not shown immediately, need to call 
                         #plt.show()
plt.hist(x = 'carat',
         data = diamonds)#another column name from file


plt.show()

plt.hist(x = 'price',
         data = diamonds,
         bins = 15,
         normed = True)

plt.show()

plt.hist(x = 'price',
         data = diamonds,
         bins = 150,
         normed = True)

plt.show()



plt.hist(x = 'price',
         data = diamonds,
         bins = 150,
         normed = True)

plt.show()


# Finding the optimal number of bins with the
# Freedman-Diaconis rule

iqr_max = pd.np.percentile(diamonds['price'], [75])

iqr_min = pd.np.percentile(diamonds['price'], [25])

iqr_price = float(iqr_max - iqr_min)

h = 2 * iqr_price * (len(diamonds['price']) ** -(1/3))

price_range = max(diamonds['price']) - min(diamonds['price'])

print(price_range / h)


plt.hist(x = 'price',
         data = diamonds,
         bins = 21,
         normed = True)

"""
Prof. Chase:
    The Freedman-Diaconis rule can be cumbersome if done manually in
    Python. Luckily, it is built into plt.hist as an option for bins.
    This is one of the major advantages of open source communities.
"""

plt.hist(x = 'price',
         data = diamonds,
         bins = 'fd',
         normed = True)#fd is freedman-diaconis, best form of data, optimized



# Scatterplot example
plt.scatter(x = 'carat',
            y = 'price',
            data = diamonds)


plt.xlabel('Carat Weight')
plt.ylabel('Price')

plt.axhline(y = 25000)
plt.axvline(x = 1)#vertical line
plt.axvline()


plt.show()
