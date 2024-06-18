from entities.heroes import Hero
from entities.enemies import Enemy

class Model:
    def __init__(self):
        self.player = Hero(asset_name="hero 2.png")
        
        self.player_attacks = []
        self.player_muscle_flash = []
        self.enemies = []
        self.enemy_attacks = []
        self.shot_explosions = []
        # sample enemy
        self.temp = Enemy(asset_name = "scout 256.png", x=300, y=100)
        self.enemies.append(self.temp)

    def get_displayable_items(self):
        entities = (
            self.player_attacks + self.enemy_attacks + self.enemies
        )
        entities.append(self.player)
        entities.extend(self.shot_explosions)
        return entities