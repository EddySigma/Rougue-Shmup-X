#!/usr/bin/venv python

import os
import math
import pygame
from . import attack
from . import baseActor


class Enemy2(baseActor.BaseActor):
    def __init__(
        self,
        img: pygame.surface = pygame.image.load(os.path.join("assets", "test img.png")),
        rect: pygame.Rect = pygame.Rect(100, 100, 64, 64),
        weapon: attack.Weapon = attack.Weapon(bullet_asset_name="shot 20.png")
    ):
        super().__init__(img, rect, weapon)
        self.sprite_type = "enemy"
        self.backup_sprite = pygame.transform.rotate(self.sprite, 180)

    def turn_toward(self, target: baseActor.BaseActor):
        angle_to_target = self.angle_direction_to(target)

        angle_difference = (angle_to_target - self.viewing_angle + 180) % 360

        turn_direction = 0
        if angle_difference > 180:
            turn_direction = 1
        elif angle_difference < 180:
            turn_direction = -1
        
        self.viewing_angle += self.turning_speed * turn_direction

        print ("viewing angle: ", self.viewing_angle)
        img_copy = self.backup_sprite
        self.sprite = pygame.transform.rotate(img_copy, self.viewing_angle)
        self.rect = self.sprite.get_rect(center = (self.rect.centerx, self.rect.centery))
        
    def behavior(self, player):
        # print(self.direction_to_player(player_x_pos, player_y_pos))
        self.turn_toward(player)
        return self.weapon.fire(self.rect.centerx, self.rect.centery, self.viewing_angle)