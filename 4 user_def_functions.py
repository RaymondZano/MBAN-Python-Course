#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 14:29:57 2018

@author: chase.kusterer

Working Directory:
/Users/chase.kusterer/Desktop/PyCourse
    
Purpose:
To learn user input and escape sequences
"""

###############################################################################
## Part 1: Basic Functions
###############################################################################

"""
Prof. Chase:
    In their most basic form, user-defined functions follow the
    following framework:
        
        def FUNCTION_NAME(ARGUMENTS):
            
            FUNCTION BODY

"""

# Function with no arguments
def nice_comment():
    """ This function prints a nice comment. """
    
    print("You look lovely today.")


nice_comment()


"""
Prof. Chase:
   Notice the explanation of the function in the first line of its
   definition. This is called a docstring. These are very important in
   helping others to understand what your function does, and also to
   help you remember after you haven't used it for awhile.

"""

help(nice_comment)


# This function can be extended with deeper Python logic

def nice_comment():
    import random # importing random within the function
    """ This function prints a nice comment at random. """
    
    comment = random.randint(1,3) # defining a new variable called random
    
    if comment == 1:
        print("You look lovely today.")
    
    
    elif comment == 2:
        print("I feel happier when you are around.")
    
    
    elif comment == 3:
        print("Today is a great day to be yourself.")
        
    
    else:
        print("This function has bugs.")

nice_comment()

"""
Prof. Chase:
    In the above function, the variable comment is a local variable,
    meaning it only exists within the function but nowhere else in the
    script.
    
    This is why iff we try to run comment (as below) we will get an
    error.

"""

# The following will not work (comment only exists within nice_comment())
comment

# The following will not work (random is only loaded within nice_comment())
random.randint(1,2)

###############################################################################
## Part 2: Functions with Return Statements
###############################################################################

"""
Prof. Chase:
    If we want our function to return something, we can update our
    function framework to the following:
        
        def FUNCTION_NAME(ARGUMENTS):
            
            FUNCTION BODY
            
            RETURN

"""

# Let's set up our code a little differently and see what happens

def nice_comment():
    import random #importing random within the function
    """ This function does nothing because there is no return statement. """
    
    comment = random.randint(1,3)
    
    if comment == 1:
        comment = "You look lovely today."
    
    elif comment == 2:
        comment = "I feel happier when you are around."
    
    elif comment == 3:
        comment = "Today is a great day to be yourself."
    
    else:
        print("This function has bugs.")
    

import random

# Notice how nice_comment doesn't print anything anymore
nice_comment

# Notice also that if we print the result of nice_comment, we get None
a = nice_comment()
print(a)


"""
Prof. Chase:
    Notice the indentations in the above function. These are VERY
    IMPORTANT!
"""

# By adding a return statement, we get the result we are looking for

def nice_comment():
    """ This function returns a nice comment at random. """
    
    import random
    comment = random.randint(1,3)
    
    if comment == 1:
        comment = "You look lovely today."
        return comment
    
    elif comment == 2:
        comment = "I feel happier when you are around."
        return comment
    
    elif comment == 3:
        comment = "Today is a great day to be yourself."
        return comment
    
    else:
        print("This function has bugs.")
    


# Now when we print nice_comment() we get a random nice comment!
print(nice_comment())


# If we want a non-random comment, we can save the result of nice_comment
b = nice_comment()
print(b)



###############################################################################
## Part 3: Functions and Lists
###############################################################################

list_1 = [1, 2, 3, 4, 5]

print(list_1)

def new_item(item):
    """ This function adds a new item to a predefined list. """
    
    list_1.append(item) # appending list_1 with item
 


# Adding 6 to list_1
new_item(6)
   
print(list_1)

"""
Prof. Chase:
   Notice how we did not need a return statement in the new_item
   functon. This is because my_list already existed outside of the
   function. Therefore, the function search the global environment and
   used the most recent version of my_list before the function was
   called.
