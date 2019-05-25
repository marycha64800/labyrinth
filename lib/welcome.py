import sys
import pygame
from lib.base_menu import BaseMenu
from lib.connection import Connection


class Welcome(BaseMenu):
    """
    Class welcome affiche les possibilités qui sont offerte à l'utilisateur se charge de renvoyer l'objet suivant

    methode identique a Basemenu modifier pour les besoin de la classe
    Attribut :
        regex : securise la saisie et renvoie lobjet actuel si une erreur est detecter
        error : affiche la presence d'une erreur
        next_screen : dictionaire contenant tout les objet diponible depuis ce menu

    """

    def __init__(self):

        super().__init__()
        self.backgound_menu = pygame.image.load("lib/pictures/image_welcome.jpg")

    def user_input(self, event_value):

        for event in event_value:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            key = pygame.key.get_pressed()
            print(key)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print('ok')
                    return Connection(self)

            return None




