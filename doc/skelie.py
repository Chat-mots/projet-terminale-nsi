#!/bin/python3
class Objet():
    def colision(x, y):
        """
        Parametres :
            Les coordonées du joueur qui rentre en colision sous forme de deux enteir x, y.
        Retour :
            Aucun cette fonction applique simplement les effets
        ---
        """
        pass

    def afficher():
        """
        Cette fonction ne prend aucun parametre
        Fait le rendu de l'objet sur l'écran
        """
        pass

    def click_event(x, y):
        """
        Parametre :
            Les coordonées du joueur (x,yà
        Retour:
            Aucun, applique l'effet de clic de l'objet si je curseur est sur l'objet.
        """
        pass

class Mur(Objet):
    def colision(x,y):
        pass


[ 
    [fonction_a_appeler, t, delta_t]
    [fonction_a_appeler, t, delta_t]
    [fonction_a_appeler, t, delta_t]
    [fonction_a_appeler, t, delta_t]
]

def execute(el):
    attente = next_shit_time-current_time
    if attente>0:
        sleep(attente)
