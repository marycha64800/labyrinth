from lib.base_menu import BaseMenu
import sys
import pygame
from pygame.locals import *


class NewGame(BaseMenu):
    """
    Pas de modifictaion par rapport a Welcome seul les possibilités differe
    previous_screen : l objet par lequel celui ci a etait cree

    """

    def __init__(self, screen):

        super().__init__()
        self.previous_sreen = screen
        self.backgound_menu = pygame.image.load("lib/pictures/image_nouvelle_partie.jpg").convert()

    def user_input(self, event_value):

        while True:
            if event_value.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event_value.type == KEYDOWN:
                if event_value.key == K_KP0 or event_value.key == K_0 or event_value.key == K_ESCAPE:
                    return self.previous_sreen
                if event_value.key == K_KP1 or event_value.key == K_1:
                    return LevelEasy(self)
                if event_value.key == K_KP2 or event_value.key == K_2:
                    return self.previous_sreen
                if event_value.key == K_KP3 or event_value.key == K_3:
                    return self.previous_sreen
                if event_value.key == K_KP4 or event_value.key == K_4:
                    return self.previous_sreen

            event_value = pygame.event.wait()


class LevelEasy(BaseMenu):

    def __init__(self, screen):

        super().__init__()
        self.previous_sreen = screen
        self.backgound_menu = pygame.image.load("lib/pictures/level_easy.jpg").convert()

    def user_input(self, event_value):

        while True:
            while True:
                if event_value.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event_value.type == KEYDOWN:
                    if event_value.key == K_KP0 or event_value.key == K_0 or event_value.key == K_ESCAPE:
                        return self.previous_sreen
                    if event_value.key == K_KP1 or event_value.key == K_1:
                        return "lib/level/lvl_easy/map_1"
                    if event_value.key == K_KP2 or event_value.key == K_2:
                        return self.previous_sreen
                    if event_value.key == K_KP3 or event_value.key == K_3:
                        return self.previous_sreen
                    if event_value.key == K_KP4 or event_value.key == K_4:
                        return self.previous_sreen

                event_value = pygame.event.wait()


class LevelMedium(BaseMenu):

    def __init__(self, screen):

        super().__init__()
        self.previous_sreen = screen
        self.backgound_menu = pygame.image.load("lib/pictures/level_medium.jpg").convert()

    def user_input(self, event_value):

        while True:
            while True:
                if event_value.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event_value.type == KEYDOWN:
                    if event_value.key == K_KP0 or event_value.key == K_0 or event_value.key == K_ESCAPE:
                        return self.previous_sreen
                    if event_value.key == K_KP1 or event_value.key == K_1:
                        return self.previous_sreen
                    if event_value.key == K_KP2 or event_value.key == K_2:
                        return self.previous_sreen
                    if event_value.key == K_KP3 or event_value.key == K_3:
                        return self.previous_sreen
                    if event_value.key == K_KP4 or event_value.key == K_4:
                        return self.previous_sreen

                event_value = pygame.event.wait()


class LevelHard(BaseMenu):

    def __init__(self, screen):

        super().__init__()
        self.previous_sreen = screen
        self.backgound_menu = pygame.image.load("lib/pictures/level_hard.jpg").convert()

    def user_input(self, event_value):

        while True:
            while True:
                if event_value.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event_value.type == KEYDOWN:
                    if event_value.key == K_KP0 or event_value.key == K_0 or event_value.key == K_ESCAPE:
                        return self.previous_sreen
                    if event_value.key == K_KP1 or event_value.key == K_1:
                        return self.previous_sreen
                    if event_value.key == K_KP2 or event_value.key == K_2:
                        return self.previous_sreen
                    if event_value.key == K_KP3 or event_value.key == K_3:
                        return self.previous_sreen
                    if event_value.key == K_KP4 or event_value.key == K_4:
                        return self.previous_sreen

                event_value = pygame.event.wait()


class LevelVeryHard(BaseMenu):

    def __init__(self, screen):

        super().__init__()
        self.previous_sreen = screen
        self.backgound_menu = pygame.image.load("lib/pictures/level_very_hard.jpg").convert()

    def user_input(self, event_value):

        while True:
            while True:
                if event_value.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event_value.type == KEYDOWN:
                    if event_value.key == K_KP0 or event_value.key == K_0 or event_value.key == K_ESCAPE:
                        return self.previous_sreen
                    if event_value.key == K_KP1 or event_value.key == K_1:
                        return self.previous_sreen
                    if event_value.key == K_KP2 or event_value.key == K_2:
                        return self.previous_sreen
                    if event_value.key == K_KP3 or event_value.key == K_3:
                        return self.previous_sreen
                    if event_value.key == K_KP4 or event_value.key == K_4:
                        return self.previous_sreen

                event_value = pygame.event.wait()
