import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='victor',
    password='azerty',
    database='jeu_nsi'
)

mycursor = mydb.cursor(buffered=True)


def creerjoueur(pseudo):
    """crée un joueur dans la base de donnée

    ajoute un joueur dans la bdd, lui crée un `id` et tout ce qui va avec.

    :param str pseudo: pseudo du joueur
    :return: None
    """
    pseudo = (pseudo,)
    sql = "INSERT INTO `base` (`pseudo`) VALUES (%s);"
    sql_stat = "INSERT INTO statistiques (ID) VALUES (%s);"
    sql_badge = "INSERT INTO badges (ID) VALUES (%s);"
    # on insere dans la table base
    mycursor.execute(sql, pseudo)
    idjoueur = (mycursor.lastrowid,)
    # on insere dans les autres tables
    mycursor.execute(sql_badge, idjoueur)
    mycursor.execute(sql_stat, idjoueur)

    mydb.commit()


def ajoutermort(nbrmort, idjoueur):
    """ajoute le nombre de morts de la partie précedente au joueur


    :param int nbrmort: entier >= 0
    :param idjoueur: id du joueur (entier à 6 chiffres)
    :return: None
    """
    # on récupere le nombre de morts précedentes
    id_sp = (idjoueur,)
    sqlcall = "SELECT `nombre_morts` FROM `statistiques` WHERE `ID` = %s;"
    mycursor.execute(sqlcall, id_sp)
    morts_prec = mycursor.fetchall()
    morts_prec = morts_prec[0][0]
    print(morts_prec)
    nbrmort += int(morts_prec)

    # on remplace par le nouveau nombre de morts
    valeurs = (nbrmort, idjoueur)
    mycursor.execute("SELECT * FROM `statistiques`;")
    sql = "UPDATE `statistiques` SET `nombre_morts` = '%s' WHERE `statistiques`.`ID` = %s"
    mycursor.execute(sql, valeurs)

    # on vérifie si le nombre de mort permet d'avoir le badge
    if nbrmort > 100:
        sqlbad = "UPDATE `badges` SET `crevard` = '1' WHERE `badges`.`ID` = %s"
        mycursor.execute(sqlbad, id_sp)

    mydb.commit()


def ajoutertemps_de_jeu(idjoueur, temps):
    """ajoute le temps de jeu du joueur à ses statistiques

    ajoute au joueur le temps qu'il a passé à effectuer la partie (**elle s'additionne à ses temps précédents**)

    :param int idjoueur: id du joueur (entier à 6 chiffres)
    :param int temps: nombre de secondes
    :return: None
    """
    # on récupère le temps de jeu précedent
    id_sp = (idjoueur,)
    sqlcall = "SELECT `temps_de_jeu` FROM `statistiques` WHERE `ID` = %s;"
    mycursor.execute(sqlcall, id_sp)
    temps_prec = mycursor.fetchall()
    temps_prec = temps_prec[0][0]
    temps += int(temps_prec)

    # on remplace par le nouveau temps de jeu
    valeurs = (temps, idjoueur)
    mycursor.execute("SELECT * FROM `statistiques`;")
    sql = "UPDATE `statistiques` SET `temps_de_jeu` = '%s' WHERE `statistiques`.`ID` = %s"
    mycursor.execute(sql, valeurs)

    mydb.commit()


def modifierelo(idjoueur, elo):
    """modifie l'elo d'un joueur

    après avoir calculé l'elo à l'aide de la fonction de calcul (faite autre part), `modifierelo` met à jour l'elo du
    joueur dans la base de données.

    :param int idjoueur: id du joueur (entier à 6 chiffres)
    :param int elo: elo calcul, entier >= 0
    :return: None
    """
    # on récupère l'elo précedent
    eloprec = getelo(idjoueur)
    eloprec = int(eloprec)
    elo += eloprec

    # si le nouvel elo devient inférieur à 0, on le remets à 0
    if elo < 0:
        id_tuple = (idjoueur,)
        sqlbas = "UPDATE `base` SET `ELO` = '0' WHERE `base`.`ID` = %s"
        mycursor.execute(sqlbas, id_tuple)
        mydb.commit()
        return "inférieur à 0"

    # on ajoute le nouvel elo
    valeurs = (elo, idjoueur)
    mycursor.execute("SELECT * FROM `base`;")
    sql = "UPDATE `base` SET `ELO` = '%s' WHERE `base`.`ID` = %s"
    mycursor.execute(sql, valeurs)
    mydb.commit()

    # on vérifie si il s'agit d'un nouveau record
    gethautelo = "SELECT `plus_haut_ELO` FROM `statistiques` WHERE `ID` = %s;"
    mycursor.execute(gethautelo, (idjoueur,))
    haut_elo = mycursor.fetchall()[0][0]
    if elo > haut_elo:
        sqlhaut = "UPDATE `statistiques` SET `plus_haut_ELO` = '%s' WHERE `statistiques`.`ID` = %s"
        mycursor.execute(sqlhaut, valeurs)
        mydb.commit()


