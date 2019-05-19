from lib.base_menu import BaseMenu
from lib.welcome import Welcome




class MenuManager(BaseMenu):

    def start(self):

        current_screen = Welcome(self.screens)
        print(current_screen)
        self.screens.append(current_screen)

        self.menu_process(current_screen.user_input(input("Choix :"), current_screen))


    def menu_process(self, screen):

        if screen is None:
            return exit()

        self.screens.append(screen)
        print(screen)
        return self.menu_process(screen.user_input(input("Choix"), screen))



