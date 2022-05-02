
import socket
import sys

host = '10.42.0.34'
port = 4000

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((host, port))
print("Server started")

socket_server.listen(5)
socket_client, address = socket_server.accept()
while True:
        data = socket_client.recv(1024)
        data = data.decode('utf-8')
        print("Message from : ", address)
        print("Data : ", data)
        data = data.upper()
        print("Sending :", data)
        socket_client.send(data.encode('utf-8'))
