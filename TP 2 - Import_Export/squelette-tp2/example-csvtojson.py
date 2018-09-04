import csv
import json

if __name__ == "__main__":
    print('------------------------------------------------------------------- \n')
    print('Création du fichier output/prenoms-cesson-sevigne.json à partir de files/prenoms-cesson-sevigne.csv')
    with open('output/prenoms-cesson-sevigne.json', 'w') as jsonfile:
        with open('files/prenoms-cesson-sevigne.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            # tableau de résultat
            result = []
            # les clés qui vont nous servir à créer nos dictionnaires
            keys = None
            for row in csvreader:
                # la première ligne va servir pour les clés de nos dictionnaires pythons
                if not(keys):
                    keys = row
                else:
                    # on transforme les lignes suivantes en dictionnaire
                    dictionnary = dict(zip(keys, row))
                    # on l’ajoute au tableau
                    result.append(dictionnary)

            # on transforme le tableau en json et on écrit le résultat dans le fichier
            jsonfile.write(json.dumps(result))

            print('Fichier output/prenoms-cesson-sevigne.json créé \n')
            print(
                '------------------------------------------------------------------- \n')
