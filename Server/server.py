import socket

class Server:
    '''
    Classe du serveur qui va gérer les threads clients, les communications entre clients et serveurs

    Attributs :
    ---------------
    str:ip : L'IP du serveur. Elle doit être fixe
    int:port : Le port du serveur

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
        self.ip = self.get_host_ip()

    def get_host_ip(self) -> str:
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

if __name__ == "__main__":
    server = Server(4500)
    server.get_host_ip()
    print(server.ip)