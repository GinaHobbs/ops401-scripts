#!/bin/python3

# import the datetime library
import datetime

# import the time library
import time

# import the os library
import os

# store the current time to a variable and print it to the terminal
now = datetime.datetime.now()
print("The current date and time is: ")
print(str(now))

while True:
    print("=======================================================")
    print("Start: %s" % time.ctime())
    time.sleep(2)
    print(os.system("ping -c 1 8.8.8.8"))
    print("End: %s" % time.ctime())
    print("=======================================================")


