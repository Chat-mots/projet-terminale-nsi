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
    id = (mycursor.lastrowid,)
    # on insere dans les autres tables
    mycursor.execute(sql_badge, id)
    mycursor.execute(sql_stat, id)

    mydb.commit()


def ajoutermort(nbrmort, id):
    """ajoute le nombre de morts de la partie précedente au joueur


    :param int nbrmort: entier >= 0
    :param id: id du joueur (entier à 6 chiffres)
    :return: None
    """
    # on récupere le nombre de morts précedentes
    id_sp = (id,)
    sqlcall = "SELECT `nombre_morts` FROM `statistiques` WHERE `ID` = %s;"
    mycursor.execute(sqlcall, id_sp)
    morts_prec = mycursor.fetchall()
    morts_prec = morts_prec[0][0]
    print(morts_prec)
    nbrmort += int(morts_prec)

    # on remplace par le nouveau nombre de morts
    valeurs = (nbrmort, id)
    mycursor.execute("SELECT * FROM `statistiques`;")
    sql = "UPDATE `statistiques` SET `nombre_morts` = '%s' WHERE `statistiques`.`ID` = %s"
    mycursor.execute(sql, valeurs)

    # on vérifie si le nombre de mort permet d'avoir le badge
    if nbrmort > 100:
        sqlbad = "UPDATE `badges` SET `crevard` = '1' WHERE `badges`.`ID` = %s"
        mycursor.execute(sqlbad, id_sp)

    mydb.commit()


def ajoutertemps_de_jeu(id, temps):
    """ajoute le temps de jeu du joueur à ses statistiques

    ajoute au joueur le temps qu'il a passé à effectuer la partie (**elle s'additionne à ses temps précédents**)

    :param int id: id du joueur (entier à 6 chiffres)
    :param int temps: nombre de secondes
    :return: None
    """
    # on récupère le temps de jeu précedent
    id_sp = (id,)
    sqlcall = "SELECT `temps_de_jeu` FROM `statistiques` WHERE `ID` = %s;"
    mycursor.execute(sqlcall, id_sp)
    temps_prec = mycursor.fetchall()
    temps_prec = temps_prec[0][0]
    temps += int(temps_prec)

    # on remplace par le nouveau temps de jeu
    valeurs = (temps, id)
    mycursor.execute("SELECT * FROM `statistiques`;")
    sql = "UPDATE `statistiques` SET `temps_de_jeu` = '%s' WHERE `statistiques`.`ID` = %s"
    mycursor.execute(sql, valeurs)

    mydb.commit()


def modifierelo(id, elo):
    """modifie l'elo d'un joueur

    après avoir calculé l'elo à l'aide de la fonction de calcul (faite autre part), `modifierelo` met à jour l'elo du
    joueur dans la base de données.

    :param int id: id du joueur (entier à 6 chiffres)
    :param int elo: elo calcul, entier >= 0
    :return: None
    """
    # on récupère l'elo précedent
    eloprec = getelo(id)
    eloprec = int(eloprec)
    elo += eloprec

    # si le nouvel elo devient inférieur à 0, on le remets à 0
    if eloprec + elo < 0:
        print("inférieur à 0")
        id_tuple = (id,)
        sqlbas = "UPDATE `base` SET `ELO` = '0' WHERE `base`.`ID` = %s"
        mycursor.execute(sqlbas, id_tuple)
        mydb.commit()

    # on ajoute le nouvel elo
    valeurs = (elo, id)
    mycursor.execute("SELECT * FROM `base`;")
    sql = "UPDATE `base` SET `ELO` = '%s' WHERE `base`.`ID` = %s"
    mycursor.execute(sql, valeurs)
    mydb.commit()

    # on vérifie si il s'agit d'un nouveau record
    gethautelo = ("SELECT `plus_haut_ELO` FROM `statistiques` WHERE `ID` = %s;")
    mycursor.execute(gethautelo, (id,))
    haut_elo = mycursor.fetchall()[0][0]
    if elo > haut_elo:
        sqlhaut = "UPDATE `statistiques` SET `plus_haut_ELO` = '%s' WHERE `statistiques`.`ID` = %s"
        mycursor.execute(sqlhaut, valeurs)
        mydb.commit()


def getelo(id):
    """récupere l'elo d'un joueur d'id `id`


    :param int id: id du joueur (nombre à 6 chiffres)
    :return: int correspondant à l'elo du joueur
    """
    id_sp = (id,)
    sqlcall = "SELECT `ELO` FROM `base` WHERE `ID` = %s;"
    mycursor.execute(sqlcall, id_sp)
    eloprec = mycursor.fetchall()
    eloprec = eloprec[0][0]

    return eloprec


def changerpseudo(id, nouveaupseudo):
    """ change le pseudo d'un joueur d'id `id`


    :param int id: id du joueur (nombre à 6 chiffres)
    :param str nouveaupseudo: le nouveau pseudo du joueur
    :return: None
    """
    valeurs = (nouveaupseudo, id)
    mycursor.execute("SELECT * FROM `base`;")
    sql = "UPDATE `base` SET `pseudo` = %s WHERE `base`.`ID` = %s"
    mycursor.execute(sql, valeurs)

    mydb.commit()


def serievictoire(id, resultat):
    """gère les series de victoire à effectuer en fin de partie

    serievictoire gère les series de victoires à la fin de la partie, en fonction du classement du joueur.
    A partir de la position du joueur dans le classement, on ajoute 1 à sa série de victoire, ou on la remets à 0.

    :param int id: id du joueur (entier à 6 chiffres)
    :param int resultat: entier compris entre 1 et 8
    :return: None
    """
    sqlrecord = "SELECT `plus_grande_serie_de_victoire` from `statistiques` where `statistiques`.`id` = %s"
    mycursor.execute(sqlrecord, (id,))
    record = mycursor.fetchall()[0][0]
    sql = "SELECT `serie_de_victoire_actuelle` from `statistiques` where `statistiques`.`id` = %s"
    mycursor.execute(sql, (id,))
    serie_de_victoire = mycursor.fetchall()[0][0]

    if resultat <= 3:  # c'est une défaite
        # on ajoute 1 à la série de victoire
        valeurs = (serie_de_victoire+1, id)
        sqladd = "UPDATE `statistiques` SET `serie_de_victoire_actuelle` = '%s' WHERE `statistiques`.`ID` = %s;"
        mycursor.execute(sqladd, valeurs)
        mydb.commit()
        # on vérifie si c'est un nouveau record
        if serie_de_victoire+1 > record:
            sqlnouveaurecord = \
                "UPDATE `statistiques` SET `plus_grande_serie_de_victoire` = '%s' WHERE `statistiques`.`ID` = %s;"
            mycursor.execute(sqlnouveaurecord, valeurs)
            mydb.commit()

    else:  # c'est une défaite
        valeurs = (0, id)
        sqladd = "UPDATE `statistiques` SET `serie_de_victoire_actuelle` = '%s' WHERE `statistiques`.`ID` = %s;"
        mycursor.execute(sqladd, valeurs)
        mydb.commit()