"""


###############################################################################
## Part 4: Functions, Lists, and Returns
###############################################################################

# Let's try what we did above but on a list that doesn't exist

def new_item_2(item, lst = []):
    """ This function returns nothing because it has no return statement. """
    
    lst.append(item)
#return is missing

list_2 = new_item_2(1)
print(list_2)

# As expected, we need a return statement in order for our function to
# work properly



# Adding a return clause
def new_item_3(item, lst = []):
    """ This function will return an item to a predefined list, or
    create a new list if one is not input in the arguments."""
    
    lst.append(item)
    return lst

list_3 = new_item_3(1)
print(list_3)

new_item_3(item = 99, lst = list_1)

###############################################################################
## Part 5: Adjusting Optional Arguments
###############################################################################

# Let's create a new list and use the new_item_3 function to append it

list_4 = [1, 2, 3, 4, 5]

new_item_3(6, list_4)

print(list_4)

# Creating and utilizing optional arguments can have profound effects
# on the usefulness of our functions.



###############################################################################
## Part 6: Improving our nice_comment function
###############################################################################


comment_list = ["You look lovely today.",
                "I feel happier when you are around.",
                "Today is a great day to be yourself."]



def nice_comment_2(lst = []):
    """ This function takes an item from a list and returns it. """
    
    import random
    
    comment = lst[random.randint(0, len(lst) - 1)]
    
    return comment



c = nice_comment_2(lst = comment_list)
print(c)



"""
Prof. Chase:
    The len(lst) - 1 might seem tricky. Try taking it out and see if an
    error message pops up.
    
    The reason is that our random.randint starts with 0, so we would be
    adding in a range that is wider than the length of our list.
    
    len(lst) - 1 is useful if we want to extend our comment list. This
    way, we don't have to update the function every time we want to add
    or delete a comment from the list.
"""


# We could also house comment_list inside of our function
# That way, we don't need the optional lst argument



def nice_comment_3():
    """ This function takes a comment from an internal comment list and returns it. """
    
    import random
    
    lst = ["You look lovely today.",
           "I feel happier when you are around.",
           "Today is a great day to be yourself."]
    
    comment = lst[random.randint(0, len(lst) - 1)]
    
    return comment

d = nice_comment_3()
print(d)


###############################################################################
## Part 7: Setting Global Variables
###############################################################################

"""
Prof. Chase:
    If we wanted to be able to access our comment list in
    nice_comment_3(lst), we could declare it global using the following
    command:
        
        global lst
"""


def nice_comment_4():
    """ This function takes a comment from an internal comment list and returns it.
        It also sends the comment list and the comment to the global environment."""
    
    import random
    
    global lst
    global comment
    
    lst = ["You look lovely today.",
           "I feel happier when you are around.",
           "Today is a great day to be yourself."]
    
    comment = lst[random.randint(0, len(lst) - 1)]
    
    return comment


# To activate these variables as global, we need to call our function
# at least one time.

nice_comment_4()

# Now lst and comment are both available in the global environment
lst
comment

"""
Prof. Chase:
   Be careful when declaring global variables. This is not a common
   practice in functions as it can change the values of variables that
   you already have in your global environment.
   
   For example, if you have a variable named x in your global
   environment and you call a function that has a global variable also
   named x, you may run into problems due to what's happening behind
   the scenes.
"""

###################
# Global overwright example
###################

x = 10

def global_example():
    """ This function sets a global variable named x to 100 """
    
    global x
    x = 100



# x BEFORE calling global example
print(x)


# x AFTER calling global example
global_example()

print(x)



###############################################################################
## Part 8: Advanced nice_comment function (Advanced)
###############################################################################

"""
Prof. Chase:
   This section uses a technique called the while loop, which we have
   not covered in class yet. For now, try to understand what it is
   doing so that you get a better understanding as to what's to come.
"""

# Using a while loop in the function

# Redefining the function so that it can return more than one comment
def nice_comment_4(n = 1):
    """ This function allows you to specify the number of comments
    you would like returned, and returns them as a list. """
    
    import random
    
    lst = ["You look lovely today.",
           "I feel happier when you are around.",
           "Today is a great day to be yourself."]
    
    comments = []
    
    while n > 0:
        comment = lst[random.randint(0, len(lst) - 1)] 
        comments.append(comment)
        n -= 1

    return comments


f = nice_comment_4()
print(f)


g = nice_comment_4(n = 2)
print(g)


h = nice_comment_4(n = 5)
print(h)



"""
Prof. Chase:
   The following also adds a for loop, another concept we have not yet
   covered. Again, try to understand what it is doing so that you have
   a better understanding as to what's to come.
"""

# Using a while loop and a for loop in the function

def nice_comment_5(n = 1):
    """ This function allows you to specify the number of comments you
    would like returned, and prints them out. """
    
    import random
    
    lst = ["You look lovely today.",
           "I feel happier when you are around.",
           "Today is a great day to be yourself."]
    
    comments = []
    
    while n > 0:
        comment = lst[random.randint(0, len(lst) - 1)] 
        comments.append(comment)
        n -= 1

    for comment in comments:
        print(comment, "\n")



nice_comment_5()


nice_comment_5(n = 2)


nice_comment_5(n = 5)