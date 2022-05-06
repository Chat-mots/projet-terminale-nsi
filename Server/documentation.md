# Liste des classes utilisées par le serveur et les clients
## Serveur
- **start_server(** `str:ip_serveur, int:port` **) ->** `None`
<br/> Connectes le serveur, c'est-à-dire le processus initiale sur l'ip et le port donné qui tournera en boucle. Met le
serveur en attente d'une connexion.
- **get_host_ip() ->** `str:IP`
<br> Récupère l'ip de la machine sur laquelle tourne le programme

On fermera le serveur manuellement (avec CTRL+C)
### Fonctions threadées
*Fonctions mises dans les thread du serveur.*
- **hub(** `bytes:message` **) ->** `None`
<br> Fonction mise en thread par le Serveur, dont le but est d'appeler les autres fonctions selon la fonction du message
reçu, fonction décrite par une trame (cf. tramde.md) contenu dans les deux premiers bits. 
- **generate_port () ->** `int:port`
<br> Génère un port pour le thread qui a été crée, et le renvoie.
- **ping(`socket:client`) ->** `bool:crash`
<br> Envoie tout les x temps un message de ping, qui devra être renvoyé par le client, afin de s'assurer que ce dernier
est en vie. QUand la fonction se termine, cela signifie que le client a crash, on renvoie alors cette information.
- **multicast(`bytes:message`) ->** 
<br>Envoie un message en multicast.
## Client
*Le client possèdera une instance des classes encodeurs et décodeurs.*
- **get_host_ip() ->** `str:IP`
<br> Récupères l'IP de la machine qui lance le programme
- **connect(`str:host_ip, int:port`) ->**
<br> Crées un socket client et le connecte au serveur.
- **send(`bytes:message`) ->** Envoie un message au serveur
## Encodeur
*L'encodeur permet d'encoder les messages en bytes afin qu'ils correspondent aux trames (cf trame.md). Chaque client
doit avoir accès aux fonctions de l'encodeur. On utilisera le module struct pour l'encodeur*
- **encode(** `str:trame, X:valeur` **) -> ** `bytes:message, str:format`
<br> Reçoit une trame et une valeur. Appele la fonction correspondante à la trame pour traduire la valeur en bytes, afin
de créer un message à envoyer. Renvoit le message créé ainsi et le format utilisé, nécessaire au décodage
- On aura ensuite une fonction pour chaque trame. Celles-ci prennent `X:valeur` en paramètre et renvoie `str:format`
le format qu'elles utilisent pour struct et `bytes:message` le message qu'elle créent. Le message doit contenir d'abord
la fonction du message (message multicast ou message de ping), la trame, puis le format et la valeur 
qui varient selon la trame.

## Decodeur
*Le décodeur permet de reconstituer une valeur, en récupérant la trame et le format à partir d'un message en bytes.
On utilisera struct*
- **(decode** `bytes:message` **) ->** `str:trame, X:valeur`
<br> Fonction qui décode le dernier message de l'encodeur. Récupères d'abord les trois premiers bytes du message,
correspondant à la trame. Selon la trame récupérée, lances une fonction qui arrivera à récupérer dans le message la
partie correspondante au format et celle à la valeur. A partir de ces deux valeurs, on pourra récupérer la valeur
- On aura donc une fonction pour chaque trame, qui renvoie `X:valeur` la valeur contenue dans le message, en depackant
avec struct sa valeur binaire. Il est donc nécessaire de récupérer dans un premier temps le format, qu'on peut retrouver
étant donné que la taille d'un format reste la même selon la trame.