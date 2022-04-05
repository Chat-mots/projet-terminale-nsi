import socket
import struct
import sys

multicast_group = '224.3.29.71'
server_address = ('192.168.43.242', 10455)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(1024)
    print("receive :", data, "from :", address)
