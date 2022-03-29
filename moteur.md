Un timer déclenche la vérification de colision
Faire un micro ordonanceur.
Donnner une forte priorité (au sens systéme du terme) au process
# Structures de données
On a une classe `Obstacle`.

Methodes:
  - `colision(x, y)` prend les coordonées d'un joueur et vérifie si un joueur est en colision avec un objet.
  - `affichage()` affiche un objet.
  - 

# Micro Ordonanceur
File d'appels de fonctions
## Thread :
 - Le timeur (el ordonanceur):
   + Affichage des obstables
   + Verification de colision
   + Envois de données au server

## NOUVEAU

L'ordonanceur aura un seul thread qui appelera les autres fonctions (gérer les autre thread si il y en a).

On utilisera une file de type (prochain, fonction, temps)
