from lib.welcome import Welcome


class MenuManager:
    """
    Class MenuManger
        module:
            start : est appeler dans le main pour demarer l'affichache de l'ecren accueil
            process_menu : appele la methode userimput de chaque objet et recolte la saisi de l'utilisateur

    """
    def start(self):

        screen = Welcome()
        print(screen)
        self.process_menu(screen.user_input(input("Choix: ")))

    def process_menu(self, next_screen):

        if next_screen is None:
            exit()

        print(next_screen)
        return self.process_menu(next_screen.user_input(input("Choix: ")))
