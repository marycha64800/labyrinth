from lib.base_menu import BaseMenu
from lib.connection import Connection
from re import match

from lib.new_game import NewGame


class Welcome(BaseMenu):

    def __init__(self, screens):

        super().__init__()
        self.regex = r"^[0-4]{1}$"
        self.screens.append(screens)
        self.error = ""

    def __str__(self):
        return """
        
        0 << Quitter
                   
        1 >> Connection
        
        2->> Nouvelle partie ( local ) 
        
        3->> Reprendre une partie ( local )
        
        {}
        """.format(self.error)

    def user_input(self, value, screens):

        if match(self.regex, value) is None:
            self.error = "Saisie incorrecte !!"
            return self
        else:
            self.error = ""

        if value == "1":
            return Connection(screens)
        elif value == "2":
            return NewGame(screens)
        elif value == "0":
            return None

