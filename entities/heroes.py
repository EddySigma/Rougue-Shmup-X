#!/usr/bin/venv python

import os
import pygame
from . import attack
from . import baseActor


def is_within_bounds(min_val, max_val, test_val, val_type):
    above_max_message = f"Error: Value {val_type} out of bounds {max_val} is MAX expected, {test_val} given."
    below_min_message = f"Error: Value {val_type} out of bounds {min_val} is MIN expected, {test_val} given."
    if test_val > max_val:
        raise ValueError(above_max_message)
    if test_val < min_val:
        raise ValueError(below_min_message)


class Hero2(baseActor.BaseActor):
    def __init__(
        self,
        img: pygame.surface = pygame.image.load(os.path.join("assets", "test img.png")),
        rect: pygame.Rect = pygame.Rect(0, 0, 64, 64),
        weapon: attack.Weapon = attack.Weapon(bullet_asset_name="h-shot20.png"),
    ):
        super().__init__(img, rect, weapon)
        self.sprite_type = "hero"

    def move_right(self):
        self.rect.x += self.movement_speed

    def move_left(self):
        self.rect.x -= self.movement_speed

    def move_forward(self):
        self.rect.y -= self.movement_speed

    def move_back(self):
        self.rect.y += self.movement_speed

    def shoot(self):
        return self.weapon.fire(self.rect.centerx, self.rect.centery, 180)


class Hero:
    """Class representing player character"""

    def __init__(
        self,
        asset_name: str,
        box: pygame.Rect = pygame.Rect(400, 600, 64, 64),  # x,y,w,h
        movement_speed: int = 2,
        health: int = 10,
    ):
        self.sprite_type = "hero"
        self.current_health = health
        self.total_health = health
        self.movement_speed = movement_speed

        # check that the dimensions specified in box are within bounds
        is_within_bounds(16, 128, box.height, "height")
        is_within_bounds(16, 128, box.width, "width")
        # TODO: need a way for the game to check that the player is within bounds?

        import_image = pygame.image.load(os.path.join("assets", asset_name))
        self.sprite = pygame.transform.scale(import_image, (box.width, box.height))
        self.rect = self.sprite.get_rect(center=(box.x, box.y))

        self.weapon = attack.Weapon(
            bullet_asset_name="h-shot20.png", magazine=5, speed=4, damage=2
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
        return self.weapon.fire(self.rect.centerx, self.rect.centery, 180)

    def take_damage(self, value):
        is_within_bounds(1, 9999, value, "player damage")
        self.current_health -= value
        if self.current_health <= 0:
            self.current_health = 0
            print("Player is dead")
