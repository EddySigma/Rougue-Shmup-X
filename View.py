import pygame
import os
from dataclasses import dataclass

@dataclass
class Thing:
    image: pygame.surface.Surface
    x_pos: int
    y_pos: int


class View:
    def __init__(self):
        self.title_bar_information()

        self._WIDTH = 900
        self._HEIGHT = 800
        self.window = pygame.display.set_mode(
            (self._WIDTH, self._HEIGHT)  # notice the double parenthesis
        )

        self.display_queue = []
        self.PLAY_AREA_WIDTH = 600
        self.PLAY_AREA_HEIGHT = 800

    def title_bar_information(self):
        SHIP_ICON = pygame.image.load(os.path.join("assets", "icon 32.png"))
        pygame.display.set_icon(SHIP_ICON)
        pygame.display.set_caption("Shmup")


    def display_elements(self):
        self.window.fill("black")# fill the screen with a color to wipe away anything from last frame
        self.display_player_enemies_butllets()
        self.border_setup_and_display()
        pygame.display.flip()
        
    def display_player_enemies_butllets(self):
        for item in self.display_queue:
            self.window.blit(item.image, (item.x_pos, item.y_pos))
        self.display_queue.clear()

    def border_setup_and_display(self):
        self.BORDER_ASSET = pygame.image.load(
            os.path.join("assets", "border 600x800.png")
        )
        self.BORDER = pygame.transform.scale(
            self.BORDER_ASSET, (self.PLAY_AREA_WIDTH, self.PLAY_AREA_HEIGHT)
        )
        self.window.blit(self.BORDER, (0, 0)) # Border should always be at the end

    def add_to_display_queue(self, payload):
        self.display_queue.extend(payload)