from email import message
import socket

host = '192.168.43.235'
port = 4005

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.bind((host, port))

serv = ('192.168.43.242',4000)
msg = "Hello"
while message != 'q':
    socket_client.sendall(msg.encode('utf-8'), serv)
    data, addr = socket_client.recvfrom(1024)
    data = data.decode('utf-8')
    print("Received from server : ", data)
    msg = input("->")
socket_client.close()
