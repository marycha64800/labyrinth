from lib.base_menu import BaseMenu
from lib.welcome import Welcome




class MenuManager(BaseMenu):

    def start(self):

        print(Welcome())
        screen = Welcome()
        next_screen = screen.user_input(input("Choix:"))
        while True:
            print(next_screen)
            next_screen = next_screen.user_input(input("Choix:"))
            self.previous_screens = next_screen



