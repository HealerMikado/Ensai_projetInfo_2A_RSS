from connection import connection
from business_object.pokemon import Pokemon


class DaoPokedex:

    def create(self, pokemon):
        cur = connection.cursor()
        try:
            cur.execute(
                "INSERT INTO pokedex (name, element) VALUES (%s, %s) RETURNING id;", (pokemon.name))

            pokemon.id = cur.fetchone()[0]
            # la transaction est enregistrée en base
            connection.commit()
        except:
            # la transaction est annulée
            connection.rollback()
            raise
        finally:
            cur.close()

        return pokemon

    def update(self, pokemon):
        with connection.cursor() as cur:
            cur.execute(
                "update pokedex set name=%s, element=%s where id=%s", (pokemon.name, pokemon.element, pokemon.id))

    def delete(self, pokemon):
        with connection.cursor() as cur:
            cur.execute(
                "delete from pokedex where id=%s", (pokemon.id,))

    def get_all_pokemons(self):
        with connection.cursor() as cur:
            cur.execute(
                "select id, name, element from pokedex")

            # on récupère des tuples et les transforme en objects Pokemon
            result = [Pokemon(id=item[0], name=item[1], element=item[2])
                      for item in cur.fetchall()]
            return result
