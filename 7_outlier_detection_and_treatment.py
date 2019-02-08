#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 11:17:09 2018

@author: chase.kusterer

Working Directory:
/Users/chase.kusterer/Desktop/PyCourse

Purpose:
    To introduce outlier detection and treatment.
"""


###############################################################################
# Importing libraries and base dataset
###############################################################################
import pandas as pd # data science essentials
import matplotlib.pyplot as plt # data visualization
import seaborn as sns # more data visualization

file ='diamonds_imputed.xlsx'
diamonds = pd.read_excel(file)



###############################################################################
# Quantile Analysis
###############################################################################

# By default, .quantile() gives the 50th percentile (a.k.a. the median)
diamonds['price'].quantile()



# Additional percentiles can be accessed by passing a list
print(
diamonds['price'].quantile([0.00,
                            0.20,
                            0.40,
                            0.50,
                            0.60,
                            0.80,
                            1.00])     
)


# We can also pass multiple variables using a list
print( 
diamonds[['carat',
          'color',
          'clarity',
          'cut',
          'price']].quantile([0.20,
                              0.40,
                              0.60,
                              0.80,
                              1.00])
)


    
###############################################################################
# Boxplots and Histograms
###############################################################################

diamonds.boxplot(column = ['price'])

plt.show()



diamonds.boxplot(column = ['carat', 'color', 'clarity', 'cut'],
                 vert = False,
                 manage_xticks = True,
                 patch_artist = False,
                 meanline = True,
                 showmeans = True,
                 )


plt.title("Boxplots for Carat, Color, Clarity, and Cut")

plt.show()


    
###############################################################################
# seaborn
###############################################################################

# Basic histogram with sns.distplot
sns.distplot(diamonds['price'])

plt.show()



# Histogram with vertical line with sns.distplot
sns.distplot(diamonds['price'])

plt.axvline(x = 15000,
            label = 'Outlier Thresholds')

plt.show()



###############################################################################
# Enumeration
###############################################################################


for val in enumerate(diamonds):
    print(val)



for val in enumerate(diamonds.loc[ : , 'price']):
    print(val)



for val in enumerate(diamonds.loc[ : , 'price']):
    
    if val[1] > 15000:
        print(val)



for val in enumerate(diamonds.loc[ : , 'price']):
    
    if val[1] > 15000:
        print(val[0])



###############################################################################
# Advanced Outlier Flagging
###############################################################################

diamonds['out_price'] = 0


for val in enumerate(diamonds.loc[ : , 'price']):
    
    if val[1] > 15000:
        diamonds.loc[val[0], 'out_price'] = 1


diamonds['out_price']
