#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 18:11:26 2018

@author: chase.kusterer

Working directory: 
    /Users/raymondzano/Desktop/PyCourse

Purpose:
    This code is meant to treat missing values in the diamond dataset
"""

###############################################################################
# Importing libraries and base dataset
###############################################################################

import pandas as pd # data science essentials (read_excel, DataFrame)
import matplotlib.pyplot as plt # data visualization


file ='diamonds_missing_values.xlsx'
diamonds = pd.read_excel(file)

###############################################################################
# Viewing our dataset
###############################################################################

"""
Prof. Chase:
    Click on the data object in the variable explorer to view it.
"""

# Taking a look at the entire dataset
diamonds



# Viewing the first 5 rows of the dataset
diamonds.head()



# Viewing the first 50 rows of the dataset
diamonds.head(n = 50)



# We can also view the last n rows of our dataset
diamonds.tail(n = 10)



# We can view subsets of columns and rows with loc and iloc

"""
Prof. Chase:
    The syntax for loc and iloc is [rows, columns].
"""

diamonds.loc[:, 'carat']
diamond['carat']    #same output as above
#loc vs iloc



diamonds.iloc[:, 1]



diamonds.iloc[0:9, :]



diamonds.iloc[20:35, :] #looks at row 20 to 34 for the entire column

# We can also provide more detailed subsets with loc and iloc
diamonds.loc[20:35, ['carat', 'price']] #this doesn't work
diamonts.loc[:,['carat', 'price']]


###############################################################################
# Summarizing our dataset
###############################################################################

diamonds.shape #output is tuple ()
#number of rows and columns

diamonds.info()

diamonds.describe() #summary statistics

diamonds.describe().round(2) #this is a dataframe, we can use loc and iloc

print(f"""
      There are {diamonds.shape[0]} rows.
      """)

###############################################################################
# Subsetting our dataset
###############################################################################

diamonds[diamonds['carat'] > 1]

diamonds[diamonds['carat'] > 1].describe()

diamonds['carat'][
        (diamonds['carat'] > 1) &
        (diamonds['carat'] < 2)
        ]

diamonds[
        (diamonds['carat'] > 1) &
        (diamonds['carat'] < 2)
        ]

diamonds[
        (diamonds['price'] > 3500) &
        (diamonds['price'] < 4500) &
        (diamonds['carat'] > 1) & # this is or |
        (diamonds['carat'] < 2)        
        ].describe().round(2)

diamonds[
        (diamonds['carat'] > 1) &
        (diamonds['carat'] < 2)
        ].describe().round(2)

# See Footnote 1 for an explanation of the code above

"""
Practice:
    Which diamonds cost less than or equal to 1000 (USD)?
"""
diamonds[diamonds['price'] <= 1000]
diamonds[diamonds['price'] <= 1000][diamonds['cut']==1]

# Let's sort this set by price.
diamonds[diamonds['price'] <= 1000].sort_values(['price'],ascending= False)
diamonds[diamonds['price'] <= 1000].sort_values(['price','carat'],ascending= False)

# See Footnote 2 for an explanation of the code above

"""
Prof. Chase:
    The code above is starting to look complicated. Let's make things
    simpler by creating a new object.
"""


low_price = diamonds[diamonds['price'] <= 1000]

low_price.sort_values(['price'],
                      ascending= False)

# We can sort on multiple criteria

low_price.sort_values(['cut', 'carat'],
                      ascending= False) #master sort

"""
It's interesting that are all of these diamonds come from the same
store. Let's explore this store in more detail.
"""

store_10 = diamonds[diamonds['store'] == 10]


# Rounding this summary to make things more clean.
store_10.describe().round(1)

###############################################################################
# Checking for missing values
###############################################################################

# Let's first check how many observations aren't missing
diamonds.count() #memorize

# Stretching out our code so that we can read it more clearly
print(
      diamonds.isnull()
      .any()
      ) #looks at the summary only or per column

# Missing values in absolute numbers
print(
      diamonds
      .isnull()
      .sum()
      ) #sum of missing values per column



# As a percentage of total observations (take note of the parenthesis)
print(
      (diamonds.isnull().sum())
      /
      len(diamonds)
) # %age of data missing per column
# len() and describe[0] provides the same output

# See Footnote 3 for an explanation of the code above
print(
      (diamonds.isnull().sum())
      /
      ((len(diamonds)).round(3))
) #round(3) is not working - 'int' object has no attribute 'round'


"""
Prof. Chase:
    As with before, we can simplify our code by saving things as
    objects.
"""

missing_diamonds = diamonds.isnull().sum()


total_diamonds = diamonds.count()


missing_ratio = missing_diamonds / total_diamonds


missing_ratio.round(2)


###############################################################################
# Flagging missing values
###############################################################################

"""
Prof. Chase:
    This is an important step for two reasons:
        1) to keep record as to which values have been changed
        2) the fact that a value was missing can in and of itself be
           predictive
