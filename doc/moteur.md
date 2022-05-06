Le moteur de jeu utilisé pour ce projet sera pygame.
Il y aura aussi un compteur de morts dans les stats personnelles du joueur dans la partie et sur son compte.
Un timer déclenche la vérification de colision
Faire un micro ordonanceur.
Donnner une forte priorité (au sens systéme du terme) au process
# Structures de données
### classe `Obstacle`.

- Methodes:
  - `colision(x, y)` prend les coordonées d'un joueur et vérifie si un joueur est en colision avec un objet.
  - `affichage()` affiche un objet.

### classe `Joueur`:

- Attributs:
  + `est_mort`->True ou False
  + `coordonnee`->couple de réels(x,y)
  + `nombre_de_morts`->entier
  + `temps_arrive`->temps joué par le joueur
  + `Id_joueur`->entier à 6 chiffres pour différencier les joueurs
  + `ELO_joueur`->entier

- Méthodes:
  +  `__init__(self,Id)`
  + `set_est_mort(self,valeur)`->changer attribut `est_mort` par True or False
  + `set_nombre_de_morts(self,valeur)`-> changer attribut `nombre_de_morts` par un entier

### classe `Course`:

- Attributs:
  + `salles`->liste de plusieurs instances de la classe salle
  
### classe `Salle`:

- Attributs:
  + `liste_obstacles`-> liste d'obstacles
  
  
- Méthodes:
  + `__init__(self,fichier)`->prend commme argument le "path" du fichier qui permet de créer la salle

## NOUVEAU

L'ordonanceur aura un seul thread qui appelera les autres fonctions (gérer les autre thread si il y en a).

On utilisera une file de type (prochain, fonction, temps)

### Menus Du Jeu
Le jeu se lance sur le menu principal contenant 4 boutons: Jouer;Options;Quitter;Mon Compte.
Sans compte, le bouton jouer est grisé et le joueur devra se connecter par le bouton "Mon compte" pour pouvoir jouer.
La connexion se fait par l'ID du joueur; lors de la création du compte, il doit se définir un pseudo(plusieurs joueurs peuvent avoir le même pseudo)
Le menu "Options" permet le réglage du son, de la luminosité et l'activation d'un  mode de correction des couleurs pour les daltoniens.
Le bouton "Quitter" permet au joueur de quitter le jeu
Le bouton "Jouer" ouvre un menu avec un bouton "Créer Salon" et un champ "Entrer Code".
"Créer Salon" crée un salon qui possèdera un code, un tableau qui affichera tous les joueurs présents dans le salon et qui permettra d'afficher le profil des joueurs et les expulser du salon, un bouton "Quitter" qui permettra de quitter le salon et une case "Ready" daans laquelle tous les joueurs devront se tenir pour démarrer la partie.
Le champ "Entrer Code" lui, sera l'emplacement dans lequel le joueur voulant rejoindre un salon, devra entrer le code de celui-ci.
Les menus seront semblables à une partie: La souris sera remplacée par le skin du personnage du compte connecté.

