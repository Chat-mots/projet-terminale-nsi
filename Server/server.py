import socket
from _thread import *
import threading

class Server:
    '''
    Classe du serveur qui va gérer les threads clients, les communications entre clients et serveurs

    Attributs :
    ---------------
    str:host : L'IP du serveur. Elle doit être fixe
    int:port : Le port du serveur
    socket:socket_server : Une instance de la classe socket, permttant au serveur de se connecter au réseau

    Méthodes :
    ---------------
    start_server : démarre le serveur
    get_host_ip : Récupères l'ip de la machine
    '''

    def __init__(self, port):
        '''
        Fonction init

        :param int port: Le port du serveur
        :return:
        '''

        self.port = port
        self.host = self.get_host_ip()
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def get_host_ip(self):
        '''
        Fonction get_host_ip

        Permet d'obtenir l'adresse IP de la machine où est lancée la fonction

        :return: str
        '''

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    def start_server(self):
        '''
        Fonction start_server

        Démarres le serveur, qui attendra des connexions qu'il mettra en thread

        :return None:
        '''
        self.socket_server.bind((self.host, self.port))
        print("Server started")
        print("Connecté à l'adresse : "+self.host+" sur le port "+str(self.port))

        self.socket_server.listen(5)
        socket_client, address = self.socket_server.accept()

        while True:
            print("connecté ! ", address)
            message = socket_client.recv(1024)
            print(message is None)
            print(message)

    def hub(self, message):
        pass



if __name__ == "__main__":
    server = Server(4500)
    server.start_server()