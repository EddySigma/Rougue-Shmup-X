#!/usr/bin/venv python

import pygame
import os
from Attacks import Bullet
    
class Enemy:
    def __init__(
        self,
        asset_name: str,
        x: int = 100,
        y: int = 100,
        width: int = 64,
        height: int = 64
    ):
        self.asset_name = asset_name
        self.sprite = self.generate_image(x, y, width, height)
        self.sprite_type = "enemy"

        self.health = 100
        self.movement_speed = 2
        self.reaction_delay = 750

        self.shot_speed = 3
        self.shot_delay = 750
        self.previous_time = pygame.time.get_ticks()

    def generate_image(self, x, y, width, height):
        self.sprite = pygame.Surface((height, width))

        if self.asset_name != "":
            self.import_sprite = pygame.image.load(os.path.join("assets", self.asset_name))
            self.sprite = pygame.transform.scale(self.import_sprite, (width, height))
        else:
            print("Invalid asset name!")
        self.rect = self.sprite.get_rect(center=(x, y))
        print("Ships:generate_image ", type(self.sprite))


    # this behavior is just to follow the player x position while keeping its distance
    def behavior(self, player_x_pos, player_y_pos):
        # this is kind of frog like behavior
        time_now = pygame.time.get_ticks()
        if time_now - self.previous_time > self.reaction_delay:
            if player_x_pos > self.x_pos:
                self.rect.x += self.movement_speed

            if player_x_pos < self.x_pos:
                self.rect.x -= self.movement_speed

            if player_y_pos > self.y_pos:
                self.rect.y += self.movement_speed

            if player_y_pos < self.y_pos:
                self.rect.y -= self.movement_speed

        time_now = pygame.time.get_ticks()
        if time_now - self.previous_time > self.shot_delay * 1000:
            self.previous_time = time_now
            return self.shoot()
        

    def shoot(self):
        return Bullet(
            move_type="down",
            asset_name="enemy shot 1-10.png",
            width=2,
            height=20,
            x=self.rect.centerx,
            y=self.rect.y,
            vel=4
        )