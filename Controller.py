import pygame
from dataclasses import dataclass


@dataclass
class Sprite:
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
        self.enemy_action(self.model.player.x_pos, self.model.player.y_pos)
        self.send_items_to_display()
        return self.running

    def handle_user_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    # 16 and 48 are the space that the ship is allowed to extend past the
    # play area.

    def handle_user_input(self, keys_pressed):
        if keys_pressed[pygame.K_w] and self.model.player.y_pos >= -16:
            self.model.player.move_forward()

        if (
            keys_pressed[pygame.K_s]
            and self.model.player.y_pos <= self.view.PLAY_AREA_HEIGHT - 48
        ):
            self.model.player.move_back()

        if keys_pressed[pygame.K_a] and self.model.player.x_pos >= -16:
            self.model.player.move_left()

        if (
            keys_pressed[pygame.K_d]
            and self.model.player.x_pos <= self.view.PLAY_AREA_WIDTH - 48
        ):
            self.model.player.move_right()


    def enemy_action(self):
        x=1

    def send_items_to_display(self):
        display_paiload = []
        display_paiload.append(
            Sprite(
                self.model.player.ship, self.model.player.x_pos, self.model.player.y_pos
            )
        )

        for asset in (
            self.model.player_attacks,
            self.model.enemies,
            self.model.enemy_attacks,
        ):
            for item in asset:
                display_paiload.append(Sprite(item.image, item.x_pos, item.y_pos))

        self.view.add_to_display_queue(display_paiload)
