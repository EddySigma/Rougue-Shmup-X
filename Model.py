from ships import Hero
from ships import Enemy

class Model:
    def __init__(self):
        self.player = Hero(100, "hero 2.png", 64, 64)
        self.player_attacks = []
        self.enemies = []
        self.enemy_attacks = []

    def make_an_enemy(self, type):
        x=1

    def add_scout(self):
        self.enemies.append(Scout(100, 300, 50, 32, 32, "scout 64.png", 3))

    """
    Here: Should I have a means to generate new enemies and bullets? (fabric(s?))
    I would guess that the controller will tell the model to make more of the enemies
    """