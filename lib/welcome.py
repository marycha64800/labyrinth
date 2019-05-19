from lib.base_menu import BaseMenu
from re import match

from lib.connection import Connection


class Welcome(BaseMenu):
    """
    Class welcome affiche les possibilités qui sont offerte à l'utilisateur se charge de renvoyer l'objet suivant

    methode identique a Basemenu modifier pour les besoin de la classe
    Attribut :
        regex : securise la saisie et renvoie lobjet actuel si une erreur est detecter
        error : affiche la presence d'une erreur
        next_screen : dictionaire contenant tout les objet diponible depuis ce menu

    """

    def __init__(self):

        super().__init__()
        self.regex = r"^[0-1]{1}$"
        self.error = ""
        self.next_screen = {

            "0": None,
            "1": Connection(self),
        }

    def user_input(self, value):

        if match(self.regex, value) is None:
            self.error = "Saisie incorrecte [ 0 ] ou [ 1 ] disponible  !!"
            return self
        else:
            self.error = ""
            return self.next_screen[value]

    def __str__(self):
        return """
        
        0 << Quitter
        
        1 >> Connexion
        
        2 >> Nouvelle partie ( local )
        
        3 >> Reprendre partie en cour ( local )  
        
        
        {}
        """.format(self.error)
