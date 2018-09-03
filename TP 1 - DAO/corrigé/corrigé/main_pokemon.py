from dao.dao_pokedex import DaoPokedex
from dao.dao_dresseur import DaoDresseur
from business_object.pokemon import Pokemon
from business_object.dresseur import Dresseur
from connection import connection

daoPokedex = DaoPokedex()
daoDresseur = DaoDresseur()

#
# Pourquoi __name__ == "__main__" ?
# Normalement en Python, quand vous exécuter un script, tout se lance.  Et 90% c'est ce que l'on veut.
# Mais dans le cas d'une application avec des scripts qui s'appel les uns les autres on préfère un seul
# point d'entrée.  Il faut savoir qu'en python vous avez toujours accès à la variable __name__. Cette
# variable contient le nom du script courant en cas d'import (cela permet par exemple de savoir ou vous êtes).
# Si vous êtes dans le script principal (ie le premier script que vous avez lancé) elle prend la valeur
# __main__ et pas le nom du script.
# Faire __name__ == "__main__" permet de lancer du code uniquement si le script qui le contient est le script principal.
# Dans votre application vous n'aller avoir qu'une seul script avec __name__ == "__main__", qui sera le point
# d'entrée de l'application
#

if __name__ == "__main__":
    try:
        # création du pokemon
        pikachu = Pokemon(name="Pikachu", element='électricité')
        createdPikachu = daoPokedex.create(pikachu)
        dracaufeu = Pokemon(name="Dracaufeu", element='feu')
        createdDracaufeu = daoPokedex.create(dracaufeu)
        bulbizarre = Pokemon(name="Bulbizarre", element='plante')
        createdBulbizarre = daoPokedex.create(bulbizarre)

        createdBulbizarre.element = 'Eau'
        createdBulbizarre.name = 'Magicarpe'

        daoPokedex.update(createdBulbizarre)

        print('------------------------------------------------\n')
        print("Pokemon créé : ")
        print(createdPikachu)

        print('------------------------------------------------\n')
        print("Pokemon créé : ")
        print(createdDracaufeu)

        print('------------------------------------------------\n')
        print("Pokemon créé : ")
        print(createdBulbizarre)

        daoPokedex.delete(createdBulbizarre)

        found = daoPokedex.get_all_pokemons()

        print('\n------------------------------------------------\n')
        print("Pokemons enregistrés : ")
        print(found)

        createdPikachu.force = 23
        createdDracaufeu.force = 30
        dresseur = Dresseur('Sacha', [createdPikachu, createdDracaufeu])

        createdDresseur = daoDresseur.create(dresseur)

        poissyReine = Pokemon(name="PoissyReine", element='eau')
        createdPoissyreine = daoPokedex.create(poissyReine)

        createdPoissyreine.force = 12
        ondine = Dresseur('Ondine', [createdPoissyreine])
        createdOndine = daoDresseur.create(ondine)

        print('------------------------------------------------\n')
        print("Dresseur créé : ")
        print(createdDresseur)

        print('\n------------------------------------------------\n')
        print("Dresseurs enregistrés : ")
        dresseurs = daoDresseur.get_all_dresseurs()
        print(dresseurs)

    finally:
        # fermeture de la connexion avec la base
        connection.close()
