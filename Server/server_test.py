import imp


import socket
import sys

socket_ecoute = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_ecoute.bind(('localhost',2022))

socket_ecoute.listen(1)

while True:
    print("waiting for a connection")
    connection, client_address = socket_ecoute.accept()

    try:
        print("connection depuis", client_address)
        connected = True
        while connected:
            data = connection.recv(16)
            if data:
                print("recu : ", data)
                print("renvoie")
                connection.sendall(data)
            else:
                print("plus de données de : ", client_address)
                connected = False
    
    finally:
        connection.close()



    

