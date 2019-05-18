from lib.welcome import Welcome
from lib.connection import Connection


class MenuManager:

    def start(self):
        self.process_item(Welcome())

    def process_item(self, screen):
        if screen is None:
            exit(0)

        print(screen)
        self.process_item(screen.user_input(input()))





