

"""
Dean Luis and Dean Amber have both been assigned to wash the dishes
after the Winter Ball. They are trying to divide the work evenly, and
Dean Luis gets the great idea that one person should wash the cups,
plates, and silverware, while the other washes the pots and pans.

* It takes 15 seconds to wash one cup, and there are 500 cups.
* It takes 10 seconds to wash one plate, and there are 500 plates.
* It takes 10 seconds to wash one piece of silverware, but they can be
  washed three at a time. There are 1200 pieces of silverware
* It takes 80 seconds to wash one pot and there are 25 pots
* It takes 60 seconds to wash one pot and there are 75 pans

He asks Dean Amber which she prefers. Which should Amber choose?
    a) the cups, plates, and silverware
    b) the pots and pans
    
"""

# Washing Time Breakdown:
cup_time = 15
plate_time = 10
silverware_time = 10
pots_time = 80
pans_time = 60
    
# Quantity of Dishes:
cup_qty = 500
plate_qty = 500
silverware_qty = 1200/3
pots_qty = 25
pans_qty = 75


# Plates, Cups, and Silverware
cup_wash = (cup_time * cup_qty)
plate_wash = (plate_time * plate_qty)
silver_wash = (silverware_time * silverware_qty)

cps_wash = cup_wash + plate_wash + silver_wash
print(cps_wash)

# Pots and Pans
pot_wash = (pots_time * pots_qty)
pan_wash = (pans_time * pans_qty)

pp_wash = pot_wash + pan_wash
print(pp_wash)

# Testing for Equality

print(cps_wash == pp_wash)


"""
Dean Amber runs an analysis in Python and realizes that the duties
aren't even close to equal. She drafts Dean Luis an email informing
him of the situation.

"""

print(f"""
      Dear Luis,
      
      It has come to my attention that with our current quantities of:
      {cup_qty} cups, {plate_qty} plates, {silverware_qty} pieces of
      silverware, {pots_qty} pots, and {pans_qty} pans, our duties
      would not even be close to equal if we were to split them in the
      way that you have recommended.
      
      I will begin working on a solution where our duties are split
      more equally. And reply to you via SMS message.
      
      Sincerely,
      Dean Amber
      """)

# We have just used an f string above, which is a way to dynamically
# call variables and other objects into a print script.

###################
# Calculations in f strings
###################    

# We can make calculations in f strings as follows.

print(f"""
      Dear Luis,
      
      To give more details on my previous email, one of us would be
      working for {int(cps_wash / 3600)} hours and {int((cps_wash % 3600) / 60)}
      minutes, while the other would be working {int(pp_wash / 3600)}
      hours and {int((pp_wash % 3600) / 60)} minutes.
      
      I will begin working on a solution where our duties are split
      more equally.
      
      Sincerely,
      Dean Amber
      """)

# See Footnote 1 for these calculations step-by-step
###############################################################################
## Part 2: Making the Calculation Balance
###############################################################################

"""
Prof. Chase:
    Use this template to help balance the workload between Dean Luis
    and Dean Amber.
"""

# Current Variables
print(cup_wash)
print(plate_wash)
print(silver_wash)
print(pot_wash)
print(pan_wash)

# Change the duties below to balance the workload
luis = plate_wash+pan_wash+pot_wash
amber = cup_wash+silver_wash

print(luis)
print(amber)
      
# Testing for Equality

print(luis == amber)

###############################################################################
## Part 3: Reply to Dean Luis with your new duties
###############################################################################

print(f"""
      Dear Dean Luis,
      
      
      
      
      
      Sincerely,
      Dean Amber
      """)

###############################################################################
## Footnotes
###############################################################################

"""
Footnotes

Footnote 1: f string calculations

{int(                # int() can be used similar to =ROUNDDOWN() in Excel
cps_wash / 3600)     # dividing cps_wash by 3600 so that it is in hours, not seconds
}                    # closing the f string

(int(                # int() can be used similar to =ROUNDDOWN() in Excel
cps_wash % 3600)     # taking the remainder of cps_wash using %
/ 60)}               # dividing by 60 so the remainder is in minutes, not seconds

"""