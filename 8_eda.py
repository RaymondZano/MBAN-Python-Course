#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:59:35 2018

@author: chase.kusterer

Working Directory:
/Users/chase.kusterer/Desktop/PyCourse

Purpose:
    This code is meant to explain the basics of exploratory
    data analysis(EDA)
"""

###############################################################################
# Importing libraries and base dataset
###############################################################################
import pandas as pd # data science essentials
import matplotlib.pyplot as plt # data visualization
import seaborn as sns # more data visualization

file ='diamonds_flagged.xlsx'
diamonds = pd.read_excel(file)

diamonds.values
diamonds.mean()
diamonds.head(10)
diamonds.shape
diamonds.describe()
diamonds.info()
diamonds.columns
diamonds.count()
diamonds.iloc[:,1:7]

###############################################################################
# Correlation analysis
###############################################################################

y = pd.np.corrcoef(diamonds['price'],
                   diamonds['carat']).round(2)

print(y)



y = pd.np.corrcoef(diamonds['price'],
               diamonds['carat'])[1,0].round(2)

print(y)



########################
# Correlation matricies
########################

df_corr = diamonds.corr().round(2)

print(df_corr)



print(
df_corr.loc['price'].sort_values(ascending = False)
)

#######################
# Heatmaps
#######################

sns.heatmap(df_corr,
            cmap = 'Blues',
            square = True,
            annot = False,
            linecolor = 'black',
            linewidths = 0.5)

plt.savefig('Diamond Correlation Heatmap.png')
plt.show()



# Using palplot to view a color scheme
sns.palplot(sns.color_palette('coolwarm', 12))


fig, ax = plt.subplots(figsize=(15,15))

sns.heatmap(df_corr,
            cmap = 'coolwarm',
            square = True,
            annot = True,
            linecolor = 'black',
            linewidths = 0.5,
            cbar = False)


plt.savefig('Diamond Correlation Heatmap 2.png')
plt.show()



########################
# Pairplots
########################

# let's pick up the pace with pairplot
sns.pairplot(diamonds)

plt.savefig('Pairplot Example 1.png')
plt.show()


# this can be further focused using subsetting
diamonds_sel = diamonds.loc[:,['price', 'carat', 'color', 'clarity', 'cut']]
sns.pairplot(data = diamonds_sel)
plt.tight_layout()

plt.savefig('Pairplot Example 2.png')
plt.show()

###############################################################################
# Do prices vary by store?
###############################################################################

sns.lmplot(x = 'carat',
           y = 'price',
           data = diamonds,
           fit_reg = False,
           hue= 'store',
           scatter_kws= {"marker": "D", 
                        "s": 30},
           palette = 'plasma')

plt.title("Price and Carat by Store")
plt.grid()
plt.tight_layout()
plt.show()

###############################################################################
# Categorical Data Mapping
###############################################################################

# Building a basic dictionary

alpha_num_dict = {'a' : 1, 
                  'b' : 2, 
                  'c' : 3}



print(
      alpha_num_dict['a']
)



# Using dictionaries to make new labels for categorical variables
diamonds['channel'] = diamonds['channel'].map(
        {0: 'mall',
         1: 'independent',
         2: 'online'})

print(diamonds['channel'].value_counts())

########################
# Other Visuals
########################

sns.violinplot(x = 'channel',
               y = 'price',
               data = diamonds,
               orient = 'v')
plt.savefig('1.png')
plt.show()



sns.stripplot(x = 'store',
              y = 'price',
              data = diamonds,
              size = 5,
              orient = 'v')
plt.savefig('2.png')
plt.show()



sns.swarmplot(x = 'store',
              y = 'price',
              data = diamonds,
              size = 5,
              orient = 'v')
plt.savefig('3.png')
plt.show()



