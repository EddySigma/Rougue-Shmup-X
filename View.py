import pygame
import os

class Thing:
    def __init__(self, image, x, y):
        self.image = image
        self.x_pos = x
        self.y_pos = y

class View:
    def __init__(self):
        self.set_outer_window_info()
        self.WIDTH = 900
        self.HEIGHT = 800

        self.window = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT)  # notice the double parenthesis
        )

        self.display_queue = []
        self.PLAY_AREA_WIDTH = 600
        self.PLAY_AREA_HEIGHT = 800

    def set_outer_window_info(self):
        # window icon and text
        SHIP_ICON = pygame.image.load(os.path.join("assets", "icon 32.png"))
        pygame.display.set_icon(SHIP_ICON)
        pygame.display.set_caption("Shmup")


    def display_elements(self):
        # fill the screen with a color to wipe away anything from last frame
        self.window.fill("black")

        self.BORDER_ASSET = pygame.image.load(
            os.path.join("assets", "border 600x800.png")
        )
        self.BORDER = pygame.transform.scale(
            self.BORDER_ASSET, (self.PLAY_AREA_WIDTH, self.PLAY_AREA_HEIGHT)
        )
        self.display_everything()
        self.window.blit(self.BORDER, (0, 0)) # Border should always be at the end
        pygame.display.flip()
        


    def display_everything(self):
        for item in self.display_queue:
            self.window.blit(item.image, (item.x_pos, item.y_pos))
        self.display_queue.clear()


    def add_to_display_queue(self, payload):
        self.display_queue.extend(payload)
