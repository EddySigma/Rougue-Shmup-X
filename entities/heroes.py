#!/usr/bin/venv python

import pygame
import os
from . import attack

class Hero:
    def __init__(
        self,
        asset_name: str,
        x: int = 400,
        y: int = 600,
        width: int = 64,
        height: int = 64,
    ):
        self.asset_name = asset_name
        self.generate_image(x, y, height, width)
        self.sprite_type = "hero"
        self.fire_rate = 300
        self.movement_speed = 2  # as far as I know this is tied to frame rate... is there a way to fix that?
        self.previous_time = pygame.time.get_ticks()


    def generate_image(self, x, y, height, width):
        self.import_sprite = pygame.image.load(
            os.path.join("assets", self.asset_name)
        )
        self.sprite = pygame.transform.scale(self.import_sprite, (height, width))
        self.rect = self.sprite.get_rect(center=(x, y))


    def move_right(self):
        self.rect.x += self.movement_speed

    def move_left(self):
        self.rect.x -= self.movement_speed

    def move_forward(self):
        self.rect.y -= self.movement_speed

    def move_back(self):
        self.rect.y += self.movement_speed


    def shot(self):
        return attack.Bullet(
            asset_name="shot 1-10.png",
            x=self.rect.centerx,
            y=self.rect.y,
            width=3,
            height=30,
        )