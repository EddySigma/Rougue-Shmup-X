#!/usr/bin/venv python

import pygame
import os
import dataclasses


@dataclasses.dataclass
class Bullet:
    def __init__(
        self,
        move_type : str,
        asset_name: str,
        x: int = -100,
        y: int = -100,
        width: int = 10,
        height: int = int,
        vel: int = 1,
        dam: int = 1
    ):
        self.move_type = move_type
        self.asset_name = asset_name
        self.velocity = vel
        self.damage = dam
        self.generate_bullet(x, y, height, width)
        self.sprite_type = "bullet"
        self.rect = self.sprite.get_rect()

    def generate_bullet(self, x, y, width, height):
        self.import_sprite = pygame.image.load(
            os.path.join("assets", self.asset_name)
        ).convert_alpha()
        self.sprite = pygame.transform.scale(self.import_sprite, (width, height))
        self.rect = self.sprite.get_rect(center=(x, y))

    def move_straight(self):
        if self.direction == "down":
            self.rect.y += self.velocity

        if self.direction == "up":
            self.rect.y -= self.velocity

    def calculate_next_pos(self):
        direction = 0 # angle (in degrees?)
        vector = pygame.math.Vector2()
        vector.from_polar((self.velocity, direction))
        return (self.rect.x, self.rect.y) + vector

