import socket
from _thread import *
import threading
import time
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
        self.sender_multicast = self.init_multicast()

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

    # def start_server(self):
        '''
        Fonction start_server

        Démarres le serveur, qui attendra des connexions qu'il mettra en thread

        :return None:
        '''
        # self.socket_server.bind((self.host, self.port))
        # print("Server started")
        # print("Connecté à l'adresse : "+self.host+" sur le port "+str(self.port))

        # self.socket_server.listen(5)
        # socket_client, address = self.socket_server.accept()

        # while True:
            # print("connecté ! ", address)
            # message = socket_client.recv(1024)
            # print(message is None)
            # print(message)

    def hub(self, client):
        '''
        Fonction hub

        Ce sera la fonction qu'on ira thread. Elle reçoit le messsage, vérifie son utilité via la trame et fait quelque
        chose en conséquence.

        :param bytes message: Le message reçu
        :param Client client: Le client avec qui le thread dialogue
        :return None:
        '''

        data_type = client.recv(2)
        data_trame = client.recv(3)
        data  = client.recv(1024)
        type_msg = data_type.decode('utf-8')
        trame = data_trame.decode('utf-8')
        print(data_type, data_trame)
        if type_msg == "MC":
            msg = data_trame+data
            print(msg)

    def init_multicast(self):
        '''
        Fonction init_multicast

        Fonction utilisée par __init__ pour créer le socket qui dialoguera en multicast

        :return None:
        '''
        MCAST_GRP = '224.1.1.1'
        MCAST_PORT = 5007
        MULTICAST_TTL = 2
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

        return sock

    def multicast(self, message):
        '''
        Fonction multicast

        Fonction qui sert au serveur à envoyer à tous les clients un message en multicast.

        :param bytes message: Le message à envoyer
        :return None:
        '''





if __name__ == "__main__":
    server = Server(4500)
    # server.start_server()
    host = server.host
    port = 4500

    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind((host, port))
    print("Server started")

    socket_server.listen(5)
    while True:
        socket_client, address = socket_server.accept()
        # data = socket_client.recv(1024)
        t = start_new_thread(server.hub, (socket_client,))
        print(t)
        # data = data.decode('utf-8')
        # print("Message from : ", address)
        # print("Data : ", data)
        # data = data.upper()
        # print("Sending :", data)
        # socket_client.send(data.encode('utf-8'))
