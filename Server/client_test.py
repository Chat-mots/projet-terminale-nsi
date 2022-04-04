from email import message
import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_client.connect(('localhost',2022))
print("connection")

try:
    message = "bonjour"
    print("sending : ", message)
    socket_client.sendall(message)

    data = socket_client.recv(1)
    # amount_received += amount_expected
    print("recu", data)

finally:
    socket_client.close()