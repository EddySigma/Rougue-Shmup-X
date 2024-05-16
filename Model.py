from entities.HeroShips import Hero
from entities.EnemyShips import Enemy


class Model:
    def __init__(self):
        self.player = Hero(asset_name="hero 2.png")
        
        self.player_attacks = []
        self.enemies = []
        self.enemy_attacks = []
        # sample enemy
        self.enemies.append(Enemy(asset_name = "bomb 128.png"))