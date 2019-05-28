from lib.base_menu import BaseMenu
import sys
import pygame
from pygame.locals import *

class Connection(BaseMenu):
    """
    Pas de modifictaion par rapport a Welcome seul les possibilités differe
    previous_screen : l objet par lequel celui ci a etait cree

    """

    def __init__(self, screen):

        super().__init__()
        self.previous_sreen = screen
        self.backgound_menu = pygame.image.load("lib/pictures/image_connexion.jpg")

    def user_input(self, event_value):

        while True:
            if event_value.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event_value.type == KEYDOWN:
                    if event_value.key == K_KP0 or event_value.key == K_0 or event_value.key == K_ESCAPE:
                        return self.previous_sreen

            event_value = pygame.event.wait()
