#!/bin/python3
#Script Name: ops11_network.py
#Author: Gina Hobbs
#Date of last revision: 18 April 2022
#Description of purpose: 
#Declaration of variables: 
#Declaration of functions (if used):

# Code taken from:
# https://thepacketgeek.com/scapy/building-network-tools/part-10/
import random
import ipaddress
from scapy.all import ICMP, IP, sr1, TCP, sr

# Define end host and TCP port range
host = "scanme.nmap.org"
#host = "192.168.1.212"
network = '192.168.1.0/24'
ip_list = ipaddress.ip_network(network)
port_range = [22, 23, 80, 443, 3389]
count = 0

print("1: TCP Port Range Scanner")
print("2: ICMP Ping Sweep")
option = input("Please enter a selection.")

if option == '1':
    # Send SYN with random Src Port for each Dst port
    for dst_port in port_range:
        src_port = random.randint(1025,65534)
        resp = sr1(
            IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,
            verbose=0,
        )

        if resp is None:
            print(f"{host}:{dst_port} is filtered (silently dropped).")

        elif(resp.haslayer(TCP)):
            if(resp.getlayer(TCP).flags == 0x12):
                # Send a gratuitous RST to close the connection
                send_rst = sr(
                    IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),
                    timeout=1,
                    verbose=0,
                )
                print(f"{host}:{dst_port} is open.")

            elif (resp.getlayer(TCP).flags == 0x14):
                print(f"{host}:{dst_port} is closed.")

            
elif option == '2':
    network = input("Please input the network using CIDR notation.")
    ip_list = ipaddress.ip_network(network, False)

    for host in ip_list:
        src_port = random.randint(1025,65534)
        resp = sr1(
            IP(dst=host)
        )

        if resp is None:
            print(f"{host} is down or unresponsive.")

        elif(resp.haslayer(ICMP)):
            if(
                int(resp.getlayer(ICMP).type) == 3 and
                int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
            ):
                print(f"{host} is actively blocking ICMP traffic")
        else:
            print(f"{host} is responding.")
            count += 1
    print("There are " + count + " hosts online.")
