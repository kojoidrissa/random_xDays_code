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


d20 = die(20)
# print(d6.roll)
# print(d20)
who = d20.roll()
print (who)
