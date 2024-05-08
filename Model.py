from ships import Hero
from ships import Enemy

class Model:
    def __init__(self):
        self.player = Hero(100, "hero 2.png", 64, 64)
        self.player_attacks = []
        self.enemies = []
        self.enemy_attacks = []
        self.make_an_enemy()

    def make_an_enemy(self):
        self.enemies.append(Enemy("bomb 128.png", movement_speed=2, shot_delay=1))

    """
    Here: Should I have a means to generate new enemies and bullets? (fabric(s?))
    I would guess that the controller will tell the model to make more of the enemies
    """