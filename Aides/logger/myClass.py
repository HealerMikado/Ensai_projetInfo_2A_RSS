import logging

logger = logging.getLogger()
class MyClass():

    def __init__(self,nom):
        logger.debug("Objet myClass instancié avec pour nom {}".format(nom))
        self.nom = nom