import socket

host = '10.42.0.1'
port = 4005

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.bind((host, port))

serv = ('10.42.0.34', 4000)
msg = "Hello"
socket_client.connect(serv)
while msg != 'q':
    socket_client.send(msg.encode('utf-8'))
    data = socket_client.recv(1024)
    # data = data.decode('utf-8')
    print("Received from server : ", data)
    msg = input("->")
    print(msg)
socket_client.close()
