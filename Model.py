from entities.heroes import Hero
from entities.enemies import Enemy
from entities.attack import Bullet

class Model:
    def __init__(self):
        self.player = Hero(asset_name="hero 2.png")
        
        self.player_attacks = []
        self.enemies = []
        self.enemy_attacks = []
        # sample enemy
        temp = Enemy(asset_name = "bomb 128.png")
        self.enemies.append(temp)
        self.enemy_attacks.append(Bullet("down","enemy shot 1-10.png"))