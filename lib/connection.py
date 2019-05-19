from lib.base_menu import BaseMenu
from re import match

class Connection(BaseMenu):
    """
    Pas de modifictaion par rapport a Welcome seul les possibilités differe
    previous_screen : l objet par lequel celui ci a etait cree

    """

    def __init__(self, screen):

        super().__init__()
        self.previous_screen = screen
        self.regex = r"^[0]{1}$"
        self.error = ""
        self.next_screen = {

            "0": self.previous_screen

        }

    def user_input(self, value):

        if match(self.regex, value) is None:
            self.error = "Disponible [ 0 ]  exclusivement"
            return self
        else:
            self.error = ""
            return self.next_screen[value]

    def __str__(self):
        return """

        0 << Retour

        1 >> Incription

        2 >> Identification

        {}
        """.format(self.error)