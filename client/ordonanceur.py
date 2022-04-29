#!/bin/python3

class executable:
    def __init__(self, fonction, args, deltat, tag):
        self.fonction = fonction    #Une fonction a executer quand appelé par l'ordonanceur 
        self.args = args            #La liste des arguments de la fonction
        self.deltat = deltat        #Tout les combien de temps défiler l'instruction
        self.tag = tag              #Tag(ueule)

    def execute(self):
        self.fonction(*self.args)

class Ordonanceur:
    def __init__(self):
        #(executable, T)
        self.file = []
        self.tick = 0

    def enfiler(self, elem, time):
        taille_file = len(self.file)
        index = 0
        while (index < taille_file) and self.file[index][1] <= time:
            index += 1
        self.file.insert(index, (elem, time))
        

    def tick(self):
        while self.file[0][1] <= self.tick:

if __name__=="__main__":

