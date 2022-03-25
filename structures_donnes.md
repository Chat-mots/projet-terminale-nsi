# Liste des interactions et structures de données qu'elles utilisent
On notera ici les différentes structures de données que chaque agent utilisera
## Liste des différentes interactions
<br/>**Site web** (W) -> **Base de données** (DB) 
<br/> **Serveur** (S) <-> **Base de données** (DB)
<br/> **Serveur** (S) <-> **client x : jeu (et non le joueur)** (C)

*Moteur 3D <-> client x (moteur qui serait crée par le professeur*
# Structures de données
## Structure *DB-W* : 
- Requêtes MySQL sur des tables
-> *il faudra définir la structure à tables*
## Structure *S-C* :
- Echange en TCP avec un serveur **multithread**
- <br/> Ordre des phases : **connexion** -> **init** -> **jeu** 
- le maximum de calculs se fera sur la machine

### **A la phase de connexion :**
- ID de joueur sous la forme d'un **nombre à 6
 chiffres (donc aléatoirement entre 100000 et 999999 et jamais identique)**
- ID de salle (room) sous la forme d'un **string de 4 majuscules (de l'alphabet anglosaxon, c'est-à-dire les 26 lettres sans accent)**
- L'ID de joueur s'abonnera à un ID de room : le serveur connaitra pour chaque room **L'IP** et **l'ID** de chaque joueur dans la room, plus une valeur **booléenne** qui dit si le joueur est l'hôte ou non. Quand il reçoit une donnée d'un client, il regarde parmi ses rooms où il retrouve l'ip et l'id de ce client. Il comprendra alors où il doit envoyer la donnée.
- Il y aura toujours n rooms + 1 d'ouvertes (il y aura toujours une room vide pour permettre la création d'une nouvelle partie).
- Chaque room est composé de son **ID** et de sa **table d'abbonnement**
- Une variable **booléenne** pour prévenir le serveur que la partie démarre et qu'on passe à la phase init
- Quand un joueur se connecte, on lui attribue un **bit binaire entre 0 et 7**, correspodant à sa place dans la partie (j1 = 0, j2 = 1 ...).
On aurait donc j1 = 00000001, j2 = 00000010 etc... jusqu'à j8 = 10000000. Ce rang sera relié dans la table d'abonnement à l'IP et l'ID du joueur.
- Deux valeurs d'erreurs **booléennes** existeront : la room est complète ou la room n'a pas été trouvée
###  **A la phase d'initialisation :**
- Création d'un tableau  avec [[**bit du joueur**, **score qui est <u> un entier</u>**]]
- Création d'un autre tableau avec [[**bit du joueur**,**couple d'entiers (x;y) qui définit la position du joueur, et qui sera au point d'origine de notre repère**]]

### **A la phase de jeu :**
- Position de tous les joueurs donné par un **couple (x;y) d'entiers**. Il faudra mettre un léger time out de manière à ce que ça gêne ni l'oeil du joueur, ni le serveur, pour éviter des envois de positions inutiles (dans le cas où un joueur bougerait sa souris dans tous les sens). Pour le time out, un **timer** performant sera nécessaire. 
<br/>**En mode permanent (quand la partie est en cours)**
- Le serveur envoie au client un vecteur avec des coordonnées **de départ et d'arrivée**
- Réinitialisation de la position en cas de collision : si la position d'un joueur n'est pas dans des coordonnées jouables, alors on réinitialise sa position.
