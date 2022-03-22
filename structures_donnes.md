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
- Position de tous les joueurs donné par un **couple (x;y) d'entiers**. Il faudra mettre un léger time out de manière à ce que ça gêne ni l'oeil du joueur, ni le serveur, pour éviter des envois de positions inutiles (dans le cas où un joueur bougerait sa souris dans tous les sens). Pour le time out, un **timer** performant sera nécessaire. 
<br/>**En mode permanent (quand la partie est en cours)**

###  **A la phase d'initialisation :**
- configuration des salles

### **A la phase de connexion :**
- ID de joueur sous la forme d'un **nombre à 
 chiffres (donc aléatoirement entre 100000 et 999999 et jamais identique)**
- ID de salle (room) sous la forme d'un **string de 4 majuscules (de l'alphabet anglosaxon, c'est-à-dire les 26 lettres sans accent)**
- L'ID de joueur s'abonnera à un ID de room : le serveur connaitra pour chaque room **L'IP** et **l'ID** de chaque joueur dans la room. Quand il reçoit une donnée d'un client, il regarde parmi ses rooms où il retrouve l'ip et l'id. Il comprendra alors où il doit envoyer la donnée.
<br/> Ordre des phases : **connexion** -> **init** -> **jeu** 
