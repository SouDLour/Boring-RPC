import math as mt
import random


# Probability Function:

# Purpose of function was to assign a float to the option of the user and one to
# the bot. The number thats greatest is equivalent to that side of the coin tossed.

# Obviously didn't have to do this and could've used random.choice() for H or T, but the 
# Purpose of this project was to work with mltiple python files & To relearn python after
# 3+ months of not using python.

def probability():
    chanceOne = mt.sqrt(.50)
    chanceTwo = mt.sqrt(.501)
    fate = random.randint(1,10)
    stroke = mt.pi*chanceOne / fate** chanceTwo % 50 / 2
    return stroke

#compare Function:

# This compares the number assigned to the usr or the bot. By Default the usr choice is on the left,
# and is always compared to the bot choice on the right. Purpose is to just print a message letting
# User know which number was greater

# Output:
#    [User Number] is greater than [Bot Number] 
#       [User Number] is less than [Bot Number] 
#           [User Number] is greater than [Bot Number] 

# Note: Will not be used on from 'file' import [def] / Was Removed

# Needed for Console_Version to run.

def compare(usrChoice,btChoice):
    if usrChoice > btChoice:
        print(usrChoice, 'is greater than', btChoice)
    elif usrChoice < btChoice:
        print(usrChoice, 'is less than', btChoice)
    else:
        print(usrChoice, 'is equal to ', btChoice)
    



    

