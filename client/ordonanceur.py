#!/bin/python3
import time

class processus:
    def __init__(self, fonction, args, deltat, tag):
        """
        Créer un processus 
        ---- Arguments
        fonction    : La fonction a appeler quand le processus est executé
        args        : Une liste qui contient les arguments a passer a la fonction quand
                      on execute le processus
        deltat      : Un entier, indique tout les combien de tick on execute le processus
                      on l'execute une seule fois si égal a 0.
        """
        self.fonction = fonction    #Une fonction a executer quand appelé par l'ordonanceur 
        self.args = args            #La liste des arguments de la fonction
        self.deltat = deltat        #Tout les combien de temps défiler l'instruction
        self.tag = tag              #Tag(ueule)

    def execute(self):
        self.fonction(*self.args)

class Ordonanceur:
    def __init__(self):
        #(processus, T)
        """
        Initialise un ordonanceur
        """
        self.file = []
        self.tick = 0
        self.ticksize = 1

    def enfiler(self, elem, time):
        """
        Ajoute un processus dans la file d'execution au tick time
        """
        taille_file = len(self.file)
        index = 0
        while (index < taille_file) and self.file[index][1] <= time:
            index += 1
        self.file.insert(index, (elem, time))
        
    def purge(self, tag):
        """
        Retire tout les processus avec un certain tag
        """
        for process in file:
            if process[0].tag == tag:
                del process

    def tick(self):
        """
        Cette méthode execute tout les processus qui doivent être executé et
        les remmet dans la file au temp aproprié.
        """
        while self.file[0][1] <= self.tick:
            self.file[0][0].execute()
            if self.file[0][0].deltat > 0: # On re enfile seulement si DeltaT est supérieur a 0
                self.enfiler(
                        self.file[0][0],
                        self.tick + self.file[0][0].deltat
                        )
            del self.file[0]
        self.tick += 1

    def start():
        """
        Cette méthode lance l'ordonanceur et execute des tick a un intérval régulier.
        """
        while True:
            T0 = time.time()
            self.tick()
            T1 = time.time()
            if (T1 - T0) > 0:
                sleep(T1-T0)

### Partie de test

def addprint(a, b):
    """
    Fonction de test pour vérifier l'execution de processus avec plusieurs arguments
    """
    print(a+b)

if __name__=="__main__":
    print("creating processus object")
    proto = processus(print, ['a'], 1, 1)
    momo = processus(addprint, [1, 2], 1, 1)
    print("testing processus.execute()")
    proto.execute()
    momo.execute()
    