"""


# How to create a missing value flag
diamonds['carat'].isnull()
diamonds['carat'].isnull().astype(int)



# Sorting to display the missing value flags
(diamonds['carat']
            .isnull()
            .astype(int)
            .sort_values(ascending = False))
#first line displays the carat of each diamond, second line flags those with NAN
#third line converts those with no values to 1,

# See Footnote 4 for an explanation of the code above



"""
Prof. Chase:
    The outer parenthesis in the code above were added so that the code
    could be spread out on mulitple lines. Other than this they are not
    necessary, as can be seen in the code below.
"""


"""
Objective:
    Create columns that are 0s if a value was not missing and 1 if
    a value is missing.
"""


# Coding line by line
diamonds['m_carat'] = (diamonds['carat']
                        .isnull()
                        .astype(int)
                        )#converted to 1 and 0 depending on boolean depending
#on the true and false outcome

#removing a column using = 

# Since we are repeating the same line of code many times, there is no
# reason to spread it out again.

diamonds['m_color'] = diamonds['color'].isnull().astype(int)


diamonds['m_clarity'] = diamonds['clarity'].isnull().astype(int)
#diamonds['m_'+col] = diamonds[col].isnull().astype(int)
#same as line 347

diamonds['m_cut'] = diamonds['cut'].isnull().astype(int)


# See Footnote 1 for a breakdown of the code above



# Let's check to make sure the code above is working properly.
print(diamonds['carat']
                .isnull()
                .sum())



print(diamonds['m_carat']
                .sum())



# We could also check with the following code
diamonds['carat'].isnull().sum() == diamonds['m_carat'].sum()


# See Footnote 5 for an explanation of the code above



###############################################################################
# Looping through missing values
###############################################################################

"""
Prof. Chase:
    This section may seem advanced. Please keep in mind that although
    coding a loop like the one below may take several hours to perfect,
    once it is coded, it can be used over and over again.
"""


# Resetting the dataset
diamonds = pd.read_excel(file)



# Creating a loop to improve efficiency
for col in diamonds:
    print(col)

    """ Create columns that are 0s if a value was not missing and 1 if
    a value is missing. """
    
    if diamonds[col].isnull().any():
        diamonds['m_'+col] = diamonds[col].isnull().astype(int)


# See Footnote 6 for a breakdown of the code above



# checking to see if the for loop worked
print(diamonds.head())


# making a more formal check
a = diamonds.isnull().sum().sum()
b = diamonds.iloc[:,-5:].sum().sum()


"""
For the footnotes:
diamonds.loc[:,['m_carat', 'm_color', 'm_clarity', 'm_cut']].sum().sum()
"""



if a == b:
    print('All missing values accounted for.')
else:
    print('Some missing values may be unaccounted for, please audit.')


###############################################################################
# Imputing missing values
###############################################################################

"""
Prof. Chase:
   In the following code, we are going to attempt three fill methods
   for our missing values: mean, median, and dropping missing values.
   
   To start, we need three different datasets
"""


# Let's start by creating three different datasets


# The following code copies and makes each DataFrame independent
df_mean  = pd.DataFrame.copy(diamonds) #makes a copy of dataset and sets to somewhere else


df_median = pd.DataFrame.copy(df_mean)


df_dropped = pd.DataFrame.copy(df_median)



# See Footnote 7 for a breakdown of the code above



# We could fill each column one-by-one
carat_mean = diamonds['carat'].mean()



diamonds['carat'] = (diamonds['carat']
                            .fillna(carat_mean)
                            .round(2))

#under the carat column, fill the null values with the mean of the initial values

(diamonds['carat'].fillna(carat_mean).round(2)) #from line 416

df_mean[col].fillna(col_mean).round(2) #from line 435

# See Footnote 8 for a breakdown of the code above



# ... or we could create a loop
for col in df_mean:
    
    """ Impute missing values using the mean of each column """
    
    if df_mean[col].isnull().any():
        
        col_mean = df_mean[col].mean()
        
        df_mean[col] = df_mean[col].fillna(col_mean).round(2)


# See Footnote 9 for a breakdown of the code above



# Creating a loop for df_median
for col in df_median:
    
    """ Impute missing values using the mean of each column """
    
    if df_median[col].isnull().any():
        
        col_median = df_median[col].median()
        
        df_median[col] = df_median[col].fillna(col_median).round(2)

#ines 442 - 451 is the same as lines 426 - 435

# Using dropna() for df_dropped
df_dropped = df_dropped.dropna().round(2)

#dropna removes missing values

# See Footnote 10 for a breakdown of the code above



# With new values imputed, our means should be different between some datasets
print(diamonds['color'].mean())


print(df_mean['color'].mean())


print(df_median['color'].mean())


print(df_dropped['color'].mean())



# We can check this as follows:
diamonds.mean() == df_mean.mean()



# Also, there should be no missing values in our new datasets
print(df_mean.isnull()
                .any()
                .any())



print(df_median.isnull()
                .any()
                .any())



print(df_dropped.isnull()
                .any()
                .any())


# See Footnote 11 for an explanation of the code above



###############################################################################
# Choosing imputation techniques
###############################################################################

"""
Prof. Chase:
    Oftentimes, choosing an imputation technique is regarded as more of
    an art than a science. We can start by:
        a) checking available domain knowledge
        b) looking for noticable patterns in the dataset
        c) checking a variable's distribution and choosing an appropriate
           measure of center
