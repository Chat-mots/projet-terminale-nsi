import socket

class Server:
    def __init__(self, ip_server, port) -> None:
        self.ip_server = ip_server
        self.port = port

    def start_server(self):
         