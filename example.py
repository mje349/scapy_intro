import sys
from scapy.all import *

ip_input = raw_input("please enter an IP address: ")
print("You entered: ", ip_input)

l3 = IP(dst=ip_input)/TCP()
l2 = Ether() / l3
l2.show()
