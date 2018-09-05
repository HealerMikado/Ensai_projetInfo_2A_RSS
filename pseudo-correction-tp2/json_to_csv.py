import csv
import json

if __name__ == "__main__":
    print('------------------------------------------------------------------- \n')
    print('Création du fichier output/statistiques-champlibre.csv à partir de files/frequentation_parheure.json')
    with open('output/statistiques-champlibre.csv', 'w', encoding="utf8") as csvfile:
        with open('files/frequentation_parheure.json', 'r', encoding="utf8") as jsonfile:
            data = json.load(jsonfile)
            # est-ce que l'entête du fichier à été écrit
            frequentation = dict()
            for row in data:
                zone = row['fields']["zone"]
                comptage_entrees = row['fields']["comptage_entrees"]
                if (zone) in frequentation:
                    frequentation[zone] += comptage_entrees
                else:
                    frequentation[zone] = comptage_entrees
             

            #le header de notre fichier final
            header = ("zone", "total_entree")
            csvfile.write(','.join(header) + '\n')
            csvfile.write(
                '\n'.join(str(clef)+","+str(frequentation[clef]) for clef in frequentation.keys()))
            print(
                'Fichier output/statistiques-de-prets-de-dvd-en-2017-cesson-sevigne.csv créé \n')
            print(
                '------------------------------------------------------------------- \n')
