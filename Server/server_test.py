from audioop import add
from distutils.log import FATAL
from http import server
import imp


import socket
import sys

from matplotlib.pyplot import close

host = '192.168.43.242'
port = 4000

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_server.bind((host, port))

print("Server started")
while True:
    data, addr = socket_server.recvfrom(1024)
    data = data.decode('utf-8')
    print("Message from : ", addr)
    print("Data : ", data)
    data = data.upper()
    print("Sending :", data)
    socket_server.sendto(data.encode('utf-8', addr))




    

