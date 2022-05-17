#!/usr/bin/python
# -*- coding: utf-8 -*-
from encodeur import Encodeur
import struct
import sys
class Decodeur:
    '''
    Classe du décodeur qui sera possédé par chaque client
    ---------------
    Attributs :
    ---------------
    str:trame = La trame de la dernière valeur reçue
    X:valeur = La dernière valeur reçue
    bytes:message = le dernier message reçu
    str:format = Le dernier format pour struct reçu
    ---------------
    Méthodes :
    ---------------


    '''
