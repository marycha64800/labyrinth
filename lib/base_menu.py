import pygame
from pygame.locals import *
import sys




class BaseMenu:
    """
    Classe mere :
        - Connection
        - Connection
        - New_game
        - Scores
        - etc ....

    Methode :
        user_input : recupere l'entre de lutilisateur pour effectuer un renvoie vers la prochaine instance object
    """
    def __init__(self):

        self.backgound_menu = pygame.image.load("lib/pictures/image_menu.jpg").convert()


    def user_input(self, event_value):

        while True:
            if event_value.type == QUIT:
                pygame.quit()
                sys.exit(0)
            elif event_value.type == KEYDOWN:
                print('plop')
                return None
            event_value = pygame.event.wait()





