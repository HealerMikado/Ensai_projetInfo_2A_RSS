import logging

class MyClass():
    logger = logging.getLogger()

    def __init__(self,nom):
        MyClass.logger.debug("Objet myClass instancié avec pour nom {}".format(nom))
        self.nom = nom