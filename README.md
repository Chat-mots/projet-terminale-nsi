# projet-terminale-nsi
projet de fin d'année de Terminale de Léandre Meunier-Criquet, Victor Jean, Noah Bréhin, Pier Boennec et Ethan Brehin.

## cahier des charges
Crée un jeu de course dans un labyrinthe en multijoueur, en temps réel, généré avec un ordre de salles aléatoires. Où le personnage est contrôlé à la souris. Un tableau de scores doit être consultable par les joueurs.

### règles du jeu
Pour gagner, il faut être le premier à toucher la ligne d'arrivée. Les perdants sont les derniers arrivés.
Les points de victoires sont donnés par ordre d'arrivé (le premier gagne le plus de points, et les points diminue avec le rang de chaque participant).
A la fin de toutes les courses, celui avec le plus de points de victoires remporte la partie.

Une fois qu'un joueur a atteint la ligne d'arrivée, un timer se déclenche et tous les joueurs passe automatiquement à la course suivant à la fin du décompte.
Chaque course correspond à une salle. Une collision avec un mur ramène le joueur au départ.
