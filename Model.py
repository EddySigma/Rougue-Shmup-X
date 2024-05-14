from ships import Hero
from ships import Enemy


class Model:
    def __init__(self):
        self.player = Hero(asset_name="hero 2.png")
        
        self.player_attacks = []
        self.enemies = []
        self.enemy_attacks = []
        # sample enemy
        self.enemies.append(Enemy("bomb 128.png", movement_speed=2, shot_delay=1))