"""

# Checking variable distributions

"""
Prof. Chase:
    Several statistical and graphical functions cannot handle missing
    data and will throw a ValueError (i.e. ValueError: max must be
    larger than min in range parameter.)
    
    Having a dataset like 'df_dropped' can be very helpful in situations
    such as these.
"""

# Creating histograms
plt.hist(df_dropped['carat'], bins = 'fd')
plt.show()


plt.hist(df_dropped['color'], bins = 50)
plt.show()


plt.hist(df_dropped['clarity'], bins = 50)
plt.show()


plt.hist(df_dropped['cut'], bins = 50)
plt.show()


# Let's develop something more sophisticated

###################
# Mean or median? #
###################

plt.subplot(2, 2, 1)
plt.hist(df_dropped['carat'],
         bins = 25,
         color='blue',
         alpha = 1)
plt.title('Carat Weight')


plt.subplot(2, 2, 2)
plt.hist(df_dropped['color'],
         bins = 20,
         color='green',
         alpha = 1)
plt.title('Color')


plt.subplot(2, 2, 3)
plt.hist(df_dropped['clarity'],
         bins = 20,
         color='red',
         alpha = 1)
plt.xlabel('Clarity')


plt.subplot(2, 2, 4)
plt.hist(df_dropped['cut'],
         bins = 3,
         color='purple',
         alpha = 1)
plt.xlabel('Cut')

plt.savefig('Histograms before Imputation.png')
plt.show()

# See Footnote 12 for an explanation of the code above

# carat seems skewed positive... median
# color seems skewed positive... median
# clarity looks normally distributed... mean
# cut is binomial... mode expressed as the median

###############################################################################
# Imputing missing values on the original dataset
###############################################################################

# Median imputation carat

fill = diamonds['carat'].median()


diamonds['carat'] = diamonds['carat'].fillna(fill)



# Median imputation color
fill = diamonds['color'].median()


diamonds['color'] = diamonds['color'].fillna(fill)



# Median imputation cut
fill = diamonds['cut'].median()


diamonds['cut'] = diamonds['cut'].fillna(fill)



print(diamonds['carat'].isnull().any())

print(diamonds['color'].isnull().any())

print(diamonds['cut'].isnull().any())


# Mean imputation (clarity)
fill = diamonds['clarity'].mean()


diamonds['clarity'] = diamonds['clarity'].fillna(fill).astype(int)


# See Footnote 13 for an explanation of the code above


print(diamonds['clarity'].isnull().any())



###############################################################################
# Checking data after imputation
###############################################################################

plt.subplot(2, 2, 1)
plt.hist(diamonds['carat'],
         bins = 25,
         color='blue',
         alpha = 0.98)
plt.title('Carat Weight')



plt.subplot(2, 2, 2)
plt.hist(diamonds['color'],
         bins = 20,
         color='green',
         alpha = 0.8)
plt.title('Color')



plt.subplot(2, 2, 3)
plt.hist(diamonds['clarity'],
         bins = 20,
         color='red',
         alpha = 0.8)
plt.xlabel('Clarity')

plt.subplot(2, 2, 4)
plt.hist(diamonds['cut'],
         bins = 3,
         color='purple',
         alpha = 0.8)
plt.xlabel('Cut')

plt.savefig('Histograms after Imputation.png')
plt.show()

###############################################################################
# Saving things for future use
###############################################################################

# saving dataset
diamonds.to_excel('diamonds_imputed.xlsx', index = False)

"""
###############################################################################
# Footnotes
###############################################################################


Footnote 0: the purpose of footnotes

to give a line-by-line explanation of a code snippet


*******************************************************************************


Footnote 1: subsetting on multiple criteria

diamonds['carat']                 # take the carat column from diamonds
[(diamonds['carat'] > 1)          # subset so that each carat is > 1
&                                 # and also
(diamonds['carat'] < 2)]          # subset so that each carat is < 2


*******************************************************************************


Footnote 2: subsetting and sorting values

