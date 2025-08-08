'''
    Write a python program to print date, time for today and now

'''

from datetime import datetime, date                       # importing a specific class

now = datetime.now()                                      # class
print("Current date & time ",now)

today = date.today()
print("Today's date ", today)

strftime = now.strftime("%H:%M:%S")                      # string format time
print("Time in hrs, min, sec: ",strftime)

'''OR'''

'''

import datetime                                         # importing the whole module

# We can access classes or functions using:
now = datetime.datetime.now()                           # module.class

'''