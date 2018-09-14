import requests
from tabulate import tabulate

if __name__ == '__main__':

    try: 

        proxies = {
            'http': 'proxy-rie.http.insee.fr:8080', 
            'https': 'proxy-rie.http.insee.fr:8080'      }

        # On envoie une requête poru récupérer les statistiques d'emprunt de films
        response = requests.get(
            'https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=equipement-accessibilite-arrets-bus&rows=100&facet=equip_mobilier&facet=equip_banc&facet=equip_eclairage&facet=equip_poubelle&facet=access_pmr&facet=nomcommune&refine.nomcommune=Bruz&refine.access_pmr=OUI', proxies=proxies)

        # Une exception est envoyée si le status de la réponse indique une erreur
        response.raise_for_status()

        # On récupère la réponse au format json, et dans cette réponse le tableau de résultats (records)
        movies = response.json()['records']

        # On filtre sur les film qui contiennent le mot "Star Wars" et on récupére les titres et nombres de prêts
        equipementPMR = [{'Titre': movie['fields']['titre'], 'Nombre de prets en 2017': movie['fields']['nombre_de_prets_2017']}
                          for movie in movies if 'Star Wars' in movie['fields']['titre']]

        # On affiche le résultat sous forme de tableau avec tabulate
        print(tabulate(starWarsMovies, headers="keys", tablefmt='grid'))

    except requests.exceptions.RequestException as error:
        print(error)
