#!/usr/bin/venv python

import pygame
import os


class Bullet:
    def __init__(
        self,
        asset_name: str,
        x: int = 100,
        y: int = 100,
        width: int = 10,
        height: int = 10,
        vel: int = 1,
        dam: int = 1,
    ):
        self.asset_name = asset_name
        self.velocity = vel
        self.damage = dam
        self.generate_image(x, y, width, height)
        self.sprite_type = "bullet"

    def generate_image(self, x, y, width, height):
        self.import_sprite = pygame.image.load(
            os.path.join("assets", self.asset_name)
        )
        self.sprite = pygame.transform.scale(self.import_sprite, (width, height))
        self.rect = self.sprite.get_rect(center=(x, y))
        print(self.rect)

    def move_up(self):
        self.rect.y -= self.velocity
    
    def move_down(self):
        self.rect.y += self.velocity

    def calculate_next_pos(self):
        direction = 0 # angle (in degrees?)
        vector = pygame.math.Vector2()
        vector.from_polar((self.velocity, direction))
        return (self.rect.x, self.rect.y) + vector
