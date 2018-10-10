
print("Avant from classeB import ClasseB ")
import classeB
print("après from classeB import ClasseB ")

print("Salut je suis le scrip classA")
class ClasseA:
    def __init__ (self):
        print ("initialisation de A")
        self.classeB = classeB.ClasseB ()