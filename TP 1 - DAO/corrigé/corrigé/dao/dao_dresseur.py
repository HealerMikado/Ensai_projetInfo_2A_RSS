from connection import connection
from business_object.dresseur import Dresseur
from business_object.pokemon import Pokemon


class DaoDresseur:

    def create(self, dresseur):
        cur = connection.cursor()
        try:
            cur.execute(
                "INSERT INTO dresseur (name) VALUES (%s) RETURNING id;", (dresseur.name,))

            dresseur.id = cur.fetchone()[0]

            for pokemon in dresseur.pokemons:
                cur.execute(
                    "INSERT INTO equipier (dresseurId, pokemonId, force) VALUES (%s, %s, %s)", (dresseur.id, pokemon.id, pokemon.force))

            # la transaction est enregistrée en base
            connection.commit()
        except:
            # la transaction est annulée
            connection.rollback()
            raise
        finally:
            cur.close()

        return dresseur

    def get_all_dresseurs(self):
        with connection.cursor() as cur:
            cur.execute(
                "select d.id, d.name, p.name, p.id, p.element, e.force from dresseur d inner join equipier e on e.dresseurId = d.id inner join pokedex p on p.id = e.pokemonId")

            result = []

            for item in cur.fetchall():

                pokemon = Pokemon(
                    id=item[2], name=item[3], element=item[4], force=item[5])
                found = next((d for d in result if d.id == item[0]), None)
                if found:
                    found.pokemons.append(pokemon)
                else:
                    dresseur = Dresseur(name=item[1], pokemons=[
                                        pokemon], id=item[0])

                    result.append(dresseur)
            return result
