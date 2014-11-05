##My effort to code a die object
import random as rnd
from datetime import datetime as dt

##Now I'll try to create a die object that I can use
class die():
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        print (rnd.randint(1, int(self.sides)))