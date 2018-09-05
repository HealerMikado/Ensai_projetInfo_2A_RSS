import csv
import json

if __name__ == "__main__":
    print('------------------------------------------------------------------- \n')
    print('Création du fichier output/statistiques-de-prets-de-dvd-en-2017-cesson-sevigne.csv à partir de files/statistiques-de-prets-de-dvd-en-2017-cesson-sevigne.json')
    with open('output/statistiques-de-prets-de-dvd-en-2017-cesson-sevigne.csv', 'w') as csvfile:
        with open('files/statistiques-de-prets-de-dvd-en-2017-cesson-sevigne.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            # est-ce que l'entête du fichier à été écrit
            firstLine = False
            for row in data:
                # la première ligne va servir pour les clés de nos dictionnaires pythons
                if not(firstLine):
                    header = list(row.keys())
                    # 'fields' est un élement imbriqué, il faut le remettre à plat pour le csv
                    header.remove('fields')
                    header = header + list(row['fields'].keys())
                    csvfile.write(','.join(header) + '\n')
                    firstLine = True
                # on ajoute une ligne dans le fichier
                fieldsValues = row['fields'].values()
                row.pop('fields')
                # on ne peut écrire que des chaines de caractères, il faut donc convertir chaque valeur
                csvfile.write(
                    ','.join(str(val) for val in list(row.values()) + list(fieldsValues)) + '\n')

            print(
                'Fichier output/statistiques-de-prets-de-dvd-en-2017-cesson-sevigne.csv créé \n')
            print(
                '------------------------------------------------------------------- \n')
