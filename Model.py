from ships import Hero


class Model:
    def __init__(self):
        self.player = Hero(100, "hero 2.png", 64, 64)
        self.player_attacks = []
        self.enemies = []
        self.enemy_attacks = []

    """
    Here: Should I have a means to generate new enemies and bullets? (fabric(s?))
    I would guess that the controller will tell the model to make more of the enemies
    """