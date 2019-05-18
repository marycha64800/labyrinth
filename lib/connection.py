from lib.base_menu import BaseMenu

from re import match


class Connection(BaseMenu):

    def __init__(self):

        super().__init__()
        self.regex = r"^[0-2]{1}$"

    def __str__(self):
        return """
        
        0 << Retour
        
        1 >> Creation compte 
        
        2 >> Itentification
        
        {} 
    
        """.format(self.error)

    def user_input(self, value):

        if match(self.regex, value) is None:
            self.error = "Saissie incorrecte !!"
            return self

        elif value == "0":
            return self.previous_screens


