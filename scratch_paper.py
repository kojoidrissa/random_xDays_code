# This is where I try various things I'm learning or read in docs

## Try/Except blocks 2017-10-19T13:28:14-05:00

import sys

while True:
	try:
		x = int(input("Please enter a number: "))
		break
	except Exception as e:
		print ("Oops! That wasn't a valid number.\nA {} error occured: \n*** {} ***. \nPlease try again""".format(type(e),e))
		print(sys.exc_info()[1])
