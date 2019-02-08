#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 14:07:29 2018

@author: chase.kusterer

Working Directory:
/Users/chase.kusterer/Desktop/PyCourse
    
Purpose:
To learn conditional statements.
"""




###############################################################################
## Part 1: Building a basic conditional statement
###############################################################################

study_hours = 1

if study_hours > 20:
    print("Wow! You get an A for effort!")


# Since study_hours does not meet the criteria in the if statement,
# nothing prints



study_hours = 21

if study_hours > 20:
    print("Wow! You get an A for effort!")


# Now that study hours meets the criteria in the if statement, the
# print statement runs




###############################################################################
## Part 2: Adding else
###############################################################################
    
# Let's enhance our function with an else statement.
    
study_hours = 1

if study_hours > 20:
    print("Wow! You get an A for effort!")


else:
    print("Take some time to study a bit more.")


# Since study_hours does not meet the criteria in the if statement,
# the else print statement runs



study_hours = 21

if study_hours > 20:
    print("Wow! You get an A for effort!")


else:
    print("Take some time to study a bit more.")


# Now that study hours meets the criteria in the if statement, the
# if print statement runs




###############################################################################
## Part 2: Adding elif
###############################################################################

# Now let's add in an elif statement for 15-20 hours of study

study_hours = 15

if study_hours > 20:
    print("Wow! You get an A for effort!")


elif study_hours >= 15:
    print("You're on pace, good job!")


else:
    print("Take some time to study a bit more.")


# In this case, the elif statement runs as the value of study_hours
# meets its criteria

"""
Prof. Chase:
    In Python, if statements run from top to bottom and stop soon a
    criteria is met. Any criteria after this will not be run. Please
    see the example below.
"""

study_hours = 5

if study_hours > 1:
    print("Wow! You get an A for effort!")


elif study_hours > 2:
    print("You're on pace, good job!")


else:
    print("Take some time to study a bit more.")
    

# Only the first met criteria runs



###############################################################################
## Part 2: Mixing User Input and Conditional Statements
###############################################################################

# Let's add an input statement to our conditional

study_hours = input("How many hours did you study this week:\n")

if study_hours > 20:
    print("Wow! You get an A for effort!")


elif study_hours >= 15:
    print("You're on pace, good job!")


else:
    print("Take some time to study a bit more.")


# TypeError: '>' not supported between instances of 'str' and 'int'


# Since we get a TypeError, let's investigate our variable types
type(study_hours)


# As expected from our error message, study_hours is of type str

# Unfortunately, we can't use boolean operators on a string, therefore
# we need to find a solution


###################
# Solution 1: Changing the type in input
###################

study_hours = int(input("How many hours did you study this week:\n"))

if study_hours > 20:
    print("Wow! You get an A for effort!")
    

elif study_hours >= 15:
    print("You're on pace, good job!")


else:
    print("Take some time to study a bit more.")



###################
# Solution 2: Changing the type in our conditional statement
###################

print("""
How many hours did you study this week?
    1. less than 15 hours
    2. 15-20 hours
    3. more than 20 hours
""")

study_hours = input("> ")


if study_hours == '1':
    print("Take some time to study a bit more.")
    
    
elif study_hours == '2':
    print("You're on pace, good job!")


elif study_hours == '3':
    print("Wow! You get an A for effort!")


else:
    print("Invalid entry. Please choose 1, 2, or 3.")



###############################################################################
## Part 3: Expanding Solution 2
###############################################################################

# Let's make Solution 2 more user friendly

"""
Prof. Chase:
    Making things more user friendly for the user is likely to make
    things more complicated for the programmer. It is important to try
    to find simple solutions to the challenges you encounter.
"""

print("""
How many hours did you study this week?
    1. less than 15 hours
    2. 15-20 hours
    3. more than 20 hours
""")

study_hours = input("> ")


if '1' in study_hours or 'less than' in study_hours:
    print("Take some time to study a bit more.")


elif '2' in study_hours or '15' in study_hours or '20' in study_hours:
    print("You're on pace, good job!")


elif '3' in study_hours or 'more than' in study_hours:
    print("Wow! You get an A for effort!")


else:
    print("invalid entry")



# This is a better approach, but there is a bug in Option 2


print("""
How many hours did you study this week?
    1. less than 15 hours
    2. 15-20 hours
    3. more than 20 hours
