# Liste des classes utilisées par le serveur et les clients
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
<br> Reçoit une trame et n'importe quel type de valeur X. Crée un string représentatif de X selon la trame donnée. 
Traduit ce string en bytes et l'envoie au serveur.
- **decodage(**`bytes:message`**) ->** `str:trame, X`
<br> Reçoit un message en bytes. Récupères d'abord la trame dans les bytes et le traduit en str, puis traduit en str 
le reste du message. Interprète selon la trame le message derrière, et crées une valeur X correspondant à la 
représentation. Renvoit la trame et la valeur X créée de cette manière.
- **send_to_all(** `str:message` **) ->** `None`
<br/> Donne un message, le traduit en bytes en précisant dans la trame qu'il est à destination de tous et l'envoie au 
serveur afin que ce dernier l'envoie à tous les clients.
- **receive() ->** `str:trame, str:donnees`
<br/> Reçoit des données, récupères la trame et les données sous une forme abstraite et renvoie ces deux informations

## Encodeur
L'encodeur permet d'encoder les messages en bytes afin qu'ils correspondent aux trames (cf trame.md). Chaque client
doit avoir accès aux fonctions de l'encodeur. On utilisera le module struct pour l'encodeur
### Fonctions :
- **encode(** `str:trame, X:valeur` **) -> ** `bytes:message, str:format`
<br> Reçoit une trame et une valeur. Appele la fonction correspondante à la trame pour traduire la valeur en bytes, afin
de créer un message à envoyer. Renvoit le message créé ainsi et le format utilisé, nécessaire au décodage
- On aura ensuite une fonction pour chaque trame. Celles-ci prennent `X:valeur` en paramètre et renvoie `str:format`
le format qu'elles utilisent pour struct et `bytes:message` le message qu'elle créent. Le message doit contenir d'abord
la trame, puis le format et la valeur qui varient selon la trame.

## Decodeur
Le décodeur permet de reconstituer une valeur, en récupérant la trame et le format à partir d'un message en bytes.
On utilisera struct
- **(decode** `bytes:message` **) ->** `str:trame, X:valeur`
<br> Fonction qui décode le dernier message de l'encodeur. Récupères d'abord les trois premiers bytes du message,
correspondant à la trame. Selon la trame récupérée, lances une fonction qui arrivera à récupérer dans le message la
partie correspondante au format et celle à la valeur. A partir de ces deux valeurs, on pourra récupérer la valeur
- On aura donc une fonction pour chaque trame, qui renvoie `X:valeur` la valeur contenue dans le message, en depackant
avec struct sa valeur binaire. Il est donc nécessaire de récupérer dans un premier temps le format, qu'on peut retrouver
étant donné que la taille d'un format reste la même selon la trame.