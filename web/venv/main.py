from flask import Flask, request, url_for, redirect
from markupsafe import escape
import sqljeu as msq
from wtforms import StringField, SubmitField

app = Flask(__name__)


class FlaskForm:
    pass


@app.route("/", methods=['POST', 'GET'])
def hello():
    return '''<!DOCTYPE html><head><title>JeuNSI</title>
    <link rel= "stylesheet" type= "text/css" href="/static/styles/mainpage.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
    </head>
    <body>
    <form action="/query" method="GET">

  <div class="form-group">
    <label>J'ai un compte : </label>
    <input type="text" class="form-control" id="username" name="username" placeholder="Votre ID (ex : 100000)">
  </div>\
    </form>
    <form action="/create" method="GET">
    <br>
        <div class="form-group">
            <label>Créer un compte : </label>
            <input type="text" class="form-control" id="pseudo" name="pseudo" placeholder="pseudo">
        </div>\
        </form>
        </body>'''


@app.route("/query", methods=['POST', 'GET'])
def querytest():
    # if key doesn't exist, returns None
    username = request.args.get('username')

    return '''<head><title>Mon compte - JeuNSI</title>
    <link rel= "stylesheet" type= "text/css" href="/static/styles/mainpage.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400&display=swap" rel="stylesheet">
    </head>
    <body>
    <a href="http://127.0.0.1:5000"> <button>retour menu</button> </a>
<h1>Mon compte</h1> <br> Bonjour ''' + (msq.getpseudo(username)) + '''<br>Changez de pseudo ici :
     <a href="http://127.0.0.1:5000/changepseudo?id=''' + username + '''" >
   <button>changer pseudo</button>
</a><br><br>
votre elo actuelle est : ''' + str(msq.getelo(username)) + '''. <br>
votre elo record est : ''' + str(msq.getstats(username, "plus_haut_ELO")) + '''. <br>
vous êtes mort ''' + str(msq.getstats(username, 'nombre_morts')) + ''' fois. <br>
vous avez fait ''' + str(msq.getstats(username, 'serie_de_victoire_actuelle')) + ''' victoires d'affilé et votre record 
est ''' + str(msq.getstats(username, 'plus_grande_serie_de_victoire')) + '''.
</body>'''.format(username)


@app.route("/create", methods=['POST', 'GET'])
def create():
    pseudo = request.args.get('pseudo')
    msq.creerjoueur(pseudo)

    return '''<head>
    <title> compte créé !</title> <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
</head>
    Votre compte a été créé ! Votre id est :''' + str(msq.getlastcreatedid()) + ''', notez-le bien il est important.<br>
    Votre pseudo est :''' + str(msq.getlastcreatedid())


@app.route("/changepseudo", methods=['POST', 'GET'])
def changepseudo():
    idjoueur = request.args.get('id')
    npseudo = request.args.get('nouveaupseudo')
    if npseudo is not None:
        msq.changerpseudo(idjoueur, npseudo)
        idjoueur = request.args.get('id')
        return '''<head><title>Changer mon pseudo</title>
    <link rel= "stylesheet" type= "text/css" href="/static/styles/mainpage.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
    </head>
    votre pseudo a été changé ! <br> <a href="http://127.0.0.1:5000/query?username=''' + idjoueur + '''">
   <button>retour au compte</button>'''
    return '''<head><title>Mon compte - JeuNSI</title>
    <link rel= "stylesheet" type= "text/css" href="/static/styles/mainpage.css">
    </head>
    mon nouveau pseudo : <form action="/changepseudo" method="GET">
        <div class="form-group">
            <input type="text" class="form-control" id="npseudo" name="nouveaupseudo" placeholder="nouveau pseudo">
            <input type="hidden" value="''' + str(idjoueur) + '''" id="id" name="id">
        </div>\
        </form>'''


if __name__ == '__main__':
    app.run(debug=True)
