from lib.menu_manager import MenuManager
import pygame

WINDOW_HEIGHT = 900
WINDOW_WIDTH = 1500
FPS = 60

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

navigation = MenuManager(window, WINDOW_HEIGHT, WINDOW_WIDTH)

game_over = False
while game_over is not True:
    level = navigation.start()


    game_over = True
