import pygame
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

        for event in event_value:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                return None
        return False




