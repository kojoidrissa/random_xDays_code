#die rolling program inspired by "Introduction to Python" and my love of D&D 

import random as rnd

s = int(input("What die would you like to roll? Enter the number of sides "))

roll = rnd.randint(1, s)
print (roll)
