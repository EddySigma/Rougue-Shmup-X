import pygame
import os
from Controller import Sprite
import pygame


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
        pygame.display.set_icon(pygame.image.load(os.path.join("assets", "icon 32.png")))
        pygame.display.set_caption("Shmup")


    def display_elements(self):
        self.window.fill("black")# fill the screen with a color to wipe away anything from last frame
        self.display_all_sprites()
        self.border_setup_and_display()
        pygame.display.flip()
        
    def display_all_sprites(self):
        for item in self.display_queue:
            color = ()
            if(item.sprite_type == "hero"):
                color = (0, 0, 255) # blue
            elif(item.sprite_type == "enemy"):
                color = (255, 0, 0) # red
            elif(item.sprite_type == "bullet"):
                color = (160, 32, 240) # purple
            
            # this rect is slightly bigger than the sprite itself to see the bullets
            temp_rect = pygame.Rect(item.x_pos -2, item.y_pos-2, item.width+4, item.height+4)
            pygame.draw.rect(self.window, color, temp_rect, width=2)
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