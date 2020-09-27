# Author: Montana Esguerra
# Description: Intro to ScaPy

import sys
from scapy.all import *

ip_input = raw_input("Please enter an IP addres: ")

subnet_mask = raw_input("Please enter a subnet mask in CIDR: ")

cidr_format = ip_input + '/' subnet_mask

ip_range = IP(dst = cidr_format) / TCP(dport=[53,80])
ip_network = []
