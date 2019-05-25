import pygame
from lib.base_menu import BaseMenu
from lib.welcome import Welcome


class MenuManager:
    """
    Class MenuManger
        module:
            start : est appeler dans le main pour demarer l'affichache de l'ecren accueil
            process_menu : appele la methode userimput de chaque objet et recolte la saisi de l'utilisateur



    """
    def __init__(self, window, winH, windW):

        self.window = window
        self.window_hght = winH
        self.window_widt = windW

    def start(self):

        layer = BaseMenu()
        self.window.blit(layer.backgound_menu, (0, 0))

        pygame.display.flip()

        answer = False
        while answer is not True:

            pygame.time.Clock().tick(30)
            answer = layer.user_input(pygame.event.get())

            if answer is None:
                layer = Welcome()
                self.window.blit(layer.backgound_menu, (0, 0))
                answer = layer.user_input(pygame.event.get())

            pygame.display.flip()



        self.process_menu(layer.user_input(pygame.event.get()))

    def process_menu(self,next_screen):

        pygame.time.Clock().tick(30)
        self.window.blit(next_screen, (0, 0))
        pygame.display.flip()

        return self.process_menu(next_screen.user_input(pygame.event.get()))


