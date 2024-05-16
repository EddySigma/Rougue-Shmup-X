#!/usr/bin/venv python

import pygame
import os
import dataclasses

class BaseShip:
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

    def generate_image(self, x, y, width, height):
        #self.sprite = pygame.Surface((height, width))

        if self.asset_name != "":
            self.import_sprite = pygame.image.load(os.path.join("assets", self.asset_name))
            self.sprite = pygame.transform.scale(self.import_sprite, (width, height))
        else:
            print("Invalid asset name!")
        self.rect = self.sprite.get_rect(center=(x, y))
        print("Ships:generate_image ", type(self.sprite))
    

class Hero(BaseShip):
    def __init__(
        self,
        asset_name: str,
        x: int = 100,
        y: int = 100,
        width: int = 64,
        height: int = 64
    ):
        super().__init__(asset_name, x, y, width, height)
        self.sprite_type = "hero"
        self.fire_rate = 300
        self.movement_speed = 2  # as far as I know this is tied to frame rate... is there a way to fix that?
        self.previous_time = pygame.time.get_ticks()
        print("Ships:hero:init ", type(self.sprite))

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


# ========================================================================


class Enemy(BaseShip):
    def __init__(
        self,
        asset_name: str,
        x: int = 100,
        y: int = 100,
        width: int = 64,
        height: int = 64
    ):
        super().__init__(asset_name, x, y, width, height)

        self.health = 100
        self.movement_speed = 2
        self.reaction_delay = 750
        self.shot_speed = 3
        self.shot_delay = 750
        self.sprite_type = "enemy"
        self.previous_time = pygame.time.get_ticks()

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


"""
For the bullet class bullets will initially spawn outside the view of the player and have a
default direction and velocity that can be changed. NOTE: look into using data classes for this
later... maybe?
"""

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

    def __post_init__(self):
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

    def move_with_curve(self):
        x = 1
