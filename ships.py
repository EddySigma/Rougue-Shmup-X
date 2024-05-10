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
        self.fire_rate = 300
        self.previous_time = pygame.time.get_ticks()
        self.movement_speed = 2  # as far as I know this is tied to frame rate... is there a way to fix that?
        self.asset_name = asset_name
        self.sprite = self.generate_ship()

    def generate_ship(self):
        self.IMAGE = pygame.image.load(os.path.join("assets", self.asset_name))
        return pygame.transform.scale(self.IMAGE, (self.width, self.height))

    def change_ship_size(self, new_width, new_height):
        self.sprite = pygame.transform.scale(self.IMAGE, (self.width, self.height))

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

    
    def shot(self):
        shot = Bullet("shot 1-10.png")
        time_now = pygame.time.get_ticks() # there is got to be a better way...
        if (time_now - self.previous_time > self.fire_rate):
            self.previous_time = time_now
            shot = Bullet("shot 1-10.png", width=3, height=30, x_pos=self.x_pos + self.width//2 -1, y_pos=self.y_pos)
        return shot
# ========================================================================

"""
All enemies have health, position (x, y), size (height, width), an asset
"""


class Enemy:
    def __init__(self, asset_name, health=100, height=64, width=64, movement_speed=1, shot_speed=3, shot_delay=1):
        self.asset_name = asset_name
        self.health = health
        # this initial values are to spawn outside the viewable area
        self.x_pos = 400
        self.y_pos = 100
        self.height = height
        self.width = width
        self.movement_speed = movement_speed
        self.reaction_delay = 750
        self.shot_speed = shot_speed
        self.previous_time = pygame.time.get_ticks()
        self.shot_delay = shot_delay
        self.sprite = self.generate_sprite()

    def generate_sprite(self):
        self.IMAGE = pygame.image.load(os.path.join("assets", self.asset_name))
        return pygame.transform.scale(self.IMAGE, (self.width, self.height))

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

    """ Goal of this behavior:
     The enemy will have the same reaction time to a human or around that level of reaction.
     From there is the enemy is doing something it will continue duing said thing, until the
     time that it "realizes" that the player is doing something else (moving in a different
     direction). At that point it will change its direction.
    """

    def shoot(self):
        return Bullet("enemy shot 1-10.png", width=2, height=20, x_pos=self.x_pos + self.width//2, y_pos=self.y_pos, vel=4, dire=-90)


"""
For the bullet class bullets will initially spawn outside the view of the player and have a
default direction and velocity that can be changed. NOTE: look into using data classes for this
later... maybe?
"""

class Bullet():
    def __init__(self, asset_name, width=2, height=20, x_pos=-100, y_pos=-100, vel=4, dire=90):
        self.asset_name = asset_name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.velocity = vel
        self.direction = dire
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