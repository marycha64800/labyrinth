from lib.base_menu import BaseMenu
from lib.connection import Connection
from re import match


class Welcome(BaseMenu):

    def __init__(self):

        super().__init__()
        self.regex = r"^[0-4]{1}$"

    def __str__(self):
        return """
        
        0 << Quitter
                   
        1 >> Connection
        
        2->> Nouvelle partie ( local ) 
        
        3->> Reprendre une partie ( local )
        
        {}
        """.format(self.error)

    def user_input(self, value):

        if match(self.regex, value) is None:
            self.error = "Saisie incorrecte !!"
            return self

        elif value == "1":
            return Connection()
        elif value == "2":
            pass
        elif value == "0":
            return None

