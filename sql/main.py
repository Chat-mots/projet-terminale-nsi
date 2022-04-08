import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='victor',
    password='azerty',
    database='jeu_nsi'
)

mycursor = mydb.cursor(buffered=True)


def creerjoueur(pseudo):
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
        return "inférieur à 0"

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

        return "Nouveau record !"


def getelo(id):
    id_sp = (id,)
    sqlcall = "SELECT `ELO` FROM `base` WHERE `ID` = %s;"
    mycursor.execute(sqlcall, id_sp)
    eloprec = mycursor.fetchall()
    eloprec = eloprec[0][0]

    return eloprec


def changerpseudo(id, nouveaupseudo):
    valeurs = (nouveaupseudo, id)
    mycursor.execute("SELECT * FROM `base`;")
    sql = "UPDATE `base` SET `pseudo` = %s WHERE `base`.`ID` = %s"
    mycursor.execute(sql, valeurs)

    mydb.commit()


def seriedevictoire(id, resultat):
    sql = "SELECT `serie_de_victoire_actuelle` from `statistiques` where `statistiques`.`id` = %s"
    mycursor.execute(sql, (id,))
    serie_de_victoire = mycursor.fetchall()[0][0]
    sqlrecord = "SELECT `plus_grande_serie_de_victoire` from `statistiques` where `statistiques`.`id` = %s"
    mycursor.execute(sql, (id,))
    if resultat > 0:
        # on ajoute 1 à la série de victoire
        valeurs = (serie_de_victoire+1, id)
        sqladd = "UPDATE `statistiques` SET `serie_de_victoire_actuelle` = '%s' WHERE `statistiques`.`ID` = %s;"
        mycursor.execute(sqladd, valeurs)
        mydb.commit()
        # on vérifie si c'est un nouveau record
        if serie_de_victoire+1 >
