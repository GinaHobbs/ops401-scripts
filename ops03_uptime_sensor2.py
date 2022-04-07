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

# Set ping flag for mail
old_ping_status = "none"

def mail(ping_status, old_ping_status):
    # Email administrator
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()

    # Log in to the server
    server.login("ginamariehobbs@gmail.com", "password")

    # Check the ping variable to see if network is up or down
    if ping_status != old_ping_status:
        msg = "The network has changed. It is now " + ping_status + "."
        server.sendmail("ginamariehobbs@gmail.com", "ginamariehobbs@gmail.com", msg)
        server.quit()

# Declare function check_ping
def check_ping(target):
    ping = os.system("ping -c 1 " + target)
    if ping == 0:
        print("Network Active")
        ping_status = "up"
    else:
        print("Network Inactive")
        ping_status = "down"
    return ping_status

while True:
    print("=======================================================")
    print("The current date and time is: " + str(now))
    ping_status = check_ping("8.8.8.8")
    mail(ping_status, old_ping_status)
    old_ping_status = ping_status
    time.sleep(2)
    print("=======================================================")