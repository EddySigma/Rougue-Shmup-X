import os
import math
import pygame
from . import attack


class BaseActor:
    """ BaseActor acts as base class for anything that can take damage. There are a few
    functions added to help with player characters and enemy behavior. """
    def __init__(
        self,
        img: pygame.surface = pygame.image.load(os.path.join("assets", "test img.png")),
        rect: pygame.Rect = pygame.Rect(0, 0, 64, 64),
        weapon: attack.Weapon = attack.Weapon(bullet_asset_name="shot 20.png"),
    ):
        self.sprite = pygame.transform.scale(img, (rect.width, rect.height))
        self.backup_sprite = self.sprite
        self.rect = self.sprite.get_rect(center=(rect.center))
        print(self.rect.center)
        self.weapon = weapon

        self.sprite_type = ""
        self._total_health = 10
        self.health = self._total_health
        self.movement_speed = 1
        self.is_alive = True
        self.viewing_angle = 0
        self.turning_speed = 1

    def take_damage(self, value):
        #is_within_bounds(1, 9999, value, "player damage")
        self.health -= value
        if self.health <= 0:
            self.health = 0
            self.is_alive = False

    def increase_health(self, amount: int):
        """ Function to increase health, its use is encouraged to ensure that
        current health also is increased """
        # TODO: add a check here that the amount is neither bellow zero, nor too large
        self._total_health += amount
        self.health += amount

    def find_squared_distance_to(self, another: "BaseActor"):
        """ Distance function that remains squared to make it faster """
        return (
            (self.rect.centerx - another.rect.centerx)^ 2 +
            (self.rect.centery - another.rect.centery)^ 2
        )

    def find_distance_to(self, another: "BaseActor"):
        """Simple distance function taking self as one of the points"""
        return math.sqrt(self.find_squared_distance_to(another))

    def angle_direction_to(self, another: "BaseActor"):
        """ Function to determine the direction  """
        angle = math.degrees(
            math.atan2(
                (another.rect.centerx - self.rect.centerx),
                (another.rect.centery - self.rect.centery),
            )
        )
        return angle