diamonds                          # take the whole diamonds dataset
[diamonds['price'] <= 1000]       # subset where price <= 1000
.sort_values(['price'],           # sort each value based on price
ascending= False)                 # such that the highest price is at the top


*******************************************************************************


Footnote 3: subsetting and sorting values

print(                            # wrapping the call around a print statement
((diamonds                        # calling the diamonds dataset
.isnull()                         # checking to see if there are any missing values
.sum())                           # and adding all the missing values together per column
/                                 # ... dividing this result by
len(diamonds)                     # the total number of observations in the dataset
)                                 # closing the print statement


*******************************************************************************


Footnote 4: displaying missing value flags

(                                 # allows for spreading a call on multiple lines
diamonds['carat']                 # calling the carat column of diamonds
.isnull()                         # checking each observation for missing values (True or False)
.astype(int)                      # converting the True/False to an integer (1 or 0)
.sort_values(ascending = False)   # sorting so that the 1's are at the top
)                                 # closing the call


*******************************************************************************


Footnote 5: checking to see if all missing values have been flagged

diamonds['carat']                 # calling the carat column of diamonds
.isnull()                         # checking each observation for missing values (True or False)
.sum()                            # adding the number of missing values together
==                                # checking for equality
diamonds['m_carat']               # calling the m_carat column of diamonds
.sum()                            # and adding the number of flags (1's) together



*******************************************************************************


Footnote 6: creating a for loop to flag missing values

for col in diamonds:              # Starting a for loop

Create columns that are           # Docstring to explain the loop
0s if a value was not missing
and 1 if a value is missing.
    
if                                # Starting an if statement
diamonds[col]                     # ...that takes each column in the diamonds dataset
.isnull().any():                  # and checks to see if it has at least one missing value

diamonds['m_'+col] =              # and if so, creates a new column with named m_ + the original column name
diamonds[col].                    # and the values for this new column
isnull().astype(int)              # are 1's or 0's based on whether the orginal observation was missing


*******************************************************************************


Footnote 7: copying a dataframe to different objects

df_dropped =                       # create a new object 'df_dropped'
pd.DataFrame                       # call the package pd.DataFrame
.copy(diamonds)                    # and use its copy function on 'diamonds'


*******************************************************************************


Footnote 8: filling missing values across the entire dataset

carat_mean =                       # create a new object called carat_mean
diamonds['carat'].mean()           # by taking the mean of the 'carat' column

diamonds['carat'] =                # prepare to modify the 'carat' column
(diamonds['carat']                 # by putting it on both sides of =
.fillna(carat_mean)                # fill in the na values with carat_mean
.round(2))                         # and round the results to two decimal places


*******************************************************************************


Footnote 9: for loop for filling missing values across the entire dataset

for col in df_mean:                # starting a for loop

\""" Impute... \"""                # explaining what the loop does

if df_mean[col]                    # adding a conditional if statement
.isnull()                          # that first checks if a value is missing
.any():                            # then checks if there is at least one missing value
    
col_mean = df_mean[col].mean()     # defining an object to store the mean of the column

df_mean[col] =                     # redefining the object 'df_dropped'
df_mean[col]                       # by putting it on both sides of the '='
.fillna(col_mean)                  # impute missing values using the mean
.round(2)                          # then round it to two decimal places


*******************************************************************************


Footnote 10: dropping missing values

df_dropped =                       # redefining the object 'df_dropped'
df_dropped                         # by putting it on both sides of the '='
.dropna()                          # 'dropna()' will remove all rows with missing values
.round(2)                          # rounding the result to two decimal places


*******************************************************************************


Footnote 11: checking for missing values

print(                             # calling 'print()'
df_dropped.isnull()                # on a null boolean of 'df_dropped'
.any()                             # and aggregating the result to the column level
.any())                            # and finally to the dataset level


*******************************************************************************


Footnote 12: plotting histograms

plt.subplot(2, 2,                  # creating a 2x2 plot matrix
4)                                 # and setting this graph to the bottom-left window

plt.hist(df_dropped['cut'],        # calling the '.hist' function on some data
         bins = 3,                 # and setting bins equal to three
         color='purple',           # and making the data bars purple
         alpha = 0.1)              # and fading the data bars 90%
plt.xlabel('Cut')                  # adding a label for the x-axis

plt.savefig('....png')             # saving the figure as a .png file

plt.show()                         # and finally showing the plot


*******************************************************************************

Footnote 13: mean imputation for clarity

fill =                             # creating a variable called fill
diamonds['clarity'].mean()         # that is equal to the mean of clarity from diamonds


diamonds['clarity'] =              # redefining clarity from diamonds
diamonds['clarity']                # by taking its original values
.fillna(fill)                      # and filling missing values with 'fill' as defined above
.astype(int)                       # and converting the values to integers


*******************************************************************************
"""








