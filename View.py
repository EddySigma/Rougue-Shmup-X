import pygame
import os

class View:
    def __init__(self):
        # window icon and text
        SHIP_ICON = pygame.image.load(os.path.join("assets", "icon 32.png"))
        pygame.display.set_icon(SHIP_ICON)
        pygame.display.set_caption("Shmup")

        self.WIDTH = 900
        self.HEIGHT = 800

        self.window = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT)
        )  # notice the double parenthesis

        self.display_queue = []

        self.PLAY_AREA_WIDTH = 600
        self.PLAY_AREA_HEIGHT = 800
        self.BORDER_ASSET = pygame.image.load(
            os.path.join("assets", "border 600x800.png")
        )
        self.BORDER = pygame.transform.scale(
            self.BORDER_ASSET, (self.PLAY_AREA_WIDTH, self.PLAY_AREA_HEIGHT)
        )
        # fill the screen with a color to wipe away anything from last frame
        self.window.fill("black")

        self.display_everything()

        # Border should always be last to make sure that its on top of everything else in playarea
        self.window.blit(self.BORDER, (0, 0))
        # flip() the display to put your work on screen

    def display_everything(self):
        for item in self.display_queue:
            image = item[0]
            x_pos = item[1]
            y_pos = item[2]
            self.window.blit(image, x_pos, y_pos)

    def add_to_display_queue(self, payload):
        self.display_queue.extend(payload)