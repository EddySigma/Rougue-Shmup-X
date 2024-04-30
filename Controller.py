import pygame
from dataclasses import dataclass

@dataclass
class Thing:
    image: pygame.surface.Surface
    x_pos: int
    y_pos: int

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.running = True
        
    
    def run(self):
        keys_pressed = pygame.key.get_pressed()
        self.handle_user_events()
        self.handle_user_input(keys_pressed)
        self.display_to_screen()
        return self.running

    def handle_user_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    # 0.25 and 0.75 are used to allow the player to exede the play area slightly
    # My thinking is that this will help the player dodge things by having a
    # a little more space to work with.

    def handle_user_input(self, keys_pressed):
        if (keys_pressed[pygame.K_w]
            and self.model.player.y_pos >= (0 - self.model.player.height) * 0.25):
            self.model.player.move_forward()

        if (keys_pressed[pygame.K_s]
            and self.model.player.y_pos <= self.view.PLAY_AREA_HEIGHT - (self.model.player.height * 0.75)):
            self.model.player.move_back()

        if (keys_pressed[pygame.K_a]
            and self.model.player.x_pos >= (0 - self.model.player.width) * 0.25):
            self.model.player.move_left()

        if (keys_pressed[pygame.K_d] 
            and self.model.player.x_pos <= self.view.PLAY_AREA_WIDTH - (
            self.model.player.width * 0.75)):
            self.model.player.move_right()
        

    def display_to_screen(self):
        paiload = []
        paiload.append(Thing(self.model.player.ship, self.model.player.x_pos, self.model.player.y_pos))
        
        for item in self.model.player_attacks:
            paiload.append(Thing(item.image, item.x_pos, item.y_pos))

        for item in self.model.enemies:
            paiload.append(Thing(item.image, item.x_pos, item.y_pos))
        
        for item in self.model.enemy_attacks:
            plaiload.append(Thing(item.sprite, item.x_pos, item.y_pos))

        self.view.add_to_display_queue(paiload)