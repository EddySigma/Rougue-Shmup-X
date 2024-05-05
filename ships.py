#!/usr/bin/venv python

import pygame
import os


class Hero:
    def __init__(self, health, asset_name, height, width):
        # Initial values here
        self.x_pos = (width / 2) + (600 / 2)  # center of the screen
        self.y_pos = 400
        self.height = height
        self.width = width
        self.health = health
        self.movement_speed = 2  # as far as I know this is tied to frame rate... is there a way to fix that?
        self.asset_name = asset_name
        self.ship = self.generate_ship()

    def generate_ship(self):
        self.IMAGE = pygame.image.load(os.path.join("assets", self.asset_name))
        print(type(self.IMAGE))
        return pygame.transform.scale(self.IMAGE, (self.width, self.height))

    def change_ship_size(self, new_width, new_height):
        self.ship = pygame.transform.scale(self.IMAGE, (self.width, self.height))

    # TODO: add behavior to change the color or some sprites depending on certain events
    # def change_color_filter(new_values):
    # research this bit to modify the color of items
    # self.SHIP.fill((0, 0, 0, 100), special_flags=pygame.BLEND_ADD)

    def move_right(self):
        self.x_pos += self.movement_speed

    def move_left(self):
        self.x_pos -= self.movement_speed

    def move_forward(self):
        self.y_pos -= self.movement_speed

    def move_back(self):
        self.y_pos += self.movement_speed


# ========================================================================

"""
All enemies have health, position (x, y), size (height, width), an asset
"""
