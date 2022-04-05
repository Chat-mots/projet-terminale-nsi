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
    morts_prec = str(mycursor.fetchall())
    morts_prec = morts_prec[2:]
    morts_prec = morts_prec[:1]
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


ajoutermort(33, 100011)
