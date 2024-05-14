#!/usr/bin/venv python

import pygame
import os
import dataclasses


@dataclasses.dataclass
class BaseShip:
    asset_name : str = ""
    height : int = 64
    width : int = 64
    x_pos : int = 0
    y_pos : int = 0

    # Call post init after the position and size values have been updated
    def __post_init__(self):
        self.sprite = self.generate_image()
    
    def generate_image(self):
        surface = pygame.Surface((self.height, self.width))
        if (self.asset_name != ""):
            self.IMAGE = pygame.image.load(os.path.join("assets", self.asset_name))
            surface = pygame.transform.scale(self.IMAGE, (self.width, self.height))
        return surface # return empty with white if there is no asset_name

@dataclasses.dataclass
class Hero(BaseShip):
    def __post_init__(self):
        self.sprite_type = "hero"
        self.x_pos = 600 // 2
        self.y_pos = 400
        self.fire_rate = 300
        self.movement_speed = 2  # as far as I know this is tied to frame rate... is there a way to fix that?
        self.sprite = self.generate_image()
        self.previous_time = pygame.time.get_ticks()
        super().__post_init__()


    def change_ship_size(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
        self.sprite = pygame.transform.scale(self.IMAGE, (self.width, self.height))

    def move_right(self):
        self.x_pos += self.movement_speed

    def move_left(self):
        self.x_pos -= self.movement_speed

    def move_forward(self):
        self.y_pos -= self.movement_speed

    def move_back(self):
        self.y_pos += self.movement_speed

    
    def shot(self):
        shot = Bullet("shot 1-10.png")
        time_now = pygame.time.get_ticks() # there is got to be a better way...
        if (time_now - self.previous_time > self.fire_rate):
            self.previous_time = time_now
            shot = Bullet("shot 1-10.png", width=3, height=30, x_pos=self.x_pos + self.width//2 -1, y_pos=self.y_pos)
            
        return shot
# ========================================================================
    
@dataclasses.dataclass
class Enemy(BaseShip):
    health : int = 100
    movement_speed : int = 1
    reaction_delay : int = 750
    shot_speed : int = 3
    shot_delay : int = 750

    def __post_init__(self):
        self.sprite_type = "enemy"
        self.previous_time = pygame.time.get_ticks()
        self.sprite = self.generate_image()
        super().__post_init__()

    # this behavior is just to follow the player x position while keeping its distance
    def behavior(self, player_x_pos, player_y_pos):
        # this is kind of frog like behavior
        time_now = pygame.time.get_ticks()
        if (time_now - self.previous_time > self.reaction_delay):
            if(player_x_pos > self.x_pos):
                self.x_pos += self.movement_speed
            
            if(player_x_pos < self.x_pos):
                self.x_pos -= self.movement_speed

            if(player_y_pos > self.y_pos):
                self.y_pos += self.movement_speed
            
            if(player_y_pos < self.y_pos):
                self.y_pos -= self.movement_speed
        
        time_now = pygame.time.get_ticks()
        if (time_now - self.previous_time > self.shot_delay * 1000):
            self.previous_time = time_now
            return self.shoot()

    def shoot(self):
        return Bullet("enemy shot 1-10.png", width=2, height=20, x_pos=self.x_pos + self.width//2, y_pos=self.y_pos, velocity=4, direction=-90)


"""
For the bullet class bullets will initially spawn outside the view of the player and have a
default direction and velocity that can be changed. NOTE: look into using data classes for this
later... maybe?
"""
@dataclasses.dataclass
class Bullet():
    asset_name : str
    width : int = 2
    height : int = 20
    x_pos : int = -100
    y_pos : int = -100
    velocity : int = 4
    direction : float = 90
    damage : int = 1

    def __post_init__(self):
        self.sprite_type = "bullet"
        self.sprite = self.generate_bullet()

    def generate_bullet(self):
        self.IMAGE = pygame.image.load(os.path.join("assets", self.asset_name))
        return pygame.transform.scale(self.IMAGE, (self.width, self.height))
    
    def move_straight(self):
        if(self.direction == -90):
            self.y_pos += self.velocity
    
        if(self.direction == 90):
            self.y_pos -= self.velocity
    
    def move_with_angle(self):
        x=1

    def calculate_next_pos(self):
        vector = pygame.math.Vector2()
        vector.from_polar((self.velocity, self.direction))
        return ((self.x_pos, self.y_pos) + vector)

    def move_with_curve(self):
        x=1