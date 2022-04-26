def rapport_classement(index):
    '''
    fonction renvoyant une valeure allant de 100 à -100 suivant le classement du joueur.
    :param index: entier appatrtenant à [0;7]. Si l'entier est 0, le joueur est premier. Si l'entier est 7, le joueur est 8e.
    :return: valeur: valeur de base à additionner au joueur, avant l'application du coef par rapport à l'Elo moyen de la partie.
    '''
    points = 100- (200/7)*index
    return points

def rapport_moyenne_elo(resultats,index):
    '''
    fonction renvoyant le coefficient à appliquer à la valeur d'Elo à additionner pour un joueur donné.
    :param liste_elo_joueur: liste de l'Elo de chaque joueur, triés par le classement de chaque joueur.
    :param index_joueur: l'index du joueur représentatif de son classement, index étant un entier appatrtenant à [0;7]. Si l'entier est 0, le joueur est premier. Si l'entier est 7, le joueur est 8e.
    :return: coef: le coefficient à appliquer à la valeur d'Elo à additionner pour un joueur donné.
    '''
    somme_pts = 0
    taille_resultats = len(resultats)
    moyenne = 0
    pts_joueur =resultats[index]
    rapport = 1
    for i in range(taille_resultats):
        if i != index :
            somme_pts += resultats[i]
    moyenne = somme_pts/(taille_resultats-1)
    if moyenne == 0:
        moyenne = 0.001
    if pts_joueur == 0:
        pts_joueur = 0.001
    if moyenne < 0:
        if pts_joueur < 0:
            rapport = pts_joueur/moyenne
        else:
            rapport = moyenne/(moyenne-pts_joueur)
    elif pts_joueur < 0:
        rapport = (pts_joueur-moyenne)/pts_joueur
    else:
        rapport = moyenne/pts_joueur
    return rapport

def coef_gain(moyenne):
    assert moyenne>0,"moyenne must be positive"
    coef = 1
    if moyenne < 0.0001:
        coef = 0.01
    elif moyenne<13.97:
        coef = moyenne**0.5
    elif moyenne < 1517:
        coef = (5/6)*(moyenne**0.15)+2.5
    else:
        coef = 5
    return coef

def coef_perte(moyenne):
    assert moyenne>0,"moyenne must be positive"
    coef = 1
    if moyenne < 2.666:
        coef = -moyenne**0.7+2
    elif moyenne < 10322:
        coef = -1*((moyenne**0.15)/10)+0.401
    else:
        coef = 0.1
    return coef
  
def calcul_elo(resultats,index):
    '''
    fonction qui calcule l'ELO d'un joueur en fonction de son classement et du nombre de points des autres joueurs.
    -------------------------------
    paramètres:
    resultats: liste de 8 valeurs correspondant aux ELO de chaque joueur dans l'ordre d'arrivée au classement.
    index : nombre entier entre 0 et 7 correspondant à la place du joueur cherché. 0 pour le premier, 7 pour le 8e.
    -------------------------------
    return:
    Les points à additionner au joueur choisi.
    '''
    cl = rapport_classement(index)
    moy = rapport_moyenne_ELO(resultats,index)
    if cl<0:
        coef = coef_perte(moy)
    else:
        coef = coef_gain(moy)
    return cl*coef
