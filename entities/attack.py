#!/usr/bin/venv python

"""
These are the possible attacs of the player and enemies
"""

import os
import math
import pygame

class Bullet2:
    def __init__(
        self,
        img: pygame.surface,
        img_rect: pygame.Rect,
        damage: int,
        direction: int,
        magnitude: int,
    ):
        self.sprite = img
        self.rect = img_rect
        self.sprite_type = "bullet"
        self.damage = damage
        self.direction = direction
        self.magnitude = magnitude

    def _match_img_and_direction(self):
        self.sprite = pygame.transform.rotate(self.sprite, self.direction)

    def update(self):
        """
        updates the location of the bullet based on magnitude and direction in degrees
        """
        # move the bullet to the next expected location
        x = math.sin(math.radians(self.direction)) * self.magnitude
        y = math.cos(math.radians(self.direction)) * self.magnitude

        self.rect.x += int(x)
        self.rect.y += int(y)


class Explosion:
    def __init__(
        self,
        asset_name: str,
        x: int = 100,
        y: int = 100,
        width: int = 10,
        height: int = 10,
    ):
        self.asset_name = asset_name
        self.generate_image(x, y, width, height)
        self.sprite_type = "bullet"

    def generate_image(self, x, y, width, height):
        self.import_sprite = pygame.image.load(os.path.join("assets", self.asset_name))
        self.sprite = pygame.transform.scale(self.import_sprite, (width, height))
        self.rect = self.sprite.get_rect(center=(x, y))


class Weapon:
    """
    This class essentially stores information relevant to the shooting capabilities of
    both enemies and the player character. In the future this could be used to make
    actual weapons that can have their own sprites and abilities.
    """

    def __init__(
        self, bullet_asset_name: str, magazine: int = 3, speed: int = 2, damage: int = 1
    ):
        import_bullet_image = pygame.image.load(os.path.join("assets", bullet_asset_name))
        self.bullet_sprite = pygame.transform.scale(import_bullet_image, (10, 10))
        self.shot_type = "default"  # dependency injection?
        self.magazine_size = magazine
        self.magazine = magazine
        self.shot_speed = speed
        self.shot_damage = damage
        self.reload_delay = 1000
        self.shot_delay = 250
        self.time_sice_last_shot = pygame.time.get_ticks()

    def make_bullet(self, x, y, direction):
        """ make a bullet with a given position, direction and magnitude """

        bullet_img = self.bullet_sprite
        bullet_rect = bullet_img.get_rect(center=(x, y))

        return Bullet2(bullet_img, bullet_rect, self.shot_damage, direction, self.shot_speed)

    def fire(self, x: int, y: int, direction: int):
        """
        The weapon will be allowed to fire if there are bullets in the magazine and
        the time requirements are met. If they are not, no bullet will be fired or
        the magazine will be refilled and after a moment and the gun will be allowed
        to fire
        """
        print("shooting angle: ", direction)
        bullet = None
        new_time = pygame.time.get_ticks()
        if new_time - self.time_sice_last_shot >= self.shot_delay:
            if self.magazine > 0:
                bullet = self.make_bullet(x,y,direction)
                self.magazine -= 1
                self.time_sice_last_shot = pygame.time.get_ticks()

            elif new_time - self.time_sice_last_shot >= self.reload_delay:
                self.magazine = self.magazine_size
                self.time_sice_last_shot = pygame.time.get_ticks() + self.shot_delay

        return bullet