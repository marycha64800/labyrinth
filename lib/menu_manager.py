import pygame
from pygame.locals import *
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



        layer.user_input(pygame.event.wait())

        layer = Welcome()
        self.window.blit(layer.backgound_menu, (0, 0))
        pygame.display.flip()

        self.process_menu(layer.user_input(pygame.event.wait()))

    def process_menu(self, next_screen):

        self.window.blit(next_screen.backgound_menu, (0, 0))
        pygame.display.flip()
        return self.process_menu(next_screen.user_input(pygame.event.wait()))




