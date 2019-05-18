from lib.basemenu import BaseMenu
from lib.connection import Connection


class Welcome(BaseMenu):

    def __str__(self):
         return """
C pour Connecter
I pour s'inscrire
Q pour quitter         

"""

    def user_input(self, value):

        if value.lower() == "c":
            return Connection()

        if value.lower() == 'q':
             return None