#!/usr/bin/venv python

import os
import math
import pygame
from . import attack


class Enemy:
    def __init__(
        self,
        asset_name: str,
        x: int = 100,
        y: int = 100,
        width: int = 64,
        height: int = 64,
        shot_damage: int = 2,
        health: int = 100,
    ):
        self.asset_name = asset_name
        self.generate_image(x, y, height, width)
        self.shot_damage = shot_damage
        self.sprite_type = "enemy"

        self.is_alive = True
        self.current_health = health
        self.total_health = health
        self.movement_speed = 2
        self.reaction_delay = 750

        self.shot_speed = 3
        self.magazine_size = 4
        self.shots_taken = 0
        self.shot_delay = 750
        self.reload_delay = 2000
        self.previous_time = pygame.time.get_ticks()

    def generate_image(self, x, y, height, width):
        self._is_within_bounds(16, 128, height, "height")
        self._is_within_bounds(16, 128, width, "width")

        self.import_image = pygame.image.load(os.path.join("assets", self.asset_name))
        self.sprite = pygame.transform.scale(self.import_image, (height, width))
        self.sprite = pygame.transform.rotate(self.sprite, 180)
        self.rect = self.sprite.get_rect(center=(x, y))

    def _is_within_bounds(self, min_val, max_val, test_val, val_type):
        if test_val > max_val:
            raise ValueError(
                "Error: Value %s out of bounds %s is MAX expected, %s given."
                % (val_type, max_val, test_val)
            )
        if test_val < min_val:
            raise ValueError(
                "Error: Value %s out of bounds %s is MIN expected, %s given."
                % (val_type, min_val, test_val)
            )

    # this behavior is just to follow the player x position while keeping its distance
    def behavior(self, player_x_pos, player_y_pos):
        # this is kind of frog like behavior
        time_now = pygame.time.get_ticks()
        reload_time = 0
        if time_now - self.previous_time > self.shot_delay:
            self.shots_taken += 1
            if self.shots_taken >= self.magazine_size:
                reload_time = pygame.time.get_ticks()

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
        # self.previous_time = pygame.time.get_ticks()
        # shoot if player is underneath enemy and x time has elapsed
        # if time_now - self.previous_time > self.shot_delay * 1000:
        # self.previous_time = time_now
        # self.shoot()

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
        self._is_within_bounds(1, 9999, value, "player damage")
        self.current_health -= value
        if self.current_health <= 0:
            self.is_alive = False


class Enemy2:
    def __init__(
        self,
        asset_name: str,
        rect: pygame.Rect = pygame.Rect(100, 100, 64, 64),
        shot_damage: int = 2,
        health: int = 100,
    ):
        self.sprite_type = "enemy"
        self.is_alive = True

        self.current_health = health
        self.total_health = health
        self.movement_speed = 2
        self.current_angle = 0
        self.turning_speed = 1

        self.import_image = pygame.image.load(os.path.join("assets", asset_name))
        self.sprite = pygame.transform.scale(
            self.import_image, (rect.height, rect.width)
        )
        self.sprite = pygame.transform.rotate(self.sprite, 180)
        self.rect = self.sprite.get_rect(center=(rect.x, rect.y))

        self.weapon = attack.Weapon("enemy shot 1-10.png", 4, 4, shot_damage)

    def behavior(self, player_x_pos, player_y_pos):
        # print(self.direction_to_player(player_x_pos, player_y_pos))
        #self.turn_toward_player(player_x_pos, player_y_pos)
        return self.weapon.fire(self.rect.centerx, self.rect.centery, 0)

    def turn_toward_player(self, player_x_pos, player_y_pos):
        angle_to_player = self.direction_to_player(player_x_pos, player_y_pos)
        print(angle_to_player)

        turning_angle = 0
        if (angle_to_player > 0):
            if (angle_to_player > self.current_angle):
                turning_angle += 1
                self.current_angle += 1
            else:
                turning_angle -= 1
                self.current_angle -= 1
        if (angle_to_player < 0):
            if (angle_to_player < self.current_angle):
                turning_angle -= 1
                self.current_angle -= 1
            else:
                turning_angle += 1
                self.current_angle += 1

        temp_rect = self.rect
        self.sprite = pygame.transform.rotate(self.sprite, turning_angle)
        self.rect = self.sprite.get_rect(center=self.sprite.get_rect(center=(temp_rect.centerx, temp_rect.centery))).center

    def find_distance_from_player_squared(self, px, py):
        return (self.rect.x - px) ^ 2 + (self.rect.y - py) ^ 2

    def find_distance_from_player(self, px, py):
        return math.sqrt(self.find_distance_from_player(px, py))

    def direction_to_player(self, px, py):
        angle = math.degrees(
            math.atan2((px - self.rect.centerx), (py - self.rect.centery))
        )
        return(angle)

    def take_damage(self, value):
        self.current_health -= value
        if self.current_health <= 0:
            self.is_alive = False
