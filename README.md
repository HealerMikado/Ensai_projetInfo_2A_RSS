# Agrégateur de flux RSS et de Tweets

:arrow_forward: [Les diapos de présentation](https://healermikado.github.io/Ensai_projetInfo_2A_RSS/#/)


## Table des matières

  - [Introduction](#introduction)
  - [Fonctionnalités attendues](#fonctionnalités-attendues)
    - [Fonctionnalités de base attendues](#fonctionnalités-de-base-attendues)
    - [Fonctionnalités avancées](#fonctionnalités-avancées)
  - [Diagramme UML](#diagramme-UML)
  - [TP 1 DAO](#tp-1-dao)
  - [Pourquoi ne pas mettre les fonctions de la DAO dans l'objet métier ?](#pourquoi-ne-pas-mettre-les-fonctions-de-la-dao-dans-lobjet-métier-)
  - [Problèmes rencontrés lors du TP 1](#problèmes-rencontrés-lors-du-TP-1)
  - [Lancement de la classe et pas du main](#lancement-de-la-classe-et-pas-du-main)
  - [Erreur lors du string replacement dans les requêtes](#erreur-lors-du-string-replacement-dans-les-requêtes)
  - [Mon update ne se fait pas en base ??!!!](#mon-update-ne-se-fait-pas-en-base-)
  - [Le CRUD](#le-crud)
  - [Erreur dans les imports avec pylint](#erreur-dans-les-imports-avec-pylint)
  - [Liens utiles](#liens-utiles)


## Introduction

L’objectif du projet est de créer un agrégateur de flux RSS et de tweets pour permettre aux utilisateurs de se tenir informé de l’actualité en temps réel selon des thématiques qu’ils choisissent.

## Fonctionnalités attendues

### Fonctionnalités de base attendues

  - Inscrire et authentifier les utilisateurs ;
  - Récupérer, mettre en forme et afficher des flux RSS et des tweets ;
  - Permettre à un utilisateur non inscrit d'accéder à une version allégée de l'application ;
  - Permettre à un utilisateur inscrit de s'abonner à des flux d'actualités, de sauvegarder des actualités pour y accéder hors ligne, et d'annoter ses actualités sauvegardées ;
  - Permettre à un utilisateur inscrit de gérer ses infos personnelles, et supprimer son compte à tout moment sans garder la moindre information sur lui ;
  - Pouvoir paramétrer les thématiques proposées (ajout de thématique, de flus RSS ou de hashtag twitter à une thématique) directement via l'application (en opposition à un paramétrage en dur dans le code).
 
### Fonctionnalités avancées

  - Permettre à un utilisateur inscrit de partager grâce à l’application des articles sur tweeter ou retweeter/liker des tweets ;
  - Mettre en place un système de notification pour prévenir les utilisateurs quand une thématique est ajoutée ou modifiée ;
  - Ajouter des fonctionnalités type "réseau social" (faites vous plaisir).
  
## Diagramme UML

Pour réaliser vos diagrammes, je vous conseille d'utiliser [PlantUML](http://plantuml.com/). Cela vous permet de réaliser vos diagrammes via une syntaxe assez simple,
sans vous soucier du placement des différents objets. Le placement fonctionne souvent correctement (dans certains ils faut allez bidouiller dans les options de placement).
Voici le lien pour réaliser vos diagrammes en ligne : [lien](http://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000)
Vous pouvez sauvegarder vos diagrammes en enregistrant l'image, mais également en copiant le lien en bas. Il vous permettra de charger le code du diagramme pour le modifier. Ne faites pas
comme moi lors de la démo, pour récupérer en diagramme il faut soit

  - Copier le lien dans le barre d'adresse en bas de la page de génération de diagramme en ligne
  - Modifier le lien pour qu'il commence par http://www.plantuml.com/plantuml/uml/ et pas http://www.plantuml.com/plantuml/png/, et mettre le nouveau lien
  dans la barre d'adresse de votre navigateur.
  
## TP 1 DAO

Une DAO (*Data Access Object*) est une classe technique qui permet de faire le lien entre une classe objet métier (appelée business object dans le TP) et la base de données.

### Pourquoi ne pas mettre les fonctions de la DAO dans l'objet métier ?

Car c'est mal !

En informatique au maximum il faut dissocier les taches pour que chaque classe ne fasse qu'une chose (*forte cohérence*). Un objet métier fait partie du coeur de votre système. Ce sont eux et les traitements que vous allez y appliquer qui vont faire la plu-value de votre application. Alors que les DAO ne sont pas réellement importantes. Enfin si, car elles permettent de persister vos données. Mais elles n'apportent aucune valeur métier, et pire vous pouvez parfaitement changer de façon de stocker les données sans modifier le fonctionnement de votre applicatio. Car une DAO répond juste à un besoin technique et pas métier. Par exemple vous pourriez 
très bien vous dire à la fin du projet

"Ummhhh ... Non mais en fait, travailler en PostegreSQL c'est démondé, on va faire du MongoDB"

Pour faire ça il vous suffit juste de supprimer vos classes DAO et d'en faire d'autres, sans toucher à vos objets métiers. Probabilité de "casser" votre code : faible.

Alors que si vous aviez mis les méthodes mise en base directement dans votre objet métier, vous auriez dû le modifier. Et là, la probabilité de casser votre code est très forte.

Donc au maximum, essayez de dissocier le métier de votre application et les solutions techniques. Les solutions techniques bougent très souvent et sont "jetables" alors que le métier lui
est beaucoup plus stable (même s'il est sujet à changement).


### Problèmes rencontrés lors du TP 1

#### Lancement de la classe et pas du main

J'ai vu pas mal de fois cette erreur, je vais essayer de vous expliquer pourquoi lancer une classe ne fonctionne pas.

Déjà il y a une erreur "technique" liée aux imports. Ceux qui on essayé de lancer une DAO directement ont eu une erreur du style

ModuleNotFoundError: No module named 'connection'

Cela vient du fait que, tout bêtement, python ne trouve pas le fichier que vous voulez importer. En effet dans le dossier qui contient la DAO, il n'y a aucun fichier connection.py. Alors qu'en lançant via le main, l'import se fait car fait de manière relative à partir du main.

Ensuite lancer un fichier contenant uniquement une classe ne fonctionnera jamais (en tout cas, ne produira jamais rien)

Une classe python comme celle-ci

```python
class MyClass:

    def __init__(self, attribut):   
		#Something

    def myMethod(self, attribut1):
		#Something

```

est en fait un simple "plan" et ne peut rien faire seul. Exécuter une classe pour faire quelques choses, c'est comme utiliser le plan de montage une voiture pour vous déplacer.
Pour pouvoir utiliser une classe, il faut d'abord **l'instancier**, c'est à dire, utiliser le plan de la classe pour en créer un objet avec.

```python
	myObject = MyClass()
```

Ici je dis à python de me créer un objet que j'appelle *myObject* en utilisant le constructeur de *Myclass* (le constructeur est la méthode *\_\_init\_\_*). Comme *monObjet* à pour classe *myClass* je vais pouvoir appeler la méthode *myMethod* et l'appliquer sur *myObject*

```python
	myObject.myMethod("toto")
```

**Quid de l'attribut self**

L'attribut self représente l'instance "active" de l'objet (celle que vous allez manipuler). Pour la méthode *\_\_init\_\_* c'est celle que vous créer, et pour la méthode *myMethod* c'est l'instance de l'objet sur laquelle vous l'appliquez (dans l'exemple au dessus c'est *myObject*). Vous devez absolument le mettre dans les attributs lors de la définition de la méthode (ce doit même être le premier), mais vous ne devez pas le renseigner à l'appel de la méthode, car implicitement python sais le valoriser.

#### Erreur lors du string replacement dans les requêtes

Certains d'entre vous ont eu des problèmes pour l'écriture de la requête DELETE et on vu cette erreur s'afficher 

TypeError: not all arguments converted during string formatting

Cela provient du fait que dans cette requête un seul placeholder (%s) était replacée, et que tout naturellement vous avez fait cela

```python
cur.execute("DELTE FROM pokedex WHERE nom = %s;", (pokemon.nom))
```

Sauf que Psycopg2 (la biliothèque qui gère les la partie SQL) est un peu malicieuse, et sa fonction de remplacement de placeholder attend spécifiquement un **tuple**, et pas un **string** (me demanait pas pourquoi, je trouve ça absurde ...). Bref pour que cela fonctionne il faut lui donner un tuple et pour faire ça, rien de plus simple, il suffit de faire 

```python
cur.execute("DELTE FROM pokedex WHERE nom = %s;", (pokemon.nom,))
```

Remarquez la virgule seule après pokémon.nom. Voilà c'est aussi simple que ça.

#### Mon update ne se fait pas en base ??!!!

Encore une jolie petite erreur, qui tient à peu de chose. Le sujet du TP est faux. A un moment on vous dit

> Avec psycopg2 lorsque l’on utilise with :
>
>```python
> with connection.cursor() as cur:
>```
>Implicitement, commit() et close() sont exécutés (à la fin du block) et rollback si un exception est levée.

Et ce n'est pas totalement juste. En effet *close* est appelé, mais pas *commit* et *rollback*. Pour faire un commit il faut le faire manuellement, ou activer le mode autocommit. C'est pour cela que certains d'entre vous lancez un update, récupérez la ligne updatée avec la méthode get_all_pokemon, mais quand ils allaient voir en base, la ligne n'était pas updatée. Entre temps, la base avait fait un rollback pour retrouner à son état avant update. Donc pour tout ce qui est UPDATE, INSERT, DELETE, pensez à faire un commit ! Pour les SELECT, pas besoin car c'est une opération de lecture seulement.

Par contre c'est vrai que pour un with avec une connection et pas un curseur

```python
 psycopg2.connect(DSN) as conn:
	#something
```

Quand on quitte le bloc with si aucune exception n'est levée on fait un commit, et un rollback sinon. Je vous conseille donc de conserver cette écriture

```python
 with connection.cursor() as cur:
```
car elle est plus légère que

```python
 try:
	#something
 except:
	#something
 finally:
	#something
```

mais en précisant bien 

```python
 connection.commit()
```


D'ailleurs c'était un bon reflexe d'aller voir la base de données, car c'est son état qui fait foi.

##### Le CRUD

En manipulation de données il existe 4 types de fonctions

  - CREATE
  - READ
  - UPDATE
  - DELETE

En SQL cela se traduit pour des lignes par

  - INSERT
  - SELECT
  - UPDATE
  - DELETE
  
Quand vous réaliserez vos DAO pensez-y, et essayez à chaque fois de faire ces 4 fonctions. Sachant que seul SELECT ne modifie pas la base de données, donc c'est la seule qui ne nécessite pas de commit.


#### Erreur dans les imports avec pylint

Cela provient du fait que pylint ne voit pas les répertoires. C'est pas votre faute, c'est une "fausse erreur" en plus car le code fonctionne. Une solution "old_school" est de rajouter des fichier __init__.py dans chaque sous répertoire. On cherche une meilleurs solution

## Liens utiles

  - Doc api twitter : https://developer.twitter.com/en/docs.html
  - Des flux RSS : 
     - La une du monde : https://www.lemonde.fr/rss/une.xml
	 - Tric trac : https://www.trictrac.net/actus/flux-fr.rss
	 - Science étonante : https://sciencetonnante.wordpress.com/feed/
  - Doc vers l'api requests (une library pour faire du HTTP) : http://docs.python-requests.org/en/master/