# Specification de l'ordonanceur itégré. 

```
tuple elem_ordo {
    function* Fonction
    float DeltaT
    float T
    char Tag
}
```

`Fonction`
: un pointer vers la fonction a éxécuter, cette fonction ne doit pas prendre d'argument.

`DeltaT`
: tout les combien de temps la fonttion doit s'éxécuter \
s'execute une seule fois si égal a 0.0

`T`
: le moment ou l'element doit être executé exprimé en seconde a partir du lancement
du programe.
