#die rolling program inspired by "Introduction to Python" and my love of D&D 

import random as rnd
from datetime import datetime as dt

f = open("dice_log.txt", "w")
#Can I concatenate a timestamp string to the end of the file name, to make a new log file
#each time I run this? Now it's just overwriting the file, 
#which is fine for testing, not production

#Eventually I'll want to test for non-valid entries (non-numbers)
#but I'm not sure how to do that yet. :-)

#Now I need to make 'end' non-case sensitive. Or, do I want to use a try/exception here, to CATCH
#the error?

#Also, it might be nice to capture the rolls to a log file, for reference. I'll use UTC timestamps
#to identify each roll

#I also need to include an option to roll multiple dice at once, like 2d6.

while True:
    s = input("What die would you like to roll? Enter the number of sides. Or enter 'End' to quit ")
    if s == "End":
        break
    else:
        s = int(s)

    die = ("d" + str(s)) #for capturing the TYPE of die rolled

    roll = rnd.randint(1, s)
    timestamp = str(dt.utcnow())#since f.write() only takes strings, I'm converting dt.utcnow()
    #from it's native type, 'datetime.datetime'
    print (roll)
    roll_string = str(roll) #converting to string because that's all f.write() will take
    f.write(die + "," + roll_string + "," + timestamp + "\n")

f.close()
