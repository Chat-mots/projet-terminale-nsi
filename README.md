# projet-terminale-nsi
projet de fin d'année de Terminale de Léandre Meunier-Criquet, Victor Jean, Noah Bréhin, Pier Boennec et Ethan Brehin.

## cahier des charges
Crée un jeu de course dans un labyrinthe en multijoueur, en temps réel, généré avec un ordre de salles aléatoires (salles créés à la main, ordre d'apparition aléatoire) au format 4:3. Où le personnage est contrôlé uniquement à la souris. Un tableau de scores mais aussi un classement global entre les différentes parties doit être consultable par les joueurs. Le jeu devra se lancer facilement (à l'aide d'un script bat par exemple).

### règles du jeu
Pour gagner, il faut être le premier à toucher la ligne d'arrivée. Les perdants sont les derniers arrivés.
Les points de victoires sont donnés par ordre d'arrivé (le premier gagne le plus de points, et les points diminue avec le rang de chaque participant).
A la fin de toutes les courses (nombre de courses défini par le joueur au début de la partie), celui avec le plus de points de victoires remporte la partie.

Durant la course, il n'y a pas d'intéractions directes entre les joueurs. Une fois qu'un joueur a atteint la ligne d'arrivée, un timer se déclenche et tous les joueurs passe automatiquement à la course suivant à la fin du décompte (timer global au cas où personne n'arrive la course). Chaque course correspond à une salle. Une collision avec un mur ramène le joueur au départ.

### système de classement
Avec les points de victoires remportés à la fin d'un match et le classement, un joueur gagne ou perd de l'ELO, cela représente le moyen de le classer : plus on a d'ELO, plus on est bien classé. Un jour avec beaucoup d'ELO gagnera peu et perdra beaucoup face à un joueur qui en a peu (les pertes et gains sont proportionnelles à l'ELO des joueurs).

## extension du cahier des charges (idées potentielles)
- génération de salles procéduralement, avec un paramètre de difficulté applicable à la salle.
- ajout d'un "méchant/maitre de jeu", qui voit la course à l'avance et place des obstacles sur la route, si personne ne gagne, il a les points de victoires.
