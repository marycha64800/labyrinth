import sys
import pygame
from pygame.locals import *
from lib.base_menu import BaseMenu
from lib.connection import Connection


class Welcome(BaseMenu):
    """
    Class welcome affiche les possibilités qui sont offerte à l'utilisateur se charge de renvoyer l'objet suivant

    methode identique a Basemenu modifier pour les besoin de la classe


    """

    def __init__(self):

        super().__init__()
        self.backgound_menu = pygame.image.load("lib/pictures/image_welcome.jpg")

    def user_input(self, event_value):
        while True:
            if event_value.type == QUIT:
                pygame.quit()
                sys.exit(0)
            elif event_value.type == KEYDOWN and event_value.key == 257:
                print('plop')
                return Connection(self)
            elif event_value.type == KEYDOWN:
                print(event_value.key)
            event_value = pygame.event.wait()




