import pygame
from dataclasses import dataclass
from entities.attacks import Bullet

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.running = True

        self.PLAYER_GOT_HIT = pygame.USEREVENT + 1
        self.ENEMY_GOT_HIT = pygame.USEREVENT + 2

    def run(self):
        keys_pressed = pygame.key.get_pressed()

        self.handle_user_events()
        self.handle_user_input(keys_pressed)
        self.handle_bullets()
        self.enemy_activity(self.model.player.rect.x, self.model.player.rect.y)
        self.handle_player_ship_and_enemy_bullet_collision()

        self.send_items_to_display()
        return self.running

    def handle_user_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    # Note: x increases from left to right and y increases from top to
    # bottom
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

        if keys_pressed[pygame.K_SPACE]:
            self.model.player_attacks.append(self.model.player.shot())

    def handle_bullets(self):
        for bullet in self.model.player_attacks:
            bullet.move_straight()
        for bullet in self.model.enemy_attacks:
            bullet.move_straight()

    def handle_player_ship_and_enemy_bullet_collision(self):
        for bullet in self.model.enemy_attacks:
            """
            if self.model.player.sprite.get_rect().colliderect(bullet):
                pygame.event.post(pygame.event.Event(self.ENEMY_GOT_HIT))
                self.model.enemy_attacks.remove(bullet)
                print("Hit 1")"""
        return

    def handle_enemy_ship_and_player_bullet_collision(self):
        for bullet in self.model.enemy_attacks:
            if self.model.player.colliderect(bullet):
                pygame.event.post(pygame.event.Event(self.ENEMY_GOT_HIT))
                self.model.enemy_attacks.remove(bullet)
                print("Hit 1")
        return

    def enemy_activity(self, player_x_pos, player_y_pos):
        for enemy in self.model.enemies:
            bullet = enemy.behavior(player_x_pos, player_y_pos)
            if isinstance(bullet, Bullet):
                self.model.enemy_attacks.append(bullet)

    def send_items_to_display(self):
        display_paiload = []
        for assets in (
            self.model.player_attacks,
            self.model.enemy_attacks,
            self.model.enemies,
        ):
            #print("asses: ", self.model.enemies)
            for asset in assets:
                print("asses: ", asset.sprite, " ", asset.sprite_type)
                display_paiload.append((asset.sprite, asset.sprite_type)) # send image and rect
        display_paiload.append((self.model.player.sprite, self.model.player.sprite_type))
        print("payload: ", display_paiload)
        self.view.add_to_display_queue(display_paiload)
