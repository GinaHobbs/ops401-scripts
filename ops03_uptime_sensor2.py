#!/bin/python3
#Script Name: ops02.py
#Author: Gina Hobbs
#Date of last revision: 06 April 2022
#Description of purpose: Send pings to a network every 2 seconds
#Declaration of variables: ping, now
#Declaration of functions (if used):

# import the datetime, os, time and smtplib library
import datetime,time,os,smtplib

# store the current time to a variable
now = datetime.datetime.now()

def mail(ping):
    # Email administrator
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()

    # Log in to the server
    server.login("email", "password")

    # Check the ping variable to see if network is up or down
    if ping == 0:
        msg = "The network is active."
    else:
        msg = "The network is inactive."

    # Send the mail
    server.sendmail("email", "email", msg)
    server.quit()

# Declare function check_ping
def check_ping(target):
    ping = os.system("ping -c 1 " + target)
    if ping == 0:
        print("Network Active")
    else:
        print("Network Inactive")
    return ping

while True:
    print("=======================================================")
    print("The current date and time is: " + str(now))
    ping = check_ping("8.8.8.8")
    mail(ping)
    time.sleep(2)
    print("=======================================================")


