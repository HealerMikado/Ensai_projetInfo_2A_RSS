from vue.bienvenue import Bienvenue
from vue.accueil import Accueil


class VueFactory :

    bienvenue = "bienvenue"
    accueil = "accueil"

    lienNomVue = {
        bienvenue : Bienvenue(),
        accueil : Accueil()
    }

    @staticmethod
    def getVueFromNom(nom):
        return VueFactory.lienNomVue[nom]