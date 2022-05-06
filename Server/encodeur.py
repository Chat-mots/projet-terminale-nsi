import sys
import struct
import random
import ctypes

from matplotlib.pyplot import table


class Encodeur:
    """
    Classe encodeur, dont une instance sera possédée par chaque client.
    ---------------
    Attributs :
    ---------------
    str:trame = la dernière trame utilisée par l'encodeur
    X:valeur = la dernière valeur encodée par l'encodeur
    bytes:message = le dernier message créé par l'encodeur
    str:format = Le dernier format utilisé par struct
    bool:message_multicast  = Si le prochain message créée doit être multicasté, ce qui est le considéré comme étant le
    cas de base
    ---------------
    Méthodes :
    ---------------
    encode(X:valeur) -> bytes:message => Encode une valeur selon une trame spécifique
    Il existera ensuite une fonction d'encodage pour chaque trame (cf : trame.md) qui renverront bytes:message
    """

    def __init__(self):
        self.trame = None
        self.valeur = None
        self.message = None
        self.format = None
        self.message_multicast = True

    def encode(self, trame, valeur):
        self.valeur = valeur
        self.trame = trame
        self.message_multicast = True

        if self.trame == 'IDJ':
            self.IDJ()
        if self.message_multicast == True:

            return bytes("MC", 'utf-8') + self.message
        else:
            return bytes("MV", 'utf-8') + self.message
    def IDJ(self):
        """ Encodeur pour la trame Id de joueur
        """
        self.format = 'i'

        data = struct.pack(self.format, self.valeur)

        trame = bytes(self.trame, 'utf-8')
        self.message = trame + data


if __name__ == "__main__":
    nombre_en_str = bytes("IDJ513315", 'utf-8')
    str_convert = 'IDJ'
    nombre_avec_struct = struct.pack('is', 513315, str_convert.encode('utf-8'))
    print(sys.getsizeof(nombre_en_str))
    print(sys.getsizeof(nombre_avec_struct))
    # tableau_direct = struct.pack('%si' %len(tableau), *tableau)
    e = Encodeur()
    print(e.encode('IDJ', 5))
