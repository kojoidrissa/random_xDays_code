from halo import Halo # pip install halo first
import time
 
spinner = Halo({'text': 'Calculating...',  'color': 'red','spinner': 'dots8'})
spinner.start()
counter = 0
while counter < 51:
                # print(counter)
                counter += 1
                time.sleep(.1)
# Run time consuming work here
# You can also change properties for spinner as and when you want
 
# spinner.stop()
spinner.succeed()