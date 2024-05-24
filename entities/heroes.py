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
        self.current_health = 100
        self.total_health = 100
        self.sprite_type = "hero"
        self.shot_damage = 10
        self.movement_speed = 2  # as far as I know this is tied to frame rate... is there a way to fix that?
        self.time_since_last_shot = pygame.time.get_ticks()
        self.shot_delay = 300


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


    def shoot(self):
        shot = None
        time_now = pygame.time.get_ticks()
        if time_now - self.time_since_last_shot > self.shot_delay:
            self.time_since_last_shot = time_now
            shot = attack.Bullet(
                asset_name="shot 1-10.png",
                x=self.rect.centerx,
                y=self.rect.y,
                vel=4,
                width=3,
                height=30,
            )
    
        return shot

    """
        shot = attack.Bullet(asset_name="shot 1-10.png")
        time_now = pygame.time.get_ticks()  # there is got to be a better way...
        if time_now - self.previous_time > self.fire_rate:
            self.previous_time = time_now
            shot = attack.Bullet(
                asset_name="shot 1-10.png",
                width=3,
                height=30,
                x=self.rect.x,
                y=self.rect.y,
            )

        return shot
    """