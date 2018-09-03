class Dresseur:

    def __init__(self, name, pokemons=[], id=0):
        self.name = name
        self.pokemons = pokemons
        self.id = id

    def __str__(self):
        return '%s: %s, pokemons %s' % (self.id, self.name, self.pokemons)

    def __repr__(self):
        return '(id=%s, name=%s, pokemons= %s)' % (self.id, self.name, self.pokemons)
