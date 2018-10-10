print("Import de la classe B")
import classeA

class ClasseB:
    def __init__ (self):
        print ("initialisation de B")
        self.classeA =  classeA.ClasseA()