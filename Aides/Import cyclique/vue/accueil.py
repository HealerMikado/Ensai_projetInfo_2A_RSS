from PyInquirer import Separator, prompt
from vue.abstract_vue import AbstractVue


class Accueil(AbstractVue):

    def display_info(self):
       
        print("Vue Acceuil")
        # Affichage du numero d'iteration de la session. Remarquez, on ne passe jamais la session en paramètre dans une vue
        # car grâce à l'héritage tout le monde la partage
        print("Nous comme à l'iteration {}".format(AbstractVue.session.iteration))

        # On augmente le numero d'iteration de la session. 
        AbstractVue.session.iteration += 1

        # Je seugevarge la vue également, pour un possible retour arrière
        AbstractVue.session.historiqueVue.append(self)

        # J'affiche l'historique. C'est assez moche, car je n'ai pas déclaré de manière d'afficher mes objets vue, alors
        # python affiche seulement la classe + l'adresse du pointeur mémoire
        print("Historique de navigation {}".format(AbstractVue.session.historiqueVue))

    def make_choice(self):
        # En mettant l'import ici, python à l'air d'accepter les imports cycliques
        from vue.bienvenue import Bienvenue
        return Bienvenue()
