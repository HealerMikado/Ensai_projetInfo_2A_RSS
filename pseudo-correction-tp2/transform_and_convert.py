import csv
import json

if __name__ == "__main__":
    print('------------------------------------------------------------------- \n')
    print('analyse du fichier prenoms-a-rennes.csv')
    with open('output/prenoms-a-rennes_analysed.json', 'w', encoding="utf8") as jsonfile:
        with open('files/prenoms-a-rennes.csv', 'r', encoding="utf8") as csvfile:

            #Lecture du csv
            csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')

            #tableau des résultats
            result = []
            #On passe la ligne de titre
            print (next(csvreader))

            #Le but : lire les prenoms, et sexe pour mettre à jour un dictionnaire avec pour clef, prenom/sexe

            #Le dict avec mes données
            comptagePrenomSexe = dict()


            for row in csvreader:
                #Lecture d'une ligne
                sexe = row[3]
                name = row[4]
                number = row[5]

                if (sexe,name) in comptagePrenomSexe:
                    comptagePrenomSexe[sexe,name] += number
                else:
                    comptagePrenomSexe[sexe,name] = number

            # Maintenant qu'on a les infos que l'on souhaite on fait notre JSON
            for key in comptagePrenomSexe.keys() :
                dictJson = dict()
                dictJson["Prénom"] = key[1]
                dictJson["Sexe"] = key[0]
                dictJson["Total"] = comptagePrenomSexe[key]
                result.append(dictJson)

            # on transforme le tableau en json et on écrit le résultat dans le fichier
            jsonfile.write(json.dumps(result,indent=4))

            print('Fichier output/prenoms-cesson-sevigne.json créé \n')
            print(
                '------------------------------------------------------------------- \n')
