#!/usr/bin/venv python

import pygame
import os
from Attacks import Bullet


class Hero:
    def __init__(
        self,
        asset_name: str,
        x: int = 100,
        y: int = 100,
        width: int = 64,
        height: int = 64,
    ):
        self.asset_name = asset_name
        self.sprite = self.generate_image(x, y, width, height)
        self.sprite_type = "hero"
        self.fire_rate = 300
        self.movement_speed = 2  # as far as I know this is tied to frame rate... is there a way to fix that?
        self.previous_time = pygame.time.get_ticks()

    def generate_image(self, x, y, width, height):
        self.sprite = pygame.Surface((height, width))
        if self.asset_name != "":
            self.import_sprite = pygame.image.load(
                os.path.join("assets", self.asset_name)
            )
            self.sprite = pygame.transform.scale(self.import_sprite, (width, height))
        else:
            self.rect = self.sprite.get_rect(center=(x, y))

    def change_ship_size(self, new_width, new_height):
        old_x = self.rect.x
        old_y = self.rect.y
        self.sprite = self.generate_image(old_x, old_y, new_width, new_height)

    def move_right(self):
        self.rect.x += self.movement_speed

    def move_left(self):
        self.rect.x -= self.movement_speed

    def move_forward(self):
        self.rect.y -= self.movement_speed

    def move_back(self):
        self.rect.y += self.movement_speed

    """
        self,
        move_type : str,
        asset_name: str,
        x: int = -100,
        y: int = -100,
        width: int = 10,
        height: int = int,
        vel: int = 1,
        dam: int = 1
    """
    
    def shot(self):
        shot = Bullet("up", "shot 1-10.png")
        time_now = pygame.time.get_ticks()  # there is got to be a better way...
        if time_now - self.previous_time > self.fire_rate:
            self.previous_time = time_now
            shot = Bullet(
                move_type="up",
                asset_name="shot 1-10.png",
                width=3,
                height=30,
                x_pos=self.rect.centerx,
                y_pos=self.rect.y,
            )

        return shot