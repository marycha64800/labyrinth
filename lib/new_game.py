from lib.base_menu import BaseMenu
from re import match

class NewGame(BaseMenu):


        def __init__(self, screens):

            super().__init__()
            self.regex = r"^[0]{1}$"
            self.screens.append(screens)
            self.error = ""

        def user_input(self, value, sreens):

            if match(self.regex, value) is None:
                self.error = "Saissie incorrecte !!"
                return self
            else:
                self.error = ""

            if value == "0":
                return self.screens[-1]


        def __str__(self):

            return """
            
            0 << Retour 
            
            bla bla 
            
            {}
            
            """.format(self.error)