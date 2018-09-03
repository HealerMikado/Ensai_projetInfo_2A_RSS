class Pokemon:

#
# Classe métier Pokémon
#

    #
    # le constructeur de ma classe
    # self fait référence à l'instance actuelle de l'objet. Il faut OBLIGATOIREMENT le déclarer dans un constructeur.
    # MAIS quand vous appelerez le cosntructeur (main_pokemon.py ligne 26) vous n'allez pas le passer dans les arguments
    # car c'est un paramètre 'implicite'
    #
    def __init__(self, name, element, id=0, force=0):
        self.name = name
        self.element = element
        self.id = id
        self.force = force


    #
    # Modifie l'affichage d'un objet quand vous utiliserez la méthode print dessus.
    #

    def __str__(self):
        return '%s: %s, type %s' % (self.id, self.name, self.element)


    #
    # Méthode qui modifie la façon dont l'objet est affiché. Très utile en débug
    # A noter qu'elle prend l'argument self. Cela fait référence à l'instance courante
    # de l'objet (ie celle sur laquelle on l'utilise), mais c'est un paramètre implicite
    # donc pas besoin de l'appeler.
    #

    def __repr__(self):
        return '(id=%s, name=%s, type= %s)' % (self.id, self.name, self.element)
