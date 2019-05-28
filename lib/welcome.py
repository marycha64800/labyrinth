import sys
import os
import pygame
from pygame.locals import *
from lib.base_menu import BaseMenu
from lib.connection import Connection
from lib.new_game import NewGame


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
            elif event_value.type == KEYDOWN:
                if event_value.key == K_KP1 or event_value.key == K_1:
                    return Connection(self)
                if event_value.key == K_KP2 or event_value.key == K_2:
                    return NewGame(self)
                if event_value.key == K_KP3 or event_value.key == K_3:
                    return NewGame(self)
            event_value = pygame.event.wait()




