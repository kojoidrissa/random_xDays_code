#die rolling program inspired by "Introduction to Python" and my love of D&D 

import random as rnd

#Update this to include a loop that lets you keep rolling and an option to end (break)
#when the input is "End". I should only convert the input to an int
#AFTER I've determined that it's not "End". Eventually I'll want to test for
#non-valid entries (non-numbers), but I'm not sure how to do that yet. :-)

s = int(input("What die would you like to roll? Enter the number of sides "))

roll = rnd.randint(1, s)
print (roll)
