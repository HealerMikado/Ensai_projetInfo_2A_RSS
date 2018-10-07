
from vue.accueil import Accueil
from vue.abstract_vue import AbstractVue


if __name__ == '__main__':

    # on démarre sur l'écran accueil
    current_vue = Accueil()


    # On se limite à 10 itération
    while AbstractVue.session.iteration <10:
        # on affiche une bordure pour séparer les vue
        with open('assets/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
        # les infos à afficher
        current_vue.display_info()
        # le choix que doit saisir l'utilisateur
        current_vue = current_vue.make_choice()

    with open('assets/cat.txt', 'r', encoding="utf-8") as asset:
        print(asset.read())
