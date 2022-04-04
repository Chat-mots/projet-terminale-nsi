from email import message
import socket
import struct
import sys

msg = "ultra important UwU"
multicast_group = ('224.3.29.71', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(0.2)

ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
    print("sending", msg)
    sent = sock.sendto(bytes(msg, "utf-8"), multicast_group)

    while True:
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print('timed out, no more responses')
            break
        else:
            print('received "%s" from %s', (data, server))

finally:
    print('closing socket')
    sock.close()
