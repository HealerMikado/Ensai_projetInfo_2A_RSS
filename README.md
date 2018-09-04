# Agrégateur de flux RSS et de Tweets

:arrow_forward: [Les diapos de présentation](https://healermikado.github.io/Ensai_projetInfo_2A_RSS/#/)


## Table des matières

  - [Introduction](#introduction)
  - [Fonctionnalités attendues](#fonctionnalités-attendues)
    - [Fonctionnalités de base attendues](#fonctionnalités-de-base-attendues)
    - [Fonctionnalités avancées](#fonctionnalités-avancées)
  - [Diagramme UML](#diagramme-uml)
  - [TP 1 - DAO](#tp--1--dao)
    - [Pourquoi ne pas mettre les fonctions de la DAO dans l'objet métier ?](#pourquoi-ne-pas-mettre-les-fonctions-de-la-dao-dans-lobjet-métier-)
    - [Problèmes rencontrés lors du TP 1](#problèmes-rencontrés-lors-du-tp-1)
      - [Lancement de la classe et pas du main](#lancement-de-la-classe-et-pas-du-main)
      - [Erreur lors du string replacement dans les requêtes](#erreur-lors-du-string-replacement-dans-les-requêtes)
      - [Mon update ne se fait pas en base ??!!!](#mon-update-ne-se-fait-pas-en-base-)
      - [Le CRUD](#le-crud)
      - [Erreur dans les imports avec pylint](#erreur-dans-les-imports-avec-pylint)
    - [Les imports du TP1](#les-imports-du-tp1)
      - [pylint](#pylint)
	  - [autopep8](#autopep8)
	  - [psycopg2-binary](#psycopg2-binary)
  - [TP 2 - Inport/Export de données](#tp-2---inportexport-de-données)
    - [Le CSV](#le-csv)
	- [Le XML](#le-xml)
	- [Le JSON](#le-json)
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
  
## TP 1 - DAO

Une DAO (*Data Access Object*) est une classe technique qui permet de faire le lien entre une classe objet métier (appelée business object dans le TP) et la base de données. C'est cette classe qui va vous permettre de

  - mettre des objets en base ;
  - les lire ;
  - les mettre à jour ;
  - les supprimer.
  
Une fois vos DAO faites, la manipulation de la base de données sera transparente pour vous. Vous ne ferez qu'appeler des méthodes create(), update(), etc, ce qui rendra votre code plus leger et plus simple à comprendre.

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

***Quid de l'attribut self***

L'attribut self représente l'instance "active" de l'objet (celle que vous allez manipuler). Pour la méthode *\_\_init\_\_* c'est celle que vous créez, et pour la méthode *myMethod* c'est l'instance de l'objet sur laquelle vous l'appliquez (dans l'exemple au dessus c'est *myObject*). Vous devez absolument le mettre dans les attributs lors de la définition de la méthode (ce doit même être le premier), mais vous ne devez pas le renseigner à l'appel de la méthode, car implicitement python sait le valoriser.

#### Erreur lors du string replacement dans les requêtes

Certains d'entre vous ont eu des problèmes pour l'écriture de la requête DELETE et on vu cette erreur s'afficher 

TypeError: not all arguments converted during string formatting

Cela provient du fait que dans cette requête un seul placeholder (%s) était replacé, et que tout naturellement vous avez fait cela (j'aurais fait la même chose)

```python
cur.execute("DELTE FROM pokedex WHERE nom = %s;", (pokemon.nom))
```

Sauf que Psycopg2 (la biliothèque qui gère les la partie SQL) est un peu malicieuse, et sa fonction de remplacement de placeholder attend spécifiquement un **tuple**, et pas un **string** (me demandait pas pourquoi, je trouve ça absurde ...). Bref pour que cela fonctionne il faut lui donner un tuple et pour faire ça, rien de plus simple, il suffit de faire 

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

Et ce n'est pas totalement juste. En effet *close* est appelé, mais pas *commit* et *rollback*. Pour faire un commit il faut le faire manuellement, ou activer le mode autocommit. C'est pour cela que certains d'entre vous lançaient un update, récupéraient la ligne updatée avec la méthode get_all_pokemon(), mais quand ils allaient voir en base, la ligne n'était pas updatée. Entre temps, la base avait fait un rollback pour retourner à son état avant update faute de commit. Donc pour tout ce qui est **UPDATE**, **INSERT**, **DELETE**, pensez à faire un commit ! Pour les **SELECT**, pas besoin car c'est une opération de lecture seulement.

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

  - **C**REATE
  - **R**EAD
  - **U**PDATE
  - **D**ELETE

En SQL cela se traduit pour la manipulation des lignes par

  - INSERT
  - SELECT 
  - UPDATE 
  - DELETE
  
Quand vous réaliserez vos DAO pensez-y, et essayez à chaque fois de faire ces 4 fonctions. Sachant que seul SELECT ne modifie pas la base de données, donc c'est la seule qui ne nécessite pas de commit.


#### Erreur dans les imports avec pylint

Cela provient du fait que pylint ne voit pas les répertoires. C'est pas votre faute, c'est une "fausse erreur" en plus car le code fonctionne. Une solution "old_school" est de rajouter des fichier \_\_init\_\_.py dans chaque sous répertoire. On cherche une meilleure solution.


### Les imports du TP1

Au début du TP on vous a fait installer 3 bibliothèques (*pylint*, *autopep8* et *psycopg2-binary*), je vous propose une petite explication sur ces installations

#### pylint

Pylint est un outil qui va vérifier si votre code python ne contient pas d'erreur mais aussi vérifier que vous utilisez les bonnes pratiques de codage python. C'est donc un utilitaire qui ne vous apporte rien d'un point de vu métier, mais qui vous aide à développer du code avec une syntaxe de qualité. Il peut également passer en revu votre code et vous donner des informations dessus. Mais comme vous avez pu le voir, pylint n'est pas infaillible, et peu relever des erreurs qui n'en sont pas.

La doc complète : https://www.pylint.org/

#### autopep8

Encore un utilitaire pour vous aider à écrire du code de qualité. Autopep8 vous permet de formatter votre code pour qu'il se suive les bonnes pratiques **PEP 8**.

La doc complète : https://github.com/hhatto/autopep8

#### psycopg2-binary

Psycopg2-binary est un utilitaire qui vous permet de vous connecter à une base **PostgreSQL**. Sans lui (ou une autre bibliothèque qui fait la même chose) bon courage pour vous connecter à une base. Je vous conseille de l'utiliser pour votre projet :wink:

La doc complète : http://initd.org/psycopg/docs/

## TP 2 - Inport/Export de données

Quelque soit l'application que vous développez, il y a de forte chance que vous ayez à manipuler des données externes à votre application mais également vous risquez de devoir en produire. Vos données en entrée peuvent provenir d'une base de données, mais également de fichiers, de web service ou de toute autre sources de données. Et vos données en sortie peuvent alimenter à peu près les mêmes choses.

Donc vu que quasiment toutes les applications sont amenées à communiquer avec des sources de données externes et des consommateurs de données, il faut se mettre d'accord sur les formats d'échange. Spoiler, il n'y a pas de consensus, car un format ultime qui résout tout les problèmes, ça n'existe pas. Mais, certains formats ont émergé.

### Le CSV

Le **CSV** pour *Coma Separated Values* est un format ultra simple de données. Chaque ligne représente une entrée (par exemple une personne), et chaque valeur est séparée par un caractère de séparation (généralement une virgule, mais ça peut être n'importe quoi)

Par exemple

```CSV
sam,555-555-555,5 rue des lilas
max,1234567890,thailande
bob,666,7eme cercle
```

Si le caractère de séparation peut se trouver dans les champs, on entoure les champs par des " ou des '

```CSV
"sam","555-555-555","5, rue des lilas"
"max,"1234567890","Patong, thailande"
"bob","666","7eme cercle"
```

Pour une meilleure lisibilité, on peut également rajouter en première ligne le nom des colonnes. La plupart des *parser* CSV ont une option pour gérer cette ligne

```CSV
"nom";"numero";"adresse"
"Sam";"555-555-555";"5, rue des lilas"
"Max";"1234567890";"Patong, thailande"
"Bob";"666";"7eme cercle"
```

Sa simplicité en fait un très bon format pour transférer des données qui peuvent s'apparenter à des tableaux. Les tableurs savent les lire, les pluparts des base de données savent les importer et les exporter. Bref pour les tableau :+1:

### Le XML

Le **XML** pour *eXtensible Markup Language* est un fichier qui utilise des balises pour savoir à quoi correspond vos données. On peut faire plein de choses avec, ici je vais juste montrer la version ultra basique.

```XML
<?xml version="1.0" encoding="utf8"?>
<personnes>
    <personne>
        <nom>Sam</nom>
        <numero>555-555-555</numero>
    </personne>
    <personne>
        <nom>Max</nom>
        <numero>1234567890</numero>
    </personne>
    <personne>
        <nom>Bob</nom>
        <numero>666</numero>
    </personne>
</personnes>
```

La balise 

```XML
<?xml version="1.0" encoding="utf8"?>
```
est l'entête du fichier. Elle dit juste que l'on a un fichier au format XML et que l'encodage est de l'utf8

La suite est assez lisible. Dans un fichier CSV, cela donnerait

```CSV
"nom";"numero"
"Sam";"555-555-555"
"Max";"1234567890"
"Bob";"666"
```

En plus de cela vous pouvez imbriquer des balises les unes dans les autres pour les hiérarchiser, voir dubliquer des balises pour signaler que vous avez plusieur valeur pour cet attribut. Exemple

```XML
<?xml version="1.0" encoding="utf8"?>
<personnes>
    <personne>
        <nom>Sam</nom>
            <numero>555-555-555</numero>
            <numero>556-455-055</numero>
            <numero>123-263-896</numero>
    </personne>
    <personne>
        <nom>Max</nom>
        <numero>1234567890</numero>
        <ville>
            <nom>Patong</nom>
            <coord>4.2,6.9</coord>
        </ville>
        <ville>
            <nom>Allyt</nom>
            <coord>8.3,5.2</coord>
        </ville>
    </personne>
    <personne>
        <nom>Bob</nom>
        <numero>666</numero>
    </personne>
</personnes>
```

Ce qui donne en CSV
```CSV
"nom";"numero";"ville"
"Sam";"555-555-555";
"Sam";"556-455-055";
"Sam";"123-263-896";
"Max";"1234567890";"Patong(4.2,6.9)"
"Max";"1234567890";"Allyt(8.3,5.2)"
"Bob";"666";
```

En plus de cela vous pouvez passer des valeurs dans les attributs des balises.

```XML
<personne>
    <nom>Bob</nom>
    <numero type="shortcode">666</numero>
</personne>
```

Et même utiliser un autre fichier XML pour vérifier automatiquement la forme de votre fichier (mais là on rentre dans la partie vraiment compliqué du XML)


Pour résumer, un XML permet
  - l'imbrication faciles de vos données ;
  - la réutilisation du même nom de balise, aussi bien pour le même concept qu'un concept différent
  - de représenter parfaitement des données sous forme d'arbre, et dont on souhaite vérifier la forme a priori.


### Le JSON

Le **JSON** pour *JavaScript Object Notation* est un format qui provient du JavaScript (c'est le langage qui rend les page web interactive). Comme le XML, il permet de représenter la hierachie de vos données, mais de manière plus légère. A la base, c'était juste la représentation textuel d'objet JavaScript, mais avec le temps c'est devenu un format d'échange de données grâce à sa simplicité.

```javascript
[
    {
        'nom': 'Sam',
        'numero': '555-555-555',
        'adresse': '5, rue des lilas'
    },
    {
        'nom': 'Max',
        'numero': '1234567890',
        'adresse': 'Patong, thailande'
    },
    {
        'nom': 'Bob',
        'numero': '666',
        'adresse': '7eme cercle'
    }
]
```

Je n'ai pas grand chose à dire dessus. C'est un fichier de type clef/valeur, avec la possibilité d'imbriquer les objets les uns dans les autres. Il est plus léger que le XML car on ne doit pas fermer les balises, plus agréable à lire, mais ne permet d'être vérifié a priori. Globalement c'est un très bon format d'échange.


## Liens utiles

  - Doc api twitter : https://developer.twitter.com/en/docs.html
  - Des flux RSS : 
     - La une du monde : https://www.lemonde.fr/rss/une.xml
	 - Tric trac : https://www.trictrac.net/actus/flux-fr.rss
	 - Science étonante : https://sciencetonnante.wordpress.com/feed/
  - Doc vers l'api requests (une library pour faire du HTTP) : http://docs.python-requests.org/en/master/