def getpseudo(idjoueur):
    """récupere le pseudo d'un joueur d'id `id`

    :param int idjoueur:
    :return:
    """
    id_sp = (idjoueur,)
    sqlcall = "SELECT `pseudo` FROM `base` WHERE `ID` = %s;"
    mycursor.execute(sqlcall, id_sp)
    pseudojoueur = mycursor.fetchall()
    pseudojoueur = pseudojoueur[0][0]

    return pseudojoueur


def getelo(idjoueur):
    """récupere l'elo d'un joueur d'id `id`


    :param int idjoueur: id du joueur (nombre à 6 chiffres)
    :return: int correspondant à l'elo du joueur
    """
    id_sp = (idjoueur,)
    sqlcall = "SELECT `ELO` FROM `base` WHERE `ID` = %s;"
    mycursor.execute(sqlcall, id_sp)
    eloprec = mycursor.fetchall()
    eloprec = eloprec[0][0]

    return eloprec


def changerpseudo(idjoueur, nouveaupseudo):
    """ change le pseudo d'un joueur d'id `id`


    :param int idjoueur: id du joueur (nombre à 6 chiffres)
    :param str nouveaupseudo: le nouveau pseudo du joueur
    :return: None
    """
    valeurs = (nouveaupseudo, idjoueur)
    mycursor.execute("SELECT * FROM `base`;")
    sql = "UPDATE `base` SET `pseudo` = %s WHERE `base`.`ID` = %s"
    mycursor.execute(sql, valeurs)

    mydb.commit()


def serievictoire(idjoueur, resultat):
    """gère les series de victoire à effectuer en fin de partie

    serievictoire gère les series de victoires à la fin de la partie, en fonction du classement du joueur.
    A partir de la position du joueur dans le classement, on ajoute 1 à sa série de victoire, ou on la remets à 0.

    :param int idjoueur: id du joueur (entier à 6 chiffres)
    :param int resultat: entier compris entre 1 et 8
    :return: None
    """
    sqlrecord = "SELECT `plus_grande_serie_de_victoire` from `statistiques` where `statistiques`.`id` = %s"
    mycursor.execute(sqlrecord, (idjoueur,))
    record = mycursor.fetchall()[0][0]
    sql = "SELECT `serie_de_victoire_actuelle` from `statistiques` where `statistiques`.`id` = %s"
    mycursor.execute(sql, (idjoueur,))
    serie_de_victoire = mycursor.fetchall()[0][0]

    if resultat <= 3:  # c'est une défaite
        # on ajoute 1 à la série de victoire
        valeurs = (serie_de_victoire + 1, idjoueur)
        sqladd = "UPDATE `statistiques` SET `serie_de_victoire_actuelle` = '%s' WHERE `statistiques`.`ID` = %s;"
        mycursor.execute(sqladd, valeurs)
        mydb.commit()
        # on vérifie si c'est un nouveau record
        if serie_de_victoire + 1 > record:
            sqlnouveaurecord = \
                "UPDATE `statistiques` SET `plus_grande_serie_de_victoire` = '%s' WHERE `statistiques`.`ID` = %s;"
            mycursor.execute(sqlnouveaurecord, valeurs)
            mydb.commit()

    else:  # c'est une défaite
        valeurs = (0, idjoueur)
        sqladd = "UPDATE `statistiques` SET `serie_de_victoire_actuelle` = '%s' WHERE `statistiques`.`ID` = %s;"
        mycursor.execute(sqladd, valeurs)
        mydb.commit()


def getstats(idjoueur, cherche):
    """cherche dans `statistiques` une valeur

    Dans la table `statistiques`, getstats va chercher
    dans la colonne "cherche" la valeur pour le joueur d'id `idjoueur`.

    :param int idjoueur: entier à 6 chiffres
    :param str cherche: nom de la colonne dans la table `statistiques` dans laquelle on effetue la recherche
    :return:
    """
    sqltest = "SELECT " + cherche + " FROM `statistiques` WHERE `ID` = " + str(idjoueur)
    mycursor.execute(sqltest)
    retour = mycursor.fetchone()
    retour = retour[0]

    return retour
