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
        movement_speed: int = 2,
        health: int = 100
    ):
        self.sprite_type = "hero"
        self.asset_name = asset_name
        self.current_health = health
        self.total_health = health
        self.movement_speed = movement_speed
        self.generate_image(x, y, height, width)

        """
        Idea: change this into weapon
        the weapon knows:
        * its damage
        * fire rate
        * range
        * shot type
        * trajectory
        """
        self.shot_damage = 5
        self.time_since_last_shot = pygame.time.get_ticks()
        self.shot_delay = 300

    def generate_image(self, x, y, height, width):
        self._is_within_bounds(16, 128, height, "height")
        self._is_within_bounds(16, 128, width, "width")

        self.import_image = pygame.image.load(os.path.join("assets", self.asset_name))
        self.sprite = pygame.transform.scale(self.import_image, (width, height))
        self.rect = self.sprite.get_rect(center=(x, y))

    def _is_within_bounds(self, min_val, max_val, test_val, val_type):
        if test_val > max_val:
            raise ValueError(
                "Error: Value %s out of bounds %s is MAX expected, %s given."
                % (val_type, max_val, test_val)
            )
        if test_val < min_val:
            raise ValueError(
                "Error: Value %s out of bounds %s is MIN expected, %s given."
                % (val_type, min_val, test_val)
            )

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
                dam=self.shot_damage,
            )
        return shot

    def take_damage(self, value):
        self._is_within_bounds(1, 9999, value, "player damage")
        self.current_health -= value
        if self.current_health <= 0:
            self.current_health = 0
            self.is_alive = False
