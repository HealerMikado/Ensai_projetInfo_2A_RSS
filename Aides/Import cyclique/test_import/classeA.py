
print("Avant from classeB import ClasseB ")
from classeB import ClasseB 
print("après from classeB import ClasseB ")

print("Salut je suis le scrip classA")
class classeA:
    def __init__ (self):
        print ("initialisation de A")
        self.classeB = ClasseB ()