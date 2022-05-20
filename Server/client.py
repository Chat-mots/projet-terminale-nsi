#!/usr/bin/python
# -*- coding: utf-8 -*-

from decodeur import Decodeur
from encodeur import Encodeur
import socket
import struct
import sys


class Client:
    """
    Classe client, dont le but est de se connecter au serveur

    Attributs:
    decodeur:decodeur : Une instance de la classe décodeur
    encodeur:encodeur : Une instance de la classe encodeur
    str:host : L'host du client
    int:port : Le port du client
    socket:client_multicast : Le socket qui s'occupera des dialogues multicast avec le serveur
    socket:client_ping : Le sokcet qui s'occupera des dialogues constants avec le serveur

    Méthodes :
    get_host_ip : récupères l'ip de la machine du client
    connect : Connectes un client au serveur
    send : Envoies un message au serveur
    receive : Se prépare à recevoir un message du serveur
    """

    def __init__(self, port):
        """
        Methode init

        Se lance à la création de l'instance

        :param int port: Le port du premier socket du client
        :return None:
        """

        self.host = self.get_host_ip()
        self.port = port
        self.encodeur = Encodeur()
        self.decodeur = Decodeur()
        self.client_multicast = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def get_host_ip(self):
        """
        Fonction get_host_ip

        Permet d'obtenir l'adresse IP de la machine où est lancée la fonction

        :return: str
        """

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

    def start_client(self, server_host, server_port):
        '''
        Fonction start_client

        Démarres les deux sockets du client

        :param str server_host: l'ip du serveur
        :param int server_port: Le port du serveur
        :return None:
        '''

        self.client_multicast.bind((self.host, self.port))
        print("bind")
        self.client_multicast.connect((server_host, server_port))
        print("Connecté au serveur")


    def send(self, trame, valeur):
        """
        Fonction send

        Envoies un message au serveur, après l'avoir traduit en bytes grâce à l'encodeur

        :param str trame: La trame du message
        :param X valeur: La valeur qu'on veut envoyé
        :return None:
        """

        message = self.encodeur.encode(trame, valeur, True)
        print(type(message))
        print("Envoi de : ", message)
        self.client_multicast.send(message)
        print("bien envoyé")

if __name__ == "__main__":
    client = Client(int(input("port: ")))
    client.start_client('192.168.43.235', 4500)
    client.send('IDJ', 5)

