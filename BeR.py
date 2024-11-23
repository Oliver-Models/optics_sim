import socket
import sys
import scapy

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(socket.gethostname())

print("Your Computer Name is: " + hostname)
print("Your Computer IP Address is: " + IPAddr)


def scan_network(ip_range):
    # Create an ARP request to broadcast
    arp_request = ARP(pdst=ip_range)  # Set the target IP range
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")  # Ethernet broadcast
    arp_request_broadcast = broadcast / arp_request  # Combine ARP and Ethernet frames

    # Send the request and receive responses
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    devices = []
    for sent, received in answered_list:
        devices.append({'IP': received.psrc, 'MAC': received.hwsrc})

    return devices

def print_devices(devices):
    print("Available Devices in the Network:")
    print("-" * 40)
    print("{:<20} {:<20}".format("IP Address", "MAC Address"))
    print("-" * 40)
    for device in devices:
        print("{:<20} {:<20}".format(device['IP'], device['MAC']))

# Example: Scan a common IP range (adjust for your network)
ip_range = "192.168.1.1/24"  # Replace with your network's IP range
devices = scan_network(ip_range)
print_devices(devices)
