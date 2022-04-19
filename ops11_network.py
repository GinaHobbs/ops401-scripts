#!/bin/python3
#Script Name: ops11_network.py
#Author: Gina Hobbs
#Date of last revision: 18 April 2022
#Description of purpose: 
#Declaration of variables: 
#Declaration of functions (if used):

#import libraries
import sys
from scapy.all import sr1,IP,ICMP,TCP

#define target host and TCP port to scan

host = "scanme.nmap.org"
port_range = 22
src_port = 22
dst_port = 22

response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port),timeout=1,verbose=0)

print(response)