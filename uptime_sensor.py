#!/bin/python3
#Script Name: ops02.py
#Author: Gina Hobbs
#Date of last revision: 06 April 2022
#Description of purpose: Send pings to a network every 2 seconds
#Declaration of variables: ping, now
#Declaration of functions (if used):

# import the datetime, os and time library
import datetime,time,os

# store the current time to a variable
now = datetime.datetime.now()

# Declare function check_ping
def check_ping(target):
    ping = os.system("ping -c 1 " + target)
    if ping == 0:
        print("Network Active")
    else:
        print("Network Inactive")

while True:
    print("=======================================================")
    print("The current date and time is: " + str(now))
    check_ping("8.8.8.8")
    time.sleep(2)
    print("=======================================================")


