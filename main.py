
from lib.menu_manager import MenuManager

menu_game = MenuManager()

end = True
while end is not None:
    end = menu_game.start()
