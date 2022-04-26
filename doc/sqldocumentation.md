# base de donnée pour le jeu
## à quoi ça sert ?
la base de donnée sert à stocker les informations des joueurs et leurs actions faites pendant les parties.
## quelles sont les différentes tables ?
il y a 3 tables :
  1. `table base` : elle stocke les informations les plus importantes, indispensable pour classer et connaître le joueur.
  2. `table stastistiques` : elle stocke les informations interressantes que l'on aimerait savoir à la fin d'une partie.
  3. `table badges` : à côté d'un pseudo, il est possible d'afficher un badge, pour représenter un exploit / une action effectué et mémorable. Il s'agit d'un True (1) ou False (0) qui décide si l'on possède ou non le badge.

Les tables ne sont pas fixés, on peut rajouter des informations (colonnes) si l'on souhaite. 
**Attention** : il faudra aussi rajouter dans la bibliothèque python les nouvelles informations
## exemple des tables
*pour la table badge, il s'agit d'une idée, elle n'a pas été implémenté*
**table de base :**

| ID JOUEUR (nombre à 6 chiffres entre 0 et 999999) | pseudo du joueur (string) | ELO (entier) |
| --- | --- | --- |
|  |  |  |
|  |  |  |

**table des statistiques :**

une victoire, c’est lorsqu’un joueur gagne de l’elo à la fin de la partie.

| ID JOUEUR | nombre de morts (entier) | plus haut ELO jamais atteint (entier) | temps de jeu (entier, en secondes) | serie de victoire actuelle (entier) | plus grande série de victoire (entier) | nombre de victoire total (entier) | moyenne de sa place (float) |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |

**table des badges :**

les badges ne sont pas encore implantés, cependant on peut tout de même indiquer leur existence dans une table.

- **crevard** : mourir 100 fois
- **grand vainqueur** : avoir gagné toutes les courses d’une partie
- **mauvais joueur** : donné si le joueur se comporte mal

| ID JOUEUR | crevard (booleen) | grand_vainqueur (booleen) | mauvais joueur (booleen) |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
## infos sur la bibliothèque python
Afin de faciliter la communication entre la bdd et le moteur de jeu. Une bibliothèque python a été implémenté, la documentation de toutes les fonctions se trouve à l'intérieur.
