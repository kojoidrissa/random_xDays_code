##My effort to code a die object
import random as rnd
from datetime import datetime as dt

##Now I'll try to create a die object that I can use
class die():
    def __init__(self, sides):
        self.sides = sides
        # print (rnd.randint(1, int(self.sides)))

    def roll(self):
        result = (rnd.randint(1, int(self.sides)))
        return result

die_num = input("How many dice would you like to roll? ")
die_sides = input("What sided die would you like to roll? ")

newdie = die(die_sides)

for i in range(0, int(die_num)):
    print(newdie.roll())
    

# d20 = die(20)
# # print(d6.roll)
# # print(d20)
# who = d20.roll()
# print (who)
