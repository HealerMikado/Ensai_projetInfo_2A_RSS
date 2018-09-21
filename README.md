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
	- [Injection SQL et prepared statements](#injection-sql-et-prepared-statements)
	  - [Le principe](#le-principe)
	  - [Comment s'en prémunir](#comment-sen-prémunir)
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
  - Permettre à un utilisateur non connecté d'accéder à une version allégée de l'application ;
  - Permettre à un utilisateur connecté de s'abonner à des flux d'actualités, de sauvegarder des actualités pour y accéder hors ligne, et d'annoter ses actualités sauvegardées ;
  - Permettre à un utilisateur connecté de gérer ses infos personnelles, et supprimer son compte à tout moment sans garder la moindre information sur lui ;
  - Pouvoir paramétrer les thématiques proposées (ajout de thématique, de flus RSS ou de hashtag twitter à une thématique) directement via l'application (en opposition à un paramétrage en dur dans le code).
 
### Fonctionnalités avancées

  - Permettre à un utilisateur connecté  de partager grâce à l’application des articles sur tweeter ou retweeter/liker des tweets ;
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
  
## Utilisateur inscrit vs utilisateur connecté

En passant dans les rangs, j'ai vu que beaucoup ont pris le parti d'avoir un utilisateur inscrit/non inscrit, et j'ai un peu était surpris. Après relecture du sujet, je me rend compte que c'est sûrement ma faute car je faisais mention d'utilisateur inscrit. Je vais essayer de vous expliquer pourquoi je pense que la notion d'utilisateur connecté/non connecté à plus de sens qu'inscrit/non inscrit un peu plus en détail que ce que j'ai fait à l'oral (et comme ça il y a une trace écrite).

### Vision machine vs vision humaine

La notion d'inscription, n'a pas trop de sens pour la machine, c'est une vision humaine. Alors oui il y a une ligne en base, mais quand un utilisateur lancera l'application, la machine ne saura pas s'il est inscrit ou pas. Elle ce qu'elle sait c'est s'il est authentifié ou pas (vision machine).

L'autre avantage de la notion de connecté/déconnecté est pour la réalisation d'un diagramme d'activité avec les états de l'utilisateur. Si vous faite le schéma de navigation "complet", de l'ouverture de l'application à sa fermeture, l'utilisateur sera non connecté au début. Et c'est sans appel. Alors qu'avec le notion d'inscrit c'est pas clair. Il pourra être inscrit, s'il a déjà utilisé l'applicaiton, comme non inscrit si c'est ça première fois. Et rien n'empêche à un utilisateur inscrit de créer nouveau un compte. Par contre un utilisateur connecté ne doit pas avoir ce droit.

Après c'est moi le premier a avoir parlé d'utilisateur inscrit/non inscrit, alors vous avez eu raison de reprendre ma terminologie. Et j'aurais sûrement dû parler d'utilisateur connecté/non connecté (j'ai d'ailleurs mis jour les fonctionnalités en haut de la page, et c'est celles de cette page qui sont les "bonnes"). Le côté positif, c'est que quand je suis passé, vous aviez bien tous la notion de connection, avec le CU "s'authentifier", ce qui est finalement une autre manière de représenter cela. Ce sont finalement deux visions qui s'opposent, pas un réel bug dans la conception (de mon point de vu). Donc voilà si vos diagrammes vous vont, gardez les tels quels tant que l'explication qui va avec me permet de bien les comprendre. 

## TP 1 - DAO

Une DAO (*Data Access Object*) est une classe technique qui permet de faire le lien entre une classe objet métier (appelée business object dans le TP) et la base de données. C'est cette classe qui va vous permettre de

  - mettre des objets en base ;
  - les lire ;
  - les mettre à jour ;
  - les supprimer.
  
Une fois vos DAO faites, la manipulation de la base de données sera transparente pour vous. Vous ne ferez qu'appeler des méthodes create(), update(), etc, ce qui rendra votre code plus leger et plus simple à comprendre.

### Pourquoi ne pas mettre les fonctions de la DAO dans l'objet métier ?

**Car c'est mal !**

En informatique au maximum il faut dissocier les taches pour que chaque classe ne fasse qu'une chose (*forte cohérence*). Un objet métier fait partie du coeur de votre système. Ce sont eux et les traitements que vous allez y appliquer qui vont faire la plu-value de votre application. Alors que les DAO ne sont pas réellement importantes. Enfin si, car elles permettent de persister vos données. Mais elles n'apportent aucune valeur métier, et pire vous pouvez parfaitement changer de façon de stocker les données sans modifier le fonctionnement de votre applicatio. Car une DAO répond juste à un besoin technique et pas métier. Par exemple vous pourriez 
très bien vous dire à la fin du projet

"Ummhhh ... Non mais en fait, travailler en PostegreSQL c'est démondé, on va faire du MongoDB"

Pour faire ça il vous suffit juste de supprimer vos classes DAO et d'en faire d'autres, sans toucher à vos objets métiers. Probabilité de "casser" votre code : faible.

Alors que si vous aviez mis les méthodes mise en base directement dans votre objet métier, vous auriez dû le modifier. Et là, la probabilité de casser votre code est très forte.

Donc au maximum, essayez de dissocier le métier de votre application et les solutions techniques. Les solutions techniques bougent très souvent et sont "jetables" alors que le métier lui
est beaucoup plus stable (même s'il est sujet à changement).

### Injection SQL et prepared statements

*Ce paragraphe est à titre de culture informatique, et plus précisement de sécurité informatique.*

Ne faites jamais confiance à vos utilisateurs ! Jamais ! **JAMAIS !** Pourquoi ? Eh bien car entre les utilisateurs qui font n'importe quoi sans le vouloir, et ceux qui essayent d'attaquer votre application, une application accessible depuis le web à la vie dure ! Couvrir tout ce que cela implique prendrait des mois (littérallement), alors ici je vais me concentrer sur les ***injections SQL***

Une ***injection SQL*** est une faille applicative qui permet à un utilisateur de faire réaliser à la base de données des traitements qu'elle ne devrait normalement pas faire. Cela peut-être

  - usurper l'identité de quelqu'un ;
  - modifier des données ;
  - en supprimer ;
  - ralentir votre application.

Et tout ça, c'est pas glop :weary:. Et c'est assez simple à faire si l'application n'est pas protégée contre ça. Mais c'est simple de la protéger, ouf. :relieved:

#### Le principe

Le principe est ultra simple. L'attaquant va rentrer dans un champs de l'application un bout de requête sql, que l'application va envoyer à la base. Et quand je vous dis que c'est simple, c'est vraiment simple. Dans presque tous les site, on trouve des champs login/mdp. Et ce que fait une application, en général, c'est aller chercher en base si le couple login/mdp existe. En simplifiant l'application fait

```sql
SELECT * FROM utilisateur WHERE login = 'login_saisi' AND password = 'mdp_saisi'
```
Si une ligne est renvoyée, c'est bon l'utilisateur est authentifié.

Et pour faire cette requête en python, le plus simple est de concaténer les des chaînes de caractères. Et cela donnerais quelque chose comme

```python
requete = "SELECT * FROM utilisateur WHERE login = '%s' AND password = '%s'" %(login, password)
```

Maintenant plaçons nous dans la peau d'un attaquant, qui a une petite idée du fonctionnement de notre système d'authentification. Il connait un login, mais pas de mot de passe. Au lieu d'en tenter plein, il écrit simplement

```sql
' OR 1=1--
(les -- permettent de mettre en commentaire la suite de la ligne)
```

Python fait gentillement son travail et envoie comme requête à la base :

```sql
SELECT * FROM utilisateur WHERE login = 'toto' AND password = '' OR 1=1--'
```

Si vous vous souvenez de vos cours de SQL, cette requête va systématiquement renvoyer le contenu de toute la table. Bon je souhaitais juste m'authentifier, mais on va dire que c'est un bonus. 

La cause de cette faille est que l'on va concaténer des chaînes de caractères pour réaliser notre requête. Sauf qu'en SQL une chaîne de caractères est entre quote. Et en sachant cela il est facile de tricher, en fermant la chaîne dans le champ que l'on passe pour ensuite écire sa requête.

Bref une injection SQL c'est vraiment tout bête. Cela consiste juste à avoir une idée de quels champ ssont utilisés pour créer une requête SQL et les remplir avec les bons bouts de requête.

#### Comment s'en prémunir

Tout simplement en ne concatenant plus de chaîne de caractères pour faire une requête et utiliser des ***Prepared Statements***. C'est valable en python, mais également pour tous les autres langages de programmation.

Sans rentrer dans les détails, une prepared statements vous permet de ne pas faire une simple concaténation de chaine de caractère. Elle va prendre en charge également la conversion des champs que vous passez à la requête et donc échapper tous les caractères spéciaux.

Je m'explique dans cette requête :

```python
requete = "SELECT * FROM utilisateur WHERE login = '%s' AND password = '%s'" %(login, password)
```

vous spécifiez vous même que login et password attendent des textes (regardez les ' entourants les %s). Avec une prepared statement, c'est elle qui s'en occupe. Et vous allez simplement écrire

```python
cur.execute("SELECT * FROM utilisateur WHERE login = %s AND password = %s" ,(login, password))
```

Et en changeant juste cela, vous êtes assurez (enfin ça c'est si aucune faille n'est découverte dans les prepared statements) qu'aucune injection SQL ne pourrait être réalisé via cette requête. C'est vraiment tout simple, alors pourquoi s'en priver ? :smile:

Alors ne vous inquiétez pas, c'est ce que vous avez déjà utilisé dans le TP1, mais je voulais vous expliquer ce que vous faisiez et pourquoi vous le faisiez.

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

Psycopg2-binary est un utilitaire qui vous permet de vous connecter à une base **PostgreSQL**. Sans lui (ou une autre bibliothèque qui fait la même chose) bon courage pour vous connecter à une base. Et en plus elle vous permet de faire des prepared statements, si c'est pas beau ! Je vous conseille de l'utiliser pour votre projet :wink:

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


### Problèmes rencontrés lors du TP2

#### Les fichiers n'existent pas

Au lancement des exemples, vous aviez une erreur qui vous disez que le fichier XX n'existait pas. En même temps vous vouliez le créer alors c'est normal. La raison était que vous lanciez vos scripts depuis C:\Windows il me semble. Alors quand ce genre de chose vous arrive, pensez à regarder dans la console depuis où le script se lance. Normalement, quand vous faite ouvrir un dossier avec Visual studio il doit vous amener dans le bon repertoire. Mais il semblerait qu'à l'Ensai ça fonctionne pas toujours en fonction de la manière dont vous allez chercher votre dossier (passage par mes documents ou P:)

#### Encodage

Ahhhhh la gestion des caractères spéciaux et l'encodage. Clairement l'un des problèmes les plus courants qui existe dans l'échange de données. Et vous allez sûrement y être confronté dans votre vie future, alors autant commencer tôt.

Vous devez tous savoir qu'un ordinateur ça traite des 0 et des 1, et pas des chaînes de caractères, des nombre, des dates etc. *Spoiler*, les date c'est chiant également. Pour représenter un caractère, il faut donc se mettre d'accord sur la manière dont on le représente avec des 0 et des 1. Le problème (comme souvent) c'est qu'aucun consensus n'a était trouvé pour créer un encodage unique, donc il y en a beaucoup. Dans certains cas ça à du sens d'avoir des encodages différents, surtout pour des langues comme le japonais, le chinois, le coréen etc qui sont à base d'idéogrammes. Mais dans d'autres cas, c'est sujet à problème. Et dans une même entreprise il n'y a pas consensus. Par moment on va vous fournir des fichiers en UTF-8 et après des fichiers en Windows-1252 ou autre encodage. Dans ce cas, c'est souvent car les gens ne connaissent pas la notion d'encodage, ou n'y pense pas. Mais voilà faites-y attention. Cela fait souvent perdre beaucoup de temps pour rien.

Le pire, c'est qu'en général sur les caractères "normaux", c'est bon. Alors si dans un fichier exemple il n'y a pas d'accent, on pense que c'est ok et quand on passe sur le fichier final, ça fonctionne pas du tout. Je vais vous donner un exemple. Par exemple si je pendre un **é**, dans un codage ascii il devient **11101001**, mais dans un codage UTF8 c'est **11000011 10101001**. C'est pas réellement la même chose.

Résultat, quand vous allez lire en fichier en utilisant le mauvaise encodage, vous allez avoir des résultats surprenants qui vont apparaitre. Car l'ordinateur il est un peu "idiot" donc il va le lire votre fichier et le traduire comme il peut. S'il a un caractère pour ce code il le met, et sinon il va vous mettre un caractère du style "?" car il ne sait pas. Et en plus en fonction de l'encodage, votre ordinateur doit lire les octets une par un, deux par deux, ou en prendre un nombre variable en foncton d'un préfixe. Bref c'est compliqué et ça génère plein d'erreurs.

Si vous voulez vous amusez voir ce que ça fait, sur notepad++ vous pouvez changer l'encodage d'un fichier manuellement. Cela donne des résultats surprenant. Ou sinon voici un site pour vous voir ce qu'un changement d'encodage fait sur vos fichiers : http://string-functions.com/encodedecode.aspx

## TP 3 : Utiliser un api web et réaliser une

Bon alors même si dans le TP il y a la réalisation d'une webservice, vu que ça ne va pas servir dans le cadre du projet, je ne vais pas trop détailler comment ça fonctionne. Ici je vais me concentrer uniquement sur contacter une web API (ou webservice)

### Une simple URL

Appeler une API web c'est simple, très simple même. Il vous suffit une simple [URL](https://fr.wikipedia.org/wiki/Uniform_Resource_Locator). Et c'est tout. Sauf que derrière cette URL, au lieu d'avoir une page web (style https://ent.ensai.fr) vous allez avoir une application qui va faire des traitements (par exemple aller chercher des infos dans une base de données et les mettre au format JSON) et vous envoyer un résultat, qui va contenir un code retour pour vous dire si ça c'est bien passé (code 200) ou mal passé (il y a beaucoup de code pour dire que ça c'est mal passé). Et comme ce sont des URL vous allez pouvoir y accéder avec votre navigateur !! Enfin, toute celle qui sont en méthode GET, mais ça on en parlera plus tard.

Maintenant, parlons de l'URL que vous allez envoyer. Par exemple si je veux récupérer les infos sur les arrêts physique de la STAR je peux appeler cette URL : https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=equipement-accessibilite-arrets-bus, ou celle là : https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=equipement-accessibilite-arrets-bus&facet=equip_mobilier&facet=equip_banc&facet=equip_eclairage&facet=equip_poubelle&facet=access_pmr&facet=nomcommune. La différence entre les deux (à part leur taille) est que l'une beaucoup des paramètre et que l'autre n'en moins. Dans une requête HTTP vous pouvez passer des paramètres directement dans l'URL. Et cela simplement en mettant un ? avant vos paramètres. Et ceci n'est pas spécifique au fonctionnement des API web, c'est dans la norme HTTP.

Décortiquons nos requêtes. Avant le ? les deux URL sont identiques, et font référence à  https://data.rennesmetropole.fr/api/records/1.0/search. En allant fouiller dans la doc de l'API on voit que

```
/api/records/1.0/search/
Description

Ce service permet d'effectuer une recherche sur l'ensemble des données d'un Dataset, à travers l'utilisation de fonctionnalités intuitives de recherche telles que la recherche textuelle et la recherche géographique; il permet également la navigation par Facettes pour offrir à l'utilisateur un moyen d'obtenir facilement et précisément les données souhaitées.

Dans le cas d'une utilisation sans paramètre de recherche, toutes les données du Dataset sont restituées.
```

Donc déjà nos deux requêtes sont faites pour chercher des données.

Ensuite premier paramètre : dataset=equipement-accessibilite-arrets-bus. En reprenant le doc le Dataset c'est les données que l'on veut interrogé. Et c'est un attribut obligatoire. Donc pour le moment nos deux requêtes vont bien tapé la même base. Et c'est maintenant que la différence commence car l'une à comme autres attributs : *&facet=equip_mobilier&facet=equip_banc&facet=equip_eclairage&facet=equip_poubelle&facet=access_pmr&facet=nomcommune*. Déjà les & servent à faire passer plusieurs paramètres dans l'URL. Ensuite on voit que l'on a plusieurs fois facet avec des valeurs différentes. 

Dans le doc on lit

```
facet 	

Active une Facette pour qu'elle soit incluse dans les résultats (les Facettes disponibles sont indiquées au niveau de la défition du Dataset); ce paramètre peut-être utilisé plusieurs fois pour activer plusieurs Facettes. Par défaut aucune Facette n'est activée.
```

Donc dans la requête longue on passe plusieurs facets pour récupérer plus de données. Alors oui il suffisait de cliquer sur les liens pour le voir, mais je voulais vous expliquer un peu le fonctionnement. D'ailleurs dans le TP, on vous demandait de récupérer que les arrets PMR. Et c'était faisable directement via l'API, en rajouant à l'URL &refine.access_pmr=OUI.

Petit exemple avec l'API twitter avec cette URL : https://api.twitter.com/1.1/search/tweets.json?q=ensai je vais récupérer les tweets qui mentionnent l'Ensai. Mais ça ne va pas fonctionner car *Bad Authentication data*. Et oui pour accéder à l'API twitter il faut s'authentifier. Et pour faire ça vous allez devoir passez des paramètres à vos requêtes, mais pas dans l'URL, dans le l'en-tête de la requête.

### Une requête HTTP

Bon je vous ai déjà dit que l'on pouvait passser des paramêtres dans l'URL avec ?monparam=mavaleur. Mais on peut aussi en passer via l'en-tête et le corps de la requête. Alors je ne vais pas vous expliquer plus en détail que ça comment fonctionne une requête. C'est pas forcément ultra passionnant et utile pour vous. Retenez juste cela, une requête HTTP est constituée de 

```
Ligne de commande (Commande, URL, Version de protocole)
En-tête de requête
<nouvelle ligne>
Corps de requête
```

Pourquoi c'est pas ultra important ? Car vous n'allez jamais faire une requête vous même. Vous allez toujours passer par une librairie qui la fera pour vous. Typiquement, **Requets** qui permet de tout faire, ou **feedparser** qui permet juste de récupérer un flux RSS.

Mais comment on fait pour se connecter à Twitter ? Déjà on va lire la [doc](https://developer.twitter.com/en/docs/basics/authentication/overview/oauth). Youpi une nouvelle notion, Oauth !! Oauth est un protocole de délagation d'authentification. Rapidement, avec Oauth, vous allez pouvoir via une application consommatrice de données (par exemple l'application que vous êtes en train de développer) vous connecter à une application fournisseuse de données (par exemple twitter) sans jamais passé vos identifiant/mdp de l'application fournisseuse à l'application consommatrice. Dans notre exemple, vous allez pouvoir accéder à votre compte twitter via votre application sans jamais rentrer dans votre application votre login/mdp

GROSSE PRECISION !! Ici je ne parle pas du cas d'utilisation avancé qui permet à un utilisateur de partager des choses sur twitter. Je suis juste en train de vous parler du processus qui vous permet de récupérer des infos sur twitter. Car pour faire cela il faut lier un compte twitter à votre application.

PETITE PRECISION. Pour faire le cas d'utilisation qui permet à un utilisateur de partager quelque chose sur son twitter, vous allez utiliser également Oauth, mais ça sera plus dur.

Voici un exemple de code qui vous montre comment récupérer la timeline twitter en python  https://developer.twitter.com/en/docs/basics/authentication/guides/single-user



## Liens utiles

  - Doc api twitter : https://developer.twitter.com/en/docs.html
  - Des flux RSS : 
     - La une du monde : https://www.lemonde.fr/rss/une.xml
	 - Tric trac : https://www.trictrac.net/actus/flux-fr.rss
	 - Science étonante : https://sciencetonnante.wordpress.com/feed/
  - Doc vers l'api requests (une library pour faire du HTTP) : http://docs.python-requests.org/en/master/