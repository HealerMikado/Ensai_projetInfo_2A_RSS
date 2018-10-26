# Aide mémoire git
- [Cas nominal sans problème](#cas-nominal-sans-problème)
- [Les conflits](#les-conflits)
  - [Le cas gentil](#le-cas-gentil)
  - [Le cas pas gentil](#le-cas-pas-gentil)
- [.gitignore](#gitignore)
- [Aide mémoire commande](#aide-mémoire-commande)

## Cas nominal sans problème

1. Début séance de travail, récupérer la dernière version du code : 
   
    ```
    git pull
    ```

2. Pendant la séance commiter votre code. Cela permet d'avoir l'assurance qui si à un moment vous "cassez votre code" vous pouvez toujours récupérer une version qui fonctionne.
    ```
    git add
    git commit -m "message de commit explicite"
    ```
3. Fin de la séance, vous poussez votre code sur le dépôt distant (ici gitlab)

    ```
    git push
    ```

## Les conflits

Il se peut que lors de l'étape 3, vous ne pouviez pas pousser le code car vous n'êtes à jouer avec la dernière version du code du dépôt distant. Cela veut dire qu'un de vos collègues de projet à déjà poussé du code, et git vous demande de récupérer se code avant tout envoie.

### Le cas gentil

Si vous vous êtes bien réparti le travail, votre collègue et vous avez modifié des classes différentes (le top de la répartition) ou des zone de code différentes (c'est moins top mais git est très fort alors ça va). Dans ce cas git va pouvoir faire le merge tout seul comme un grand ! Pour faire cela :

```
git pull
```

Git va automatiquement récupérer le code du dépôt distant et le fusionné avec votre code. Ensuite faite les traditionnels

```
git add .
git commit -m "message"
git push
```

### Le cas pas gentil

Il est possible que vous et votre collègue ayez modifié les mêmes lignes de code. Et la git il ne peut rien faire. Donc dans ce cas il vous annonce un conflit, et vous demande de le résoudre avant de commiter et pusher votre code.

Un conflit se matérialise par

```
<<<<<<< HEAD
Votre code
=======
Le code du dépôt
>>>>>>> something
```

A vous de choisir quoi prendre. Un fois cela fait, vous allez faire un

```
git add .
git commit -m "message"
git push
```

Et voilà :)


## .gitignore

Je ne rentre pas dans les détails mais verrifié que votre .gitignore et bien fait comme dans le TP4. Donc il doit contenir

```
.pytest_cache
__pycache__
```

## Aide mémoire commande

- Se placer dans le répertoire de votre projet.
    ```
    cd chemin/vers/votre/dossier/de/travail
    ```
  Attention, sous windows, si vous devez changer de partition (par exemple passer de C: à P:), il faut faire une commande cd pour changer de partition
    ``` 
    cd p:
    cd p:/chemin/vers/votre/dossier/de/travail
    ```
- "Stage" tout les fichiers en vue d'un commit
    ```
    git add . 
    ```
 - "Stage" un fichier vue d'un commit
    ```
    git add monFichier
    ```
 - Commiter tous les fichiers staged avec un message
    ```
    git commit -m "message" 
    ```
 - Commiter tous les fichiers modifiés sans avoir à les stage. Attention, cela ne commit pas les fichiers que vous venez de créer !
    ```
    git commit -m -a "message" 
    ```
  - Pusher tous les commit local
    ```
    git push 
    ```
 - Pusher sur le dépot git pour la première fois 
    ```
    git push -u origin master
    ```
    ```
 - Mettre à jour votre dépôt local avec le code du dépot distant
    ```
    git pull
    ```
  - Voir l'état de votre dépôt local
    ```
    git status
    ```
  - Voir le graph des commits de votre dépôt
    ```
    git log --all --decorate --oneline --graph
    ```
 - Changer d'éditeur par défaut qu'ouvre git pour les message de commit 
    ```
    git config --global core.editor «notepad»