""")

study_hours = input("> ")


if 'less than' in study_hours:
    print("Take some time to study a bit more.")


elif 'more than' in study_hours:
    print("Wow! You get an A for effort!")


elif int(study_hours) >= 15 and int(study_hours) <= 20:
    print("You're on pace, good job!")


elif int(study_hours) == 3:
    print("Wow! You get an A for effort!")


elif int(study_hours) == 2:
    print("You're on pace, good job!")


elif int(study_hours) == 1:
    print("Take some time to study a bit more.")


else:
    print("invalid entry")


# This resolves our Option 2 bug, but there is still an issue.

###############################################################################
## Part 4: Overlapping conditions
###############################################################################

"""
Prof. Chase:
    There is still a small problem. What if a user inputs 1 and their
    intent is to say that they have studied only one hour?
    
    Developing solutions to this problem can be complex and
    frustrating. One approach is to simply change our option numbering
    to A, B, and C.
"""


print("""
How many hours did you study this week?
    A. less than 15 hours
    B. 15-20 hours
    C. more than 20 hours
""")

study_hours = input("> ")
  

if 'less than' in study_hours:
    print("Take some time to study a bit more.")

 
elif 'more than' in study_hours:
    print("Wow! You get an A for effort!")


elif study_hours.lower() == 'a': # Using .lower() in case someone inputs 'A' or 'a'.
    print("Take some time to study a bit more.")


elif study_hours.lower() == 'b':
    print("You're on pace, good job!")


elif study_hours.lower() == 'c':
    print("Wow! You get an A for effort!")


elif int(study_hours) < 15:
    print("Take some time to study a bit more.")


elif int(study_hours) >= 15 and int(study_hours) <= 20:
    print("You're on pace, good job!")


elif int(study_hours) > 20:
    print("Wow! You get an A for effort!")


else:
    print("invalid entry")


# for more information on .lower() try the code below
help(str())

###############################################################################
## Part 5: (Bonus) Easter Eggs (Wontons)
###############################################################################

"""
Prof. Chase:
    An Easter egg is a special, hidden item within a program. Let's add
    one into our conditional statement for study hours.
"""


print("""
How many hours did you study this week?
    A. less than 15 hours
    B. 15-20 hours
    C. more than 20 hours
""")

study_hours = input("> ")
  
if 'less than' in study_hours:
    print("Take some time to study a bit more.")  


elif 'more than' in study_hours:
    print("Wow! You get an A for effort!")


# wonton
elif study_hours == 'every hour':
    print("""
                                                                         ___   
                                                                      .'/   \  
          __  __   ___                       .--.   _..._            / /     \ 
         |  |/  `.'   `.                     |__| .'     '.   .--./) | |     | 
         |   .-.  .-.   '                    .--..   .-.   . /.''\\  | |     | 
    __   |  |  |  |  |  |    __              |  ||  '   '  || |  | | |/`.   .' 
 .:--.'. |  |  |  |  |  | .:--.'.  .--------.|  ||  |   |  | \`-' /   `.|   |  
/ |   \ ||  |  |  |  |  |/ |   \ | |____    ||  ||  |   |  | /("'`     ||___|  
`" __ | ||  |  |  |  |  |`" __ | |     /   / |  ||  |   |  | \ '---.   |/___/  
 .'.''| ||__|  |__|  |__| .'.''| |   .'   /  |__||  |   |  |  /'""'.\  .'.--.  
/ /   | |_               / /   | |_ /    /___    |  |   |  | ||     ||| |    | 
\ \._,\ '/               \ \._,\ '/|         |   |  |   |  | \'. __// \_\    / 
 `--'  `"                 `--'  `" |_________|   '--'   '--'  `'---'   `''--'  
          """)



elif study_hours.lower() == 'a':
    print("Take some time to study a bit more.")   
    

elif study_hours.lower() == 'b':
    print("You're on pace, good job!")
    
    
elif study_hours.lower() == 'c':
    print("Wow! You get an A for effort!")


elif int(study_hours) < 15:
    print("Take some time to study a bit more.")

elif int(study_hours) >= 15 and int(study_hours) <= 20:
    print("You're on pace, good job!")

elif int(study_hours) > 20:
    print("Wow! You get an A for effort!")

else:
    print("invalid entry")


