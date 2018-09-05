import csv
from lxml import etree

if __name__ == "__main__":
    print('------------------------------------------------------------------- \n')
    print('Création du fichier output/prenoms-cesson-sevigne.xml à partir de files/prenoms-cesson-sevigne.csv')
    with open('output/prenoms-cesson-sevigne.xml', 'wb') as xmlfile:
        with open('files/prenoms-cesson-sevigne.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            # tableau de résultat
            result = etree.Element("Prenoms")
            firstLineProcessed = False
            for row in csvreader:
                # la première ligne va servir pour les clés de nos dictionnaires pythons
                if not(firstLineProcessed):
                    firstLineProcessed = True
                else:
                    # on transforme les lignes suivantes en dictionnaire
                    prenomParent = etree.SubElement(result, "Prenom")

                    commune = etree.SubElement(prenomParent, "Commune")
                    commune.text = row[0]

                    codeInsee = etree.SubElement(prenomParent, "CodeInsee")
                    codeInsee.text = row[1]

                    annee = etree.SubElement(prenomParent, "Annee")
                    annee.text = row[2]

                    sexe = etree.SubElement(prenomParent, "Sexe")
                    sexe.text = row[3]

                    prenom = etree.SubElement(prenomParent, "Prenom")
                    prenom.text = row[4]

                    nombre = etree.SubElement(prenomParent, "Nombre")
                    nombre.text = row[5]

            # on transforme le
            xmlfile.write(etree.tostring(result, pretty_print=True))

            print('Fichier output/prenoms-cesson-sevigne.xml créé \n')
            print(
                '------------------------------------------------------------------- \n')
