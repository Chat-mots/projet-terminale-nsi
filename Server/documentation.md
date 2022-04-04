# Liste des classes utilisées par le serveur
## Serveur
- **start_server(** `str:ip_serveur, int:port` **) ->** `None`
<br/> Connectes le serveur sur l'ip et le port donné qui tournera en boucle
- **get_server_ip() ->** `str:server_ip`
<br> Renvoie l'ip de la machine qu'on utilise, qui permettra de connaître l'ip de la machine qui host
- **send_to_all(** `bytes:message` **) ->** `None`
<br/> Donne un message déjà converti en bytes, et l'envoie à tous les clients connectés au serveur
- **receive() ->** `str:trame, str:donnees`
<br/> Reçoit des données, récupères la trame et les données sous une forme abstraite et renvoie ces deux informations

On fermera le serveur manuellement (avec CTRL+C)
## Client
- **start_client(** `str:ip_server, int:port` **) ->** `None`
<br> Connectes un lient sur le serveur, il faut donc que chaque client mette les mêmes paramètres que le serveur
- **encodage(** `str:trame, X` **) ->** `bytes:message`
<br> Reçoit une trame et n'importe quel type de valeur X. Crée un string représentatif de X selon la trame donnée. Traduit ce string en bytes et l'envoie au serveur.
- **decodage(**`bytes:message`**) ->** `str:trame, X`
<br> Reçoit un message en bytes. Récupères d'abord la trame dans les bytes et le traduit en str, puis traduit en str le reste du message. Interprète selon la trame le message derrière, et crées une valeur X correspondant à la représentation. Renvoit la trame et la valeur X créée de cette manière.
- **send_to_all(** `str:message` **) ->** `None`
<br/> Donne un message, le traduit en bytes en précisant dans la trame qu'il est à destination de tous et l'envoie au serveur afin que ce dernier l'envoie à tous les clients.
- **receive() ->** `str:trame, str:donnees`
<br/> Reçoit des données, récupères la trame et les données sous une forme abstraite et renvoie ces deux informations
