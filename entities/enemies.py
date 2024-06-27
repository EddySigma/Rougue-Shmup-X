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
        weapon: attack.Weapon = attack.Weapon(bullet_asset_name="shot 20.png"),
    ):
        super().__init__(img, rect, weapon)
        self.sprite_type = "enemy"
        self.backup_sprite = pygame.transform.rotate(self.sprite, 180)
        self.movement_speed = 2

    def turn_toward(self, target: baseActor.BaseActor):
        angle_to_target = self.angle_direction_to(target)

        angle_difference = (angle_to_target - self.viewing_angle + 180) % 360

        turn_direction = 0
        if angle_difference > 180:
            turn_direction = 2
        elif angle_difference < 180:
            turn_direction = -2

        self.viewing_angle += self.turning_speed * turn_direction

        self.viewing_angle %= 360
        img_copy = self.backup_sprite
        self.sprite = pygame.transform.rotate(img_copy, self.viewing_angle)
        self.rect = self.sprite.get_rect(center=(self.rect.centerx, self.rect.centery))

    def draw_x_sided_shape(self, center: baseActor.BaseActor, x_sides: int):
        pass

    def move_down_play_area(self, shape: str, x_pos: int, height: int):
        # shapes saw tooth, sin wave, square wave
        boundary_width = 64
        start_point = boundary_width / 2

        pass

    def move_in_direction(self, angle: float):
        x = math.sin(math.radians(angle)) * self.movement_speed
        y = math.cos(math.radians(angle)) * self.movement_speed

        self.rect.x += int(x)
        self.rect.y += int(y)

    def spiral_around_player(
        self, player: baseActor.BaseActor, stop_from_player: int, angle_change: float
    ):
        angle_from_player = self.angle_direction_to(player)
        distance_from_player = self.find_squared_distance_to(player)

        tangent_to_player = 90 + angle_from_player
        angle_of_attack = tangent_to_player - angle_change

        if distance_from_player > stop_from_player**2:
            self.move_in_direction(angle_of_attack)
        else:
            self.move_in_direction(tangent_to_player)

        print("distance from squared distance: ", distance_from_player)
        if angle_from_player < 90 and angle_from_player > 80:
            return self.weapon.fire(
                self.rect.centerx, self.rect.centery, self.viewing_angle
            )
        else:
            return None

    def behavior(self, player):
        self.turn_toward(player)
        return self.spiral_around_player(player, 150, 4)
        
