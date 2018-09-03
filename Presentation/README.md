# Agrégateur de flux RSS et de Tweets


:arrow_forward: [Les diapos](https://healermikado.github.io/Ensai_projetInfo_2A_RSS/#/)

## Introduction

L’objectif du projet est de créer un agrégateur de flux RSS et de tweets pour permettre aux utilisateurs de se tenir au informer de l’actualité en temps réel selon des thématiques qu’ils choisissent.

## Fonctionnalités de base attendues :

  - Inscrire et authentifier les utilisateurs
  - Récupérer, mettre en forme et afficher des flux RSS et des tweets
  - Permettre à un utilisateur non inscrit d'accéder à une version allégée de l'application
  - Permettre à un utilisateur inscrit de s'abonner a des flux d'actualités, de sauvegarder des actualités pour y accéder hors ligne, et d'annoter ses actualités sauvegardées
  - Permettre à un utilisateur inscrit de gérer ses infos personnelles, et supprimer son compte à tout moment sans garder la moindre information sur lui
  - Pouvoir paramétrer les thématiques proposées (ajout de thématique, de flus RSS ou de hashtag twitter à une thématique) directement via l'application (en opposition à un paramétrage en dur dans le code)
 
## Fonctionnalités avancées :

  - Permettre à un utilisateur inscrit peut lier son compte twitter à l’application et partager grâce à l’application des articles ou retweeter/liker des tweets
  - Mettre en place un système de notification pour prévenir les utilisateurs quand une thématique est ajoutée ou modifiée
  - Ajouter des fonctionnalités type "réseau social" (faites vous plaisir)
  
## Liens utiles

  - Doc api twitter : https://developer.twitter.com/en/docs.html
  - Des flux RSS : 
     - La une du monde : https://www.lemonde.fr/rss/une.xml
	 - Tric trac : https://www.trictrac.net/actus/flux-fr.rss
	 - Science étonante : https://sciencetonnante.wordpress.com/feed/
  - Doc vers l'api requests (une library pour faire du HTTP) : http://docs.python-requests.org/en/master/