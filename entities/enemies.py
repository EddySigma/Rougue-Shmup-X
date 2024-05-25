#!/usr/bin/venv python

import pygame
import os
from . import attack
    
class Enemy:
    def __init__(
        self,
        asset_name: str,
        x: int = 100,
        y: int = 100,
        width: int = 64,
        height: int = 64,
        shot_damage: int = 2
    ):
        self.asset_name = asset_name
        self.generate_image(x, y, height, width)
        self.shot_damage = shot_damage
        self.sprite_type = "enemy"

        self.is_alive = True
        self.current_health = 100
        self.total_health = 100
        self.movement_speed = 2
        self.reaction_delay = 750

        self.shot_speed = 3
        self.shot_delay = 750
        self.previous_time = pygame.time.get_ticks()


    def generate_image(self, x, y, height, width):
        self.import_sprite = pygame.image.load(os.path.join("assets", self.asset_name))
        self.sprite = pygame.transform.scale(self.import_sprite, (height, width))
        self.sprite = pygame.transform.rotate(self.sprite, 180)
        self.rect = self.sprite.get_rect(center=(x, y))


    # this behavior is just to follow the player x position while keeping its distance
    def behavior(self, player_x_pos, player_y_pos):
        # this is kind of frog like behavior
        time_now = pygame.time.get_ticks()
        if time_now - self.previous_time > self.shot_delay:
            self.previous_time = time_now
            return self.shoot()
            """
            if player_x_pos > self.rect.x:
                self.rect.x += self.movement_speed

            if player_x_pos < self.rect.x:
                self.rect.x -= self.movement_speed

            if player_y_pos > self.rect.y:
                self.rect.y += self.movement_speed

            if player_y_pos < self.rect.y:
                self.rect.y -= self.movement_speed
            """
        #self.previous_time = pygame.time.get_ticks()
        # shoot if player is underneath enemy and x time has elapsed
        #if time_now - self.previous_time > self.shot_delay * 1000:
            #self.previous_time = time_now
            #self.shoot()
        

    def shoot(self):
        shot = attack.Bullet(
            asset_name="enemy shot 1-10.png",
            x=self.rect.centerx,
            y=self.rect.centery,
            vel=4,
            width=4,
            height=30,
        )
    
        return shot
    
    
    def take_damage(self, value):
        self.current_health -= value
        if self.current_health <= 0:
            self.is_alive = False