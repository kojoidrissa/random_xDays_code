#die rolling program inspired by "Introduction to Python" and my love of D&D 

import random as rnd
from datetime import datetime as dt

def new_log_file():
    '''
    creates a NEW log file with a UTC timestamp in the name
    I'm not going to use this NOW, as it will create a new log file every time I run this code
    which is something I don't want at the moment
    '''

    #How would I change this to make it a stand-alone module?
    #This may be my activity for 2014-10-20 in the evening

    logstamp = str(dt.utcnow())
    logname = "dice_log_" + logstamp + ".txt"
    f = open(logname, "x")

#I'm going with the "append to existing file" option
f = open("dice_log.txt", "a")
'''I found TWO solutions to my problem, in terms of file modes 'x' and 'a':
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    So, I should be able to create a new file with a timestamp, OR just keep appending
    to the end of an existing file, depending on the timestamp of each new entry. Now
    to consider which option I prefer.
'''

#Can I concatenate a timestamp string to the end of the file name, to make a new log file
#each time I run this? Now it's just overwriting the file, 
#which is fine for testing, not production
    #See "new_log_file()"

#Eventually I'll want to test for non-valid entries (non-numbers)
#but I'm not sure how to do that yet. :-)
    #DONE
#Now I need to make 'end' non-case sensitive. Or, do I want to use a try/exception here, to CATCH
#the error?
    #went with the try/except
#Also, it might be nice to capture the rolls to a log file, for reference. I'll use UTC timestamps
#to identify each roll
    #DONE
#I also need to include an option to roll multiple dice at once, like 2d6.

while True:
    s = input("What die would you like to roll? Enter the number of sides. Or enter 'End' to quit | ")
    if s == "End":
        break

    #I'd originally had the "s = int(s)" statement below in an 'else' clause of the if above
    #but realized I didn't need it
    #now I'm using try/except to test for invalid input
    try:
        s = int(s)
        die = ("d" + str(s)) #for capturing the TYPE of die rolled

        roll = rnd.randint(1, s)
        timestamp = str(dt.utcnow())#since f.write() only takes strings, I'm converting dt.utcnow()
        #from it's native type, 'datetime.datetime'
        print (roll)
        roll_string = str(roll) #converting to string because that's all f.write() will take
        f.write(die + "," + roll_string + "," + timestamp + "\n")

    except:
        print()
        print("You must enter an integer. That's a whole number. Like 7. You entered " + s.upper())


f.close()

