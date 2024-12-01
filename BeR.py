import socket
import sys
import scapy.all as scapy
from scapy.data import *
import os
import sys

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(socket.gethostname())

request = scapy.ARP()

print("Your Computer Name is: " + hostname)
print("Your Computer IP Address is: " + IPAddr)

print(request)
