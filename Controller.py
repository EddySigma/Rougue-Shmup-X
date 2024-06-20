from collections import namedtuple
import pygame
from model import Model
from view import View
from entities import attack



class Controller:
    def __init__(self, model, view):
        self.model: Model = model
        self.view: View = view
        self.running = True

        self.PLAYER_GOT_HIT = pygame.USEREVENT + 1
        self.ENEMY_GOT_HIT = pygame.USEREVENT + 2

    def run(self):
        keys_pressed = pygame.key.get_pressed()

        self.handle_user_events()
        self.handle_user_input(keys_pressed)
        self.handle_bullets()
        self.enemy_activity(self.model.player.rect.centerx, self.model.player.rect.centery)
        self.handle_player_ship_and_enemy_bullet_collision()
        self.handle_enemy_ship_and_player_bullet_collision()
        self.send_items_to_display()
        self.send_data_to_display()

        return self.running

    def handle_user_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v:  # cycle through T/F
                    if not self.view.viewable_boxes:
                        self.view.visible_boxes()
                    else:
                        self.view.invisible_boxes()

    # Note: x increases from left to right and y increases from top to
    # bottom
    # 16 and 48 are the space that the ship is allowed to extend past the
    # play area.

    def handle_user_input(self, keys_pressed):
        if (
            (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP])
            and self.model.player.rect.y >= -16
        ):
            self.model.player.move_forward()

        if (
            (keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN])
            and self.model.player.rect.y <= self.view.PLAY_AREA_HEIGHT - 48
        ):
            self.model.player.move_back()

        if (
            (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT])
            and self.model.player.rect.x >= -16
        ):
            self.model.player.move_left()

        if (
            (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT])
            and self.model.player.rect.x <= self.view.PLAY_AREA_WIDTH - 48
        ):
            self.model.player.move_right()

        if keys_pressed[pygame.K_SPACE]:
            shot = self.model.player.shoot()
            if shot is not None:
                self.model.player_attacks.append(shot)

    def handle_bullets(self): # TODO: make function out of bounds
        for bullet in self.model.player_attacks:
            bullet.move_up()
            if bullet.rect.y < -10:
                self.model.player_attacks.remove(bullet)

        for bullet in self.model.enemy_attacks:
            bullet.update()
            if bullet.rect.y > 810:
                self.model.enemy_attacks.remove(bullet)

    def handle_player_ship_and_enemy_bullet_collision(self):
        for bullet in self.model.enemy_attacks:
            if self.model.player.rect.colliderect(bullet):
                self.model.enemy_attacks.remove(bullet)
                self.model.player.take_damage(bullet.damage)
                
                self.model.shot_explosions.append(attack.Explosion(
                        asset_name = "shot explosion 256.png",
                        x=bullet.rect.centerx,
                        y=bullet.rect.y,
                        width=10,
                        height=10,
                    ))
            if self.model.player.current_health <= 0:
                self.model.player.current_health = 0
                self.running = False

    def handle_enemy_ship_and_player_bullet_collision(self):
        for bullet in self.model.player_attacks:
            for enemy in self.model.enemies:
                if enemy.rect.colliderect(bullet):
                    enemy.take_damage(bullet.damage)
                    
                    self.model.shot_explosions.append(attack.Explosion(
                        asset_name = "shot explosion 256.png",
                        x=bullet.rect.centerx,
                        y=bullet.rect.y,
                        width=10,
                        height=10,
                    ))
                    self.model.player_attacks.remove(bullet)

                if enemy.current_health <= 0:
                    self.model.enemies.remove(enemy)
        return

    def enemy_activity(self, player_x_pos, player_y_pos):
        for enemy in self.model.enemies:
            bullet = enemy.behavior(player_x_pos, player_y_pos)
            if (bullet != None):
                self.model.enemy_attacks.append(bullet)

    def send_items_to_display(self):
        display_paiload = []
        assets = self.model.get_displayable_items()

        for asset in assets:
            display_paiload.append(self.make_display_entity(asset))
        self.view.add_to_display_queue(display_paiload)

    def make_display_entity(self, sprite):
        Display_entity = namedtuple("Display_entity", ["image", "rect", "category"])
        entity = Display_entity(
            image=sprite.sprite,
            rect=sprite.rect,
            category=sprite.sprite_type,
        )
        return entity

    def send_data_to_display(self):
        self.view.display_information = {
            "current_player_hp": self.model.player.current_health,
            "total_player_hp": self.model.player.total_health,
        }



# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====

def main():
    pygame.init()

    model = Model()
    view = View() 
    controller = Controller(model, view)

    clock = pygame.time.Clock()
    FPS = 60

    running = True
    while running:
        clock.tick(FPS)
        running = controller.run()
        view.display_elements()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()