# Liste des interactions et structures de données qu'elles utilisent
On notera ici les différentes structures de données que chaque agent utilisera
## Liste des différentes interactions
<br/>**Site web** (W) -> **Base de données** (DB) 
<br/> **Serveur** (S) <-> **Base de données** (DB)
<br/> **Serveur** (S) <-> **client x : jeu (et non le joueur)** (C)

*Moteur 3D <-> client x (moteur qui serait créé par le professeur)*
# Structures de données
## Structure *DB-W* et *DB-S* : 
- Requêtes SQL sur des tables
-> *il faudra définir la structure à tables*
## Structure *S-C* :
- Echange en TCP avec un serveur **multithread**
- <br/> Ordre des phases : **connexion** -> **init** -> **jeu** 
- le maximum de calculs se fera sur la machine
- **Tuple (x;y) d'entiers** correspondant à la résolution du client (joueur), qu'on mettra à l'échelle 4:3 pour nos affichages
- **2880 x 2160** sera la "résolution de calcul" utilisé par le serveur (résolution 4K mis au format 4:3)

### **A la phase de connexion :**
- ID de joueur sous la forme d'un **nombre à 6
 chiffres (entre 0 et 999999, auto-incrementé)**
- ID de salle (room) sous la forme d'un **string de 4 majuscules (de l'alphabet anglosaxon, c'est-à-dire les 26 lettres sans accent)**
- L'ID de joueur s'abonnera à un ID de room : le serveur connaitra pour chaque room **L'IP**, qui est une **instance d'une classe prévue ppur les ip** et **l'ID** de chaque joueur dans la room, plus une valeur **booléenne** qui dit si le joueur est l'hôte ou non. Quand il reçoit une donnée d'un client, il regarde parmi ses rooms où il retrouve l'ip et l'id de ce client. Il comprendra alors où il doit envoyer la donnée. La table contiendra également une autre variable **booléenne**, **vraie** au départ, qui correspond au fait que le joueur est toujours connecté. Dans le cas d'une déconnection, la variable passe **fausse**, et redevient **vraie** si le joueur arrive à se reconnecter.
- Il y aura toujours n rooms + 1 d'ouvertes (il y aura toujours une room vide pour permettre la création d'une nouvelle partie).
- Chaque room est composé de son **ID** et de sa **table d'abbonnement**
- Une variable **booléenne** pour prévenir le serveur que la partie démarre et qu'on passe à la phase init
- Quand un joueur se connecte, on lui attribue un **bit binaire entre 0 et 7**, correspodant à sa place dans la partie (j1 = 0, j2 = 1 ...).
On aurait donc j1 = 00000001, j2 = 00000010 etc... jusqu'à j8 = 10000000. Ce rang sera relié dans la table d'abonnement à l'IP et l'ID du joueur.
- Deux valeurs d'erreurs **booléennes** existeront : la room est complète ou la room n'a pas été trouvée
###  **A la phase d'initialisation :**
- Création d'un tableau  avec [[**bit du joueur**, **score qui est <u> un entier</u>**]]
- Création d'un autre tableau avec [[**bit du joueur**,**couple d'entiers (x;y) qui définit la position du joueur, et qui sera au point d'origine de notre repère**, **booléen qui dit si le joueur est vivant ou non, True de base**]]
- Recupères une variable **int** nombre de courses choisit avant par l'hôte.
- Une salle est représenté par un tuple (**id_salle** qui est un nombre à deux chiffres, **id_course** qui est un nombre à deux chiffres définissant si une salle est un morceau d'une course plus grande, **un str** qui est le fichier texte contenant les infos de la salle (les murs, les obstacles, point de départ et d'arrivée...))
- Une liste contenant n tuples tel que définit plus tôt, où n est le nombre de courses définit par l'hôte
- Le repère sera définie par un **tuple (x:y)**, qui correspond à l'origine, qui se situera dans un pixel en bas à gauche de l'écran.


### **A la phase de jeu :**
- Position de tous les joueurs donné par un **couple (x;y) d'entiers**. Il faudra mettre un léger time out de manière à ce que ça gêne ni l'oeil du joueur, ni le serveur, pour éviter des envois de positions trop nombreuses (dans le cas où un joueur bougerait sa souris dans tous les sens). Pour le time out, un **timer** performant sera nécessaire. 
- Réinitialisation de la position en cas de collision : si la position d'un joueur n'est pas dans des coordonnées jouables, alors on réinitialise sa position.

### **Fichier de salle :**
- Un fichier JSON
```JSON
{
    "depart" : [(x,y),(x,y)],
    "arrivee": [(x,y),(x,y)],
    "murs": [
        {
            "type" : "murs verticaux",
            "mur1" : [(x,y),(x,y)]
        },
        {
            "type" : "murs horizontaux",
            "mur1" : "etc..."

        }
    ],
    "obstacles" : [
        {
            "type" : "obstacle type 1",
            "mouvement": "etc...",
            "position" : "etc"
        },
        {
            "type" : "etc...."
        }
    ]
}
```
- où départ et arrivée sont des carrés définis par leur diagonale allant du point représenté par le tuple 1 au point du tuple 2
- les murs des segments avec un point de départ et d'arrivée
- les obstacles avec des mouvements (rotations, mouvements...) et leur position

# Répartition
- Victor s'occupera de la **BDD**
- Léandre s'occupera du **serveur**
- Noah, Ethan et Pier s'occuperont du **client x**, puis un ou deux d'entre eux s'occuperont aussi du **web**
