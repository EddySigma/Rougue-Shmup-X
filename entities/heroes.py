#!/usr/bin/venv python

import os
import pygame
from . import attack


class Hero:
    """Class representing player character"""
    def __init__(
        self,
        asset_name: str,
        box: pygame.Rect = pygame.Rect(400, 600, 64, 64),  # x,y,w,h
        movement_speed: int = 2,
        health: int = 100,
    ):
        self.sprite_type = "hero"
        self.current_health = health
        self.total_health = health
        self.movement_speed = movement_speed

        # check that the dimensions specified in box are within bounds
        self._is_within_bounds(16, 128, box.height, "height")
        self._is_within_bounds(16, 128, box.width, "width")
        # TODO: need a way for the game to check that the player is within bounds?

        import_image = pygame.image.load(os.path.join("assets", asset_name))
        self.sprite = pygame.transform.scale(import_image, (box.width, box.height))
        self.rect = self.sprite.get_rect(center=(box.x, box.y))

        # damage based attributes
        # TODO: should this become its own object???
        self.shot_damage = 5
        self.time_since_last_shot = pygame.time.get_ticks()
        self.shot_delay = 300

    def _is_within_bounds(self, min_val, max_val, test_val, val_type):
        above_max_message = (
            f"Error: Value {val_type} out of bounds {max_val} is MAX expected, {test_val} given."
        )
        below_min_message = (
            f"Error: Value {val_type} out of bounds {min_val} is MIN expected, {test_val} given."
        )
        if test_val > max_val:
            raise ValueError(above_max_message)
        if test_val < min_val:
            raise ValueError(below_min_message)

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
            print("Player is dead")
