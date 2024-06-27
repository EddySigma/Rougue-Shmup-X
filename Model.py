import os
import pygame
from entities.heroes import Hero2
from entities.enemies import Enemy2
from entities.attack import Weapon

class Model:
    def __init__(self):
        #self.player = Hero(asset_name="hero 2.png")
        img = pygame.image.load(os.path.join("assets", "hero 1.png"))
        rect = pygame.Rect(100,500, 64, 64)
        weapon = Weapon(bullet_asset_name="h-shot20.png")
        self.player = Hero2(img, rect, weapon)
        self.player.increase_health(100)
        self.player.movement_speed = 2

        self.player_attacks = []
        self.player_muscle_flash = []
        self.enemies = []
        self.enemy_attacks = []
        self.shot_explosions = []
        # sample enemy
        #self.temp = Enemy(asset_name = "scout 256.png", x=300, y=100)
        enemy_img = pygame.image.load(os.path.join("assets", "scout 256.png"))
        enemy_rect = pygame.Rect(100, 400, 64, 64)
        enemy_weapon = Weapon(bullet_asset_name="shot 20.png")
        self.temp = Enemy2(enemy_img, enemy_rect, enemy_weapon)
        self.temp.movement_speed = 3
        self.enemies.append(self.temp)
        enemy_rect = pygame.Rect(200, 400, 64, 64)
        self.temp2 = Enemy2(enemy_img, enemy_rect, enemy_weapon)
        self.temp2.movement_speed = 3
        self.enemies.append(self.temp2)


    def get_displayable_items(self):
        entities = (
            self.player_attacks + self.enemy_attacks + self.enemies
        )
        entities.append(self.player)
        entities.extend(self.shot_explosions)
        return entities