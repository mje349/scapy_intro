# Author: Montana Esguerra
# Date: 9/14/20
# Description: Intro to ScaPy

import sys
from scapy.all import *
from netaddr import IPNetwork


ip_input = raw_input("Please enter an IP address: ")
print("You entered", ip_input)

subnet_mask = raw_input("Please enter a subnet mask in cidr: ")
print("You entered" , subnet_mask)

cidr_format = ip_input + '/' + subnet_mask
print("CIDR Format: ", cidr_format)

ip_range = IP(dst = cidr_format) / TCP(dport=[53,80]) 
ip_network = []

# Traverse the ip range of the ip address with the associated subnet mask
for i in ip_range:
    ip_network.append(i)

# Remove the first element: network address | remove the last element: broadcast address
ip_network.pop()
ip_network.pop()

ip_network.reverse()

ip_network.pop()
ip_network.pop()

ip_network.reverse()

#ip_network.pop([ip_network.len() - 1])


for i in ip_network:
    #i.show()
    print(i.dst, i.dport)

#print("Broadcast Address: ", ip_range.broadcast)
#print("Network Address: ", ip_range.network)
