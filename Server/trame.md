# Trame du serveur
A chaque lettre correspond une trame, qui signifie à quoi correspond la donnée reçue.
## Liste des trames
- **IDJ** : Id de joueur
- **IDR** : Id de room
- **IPJ** : l'IP de joueur
- **PTD** : partie démarrée ou non (bool)
- **EPC** : Erreur : la partie est complète (bool)
- **EPI** : Erreur : partie inexistante (bool)
- **SCR** : Score
- **POS** : Tableau de position de tous les joueurs
- **EDM** : Etat des morts (le nombre binaire qui donne les morts)
- **IDS** : Id de salle
- **IDC** : Id de course
- **NBC** : Nombre de courses
- **DEC** : joueur deconnecté (bool)
- **TIM** : Timer

### Trames du hub
- **MC** : Message à envoyer en multi-cast
- **MP** : Message ping envoyé tous les x temps pour savoir si le client est toujours connecté