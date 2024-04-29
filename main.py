#!/usr/bin/venv python

""" Testing ground for game development. """

# TODO: Change color of things when changing behavior
# red: rush, low health, fast
# black/gray: tank
# blue: mirror match
# green bombs
# yellow: lasers
# purple: shield, wave attack

# TODO: new sprites
# health pick up
# health upgrade
# shot upgrade
# bomb
# bomb upgrade
# shield
# shield upgrade
# upgrade container
# shrink upgrade

import pygame
import os
from ships import Hero


class Controller:
    def __init__(self, data_model, obj_view):
        self.running = True
        self.keys_pressed = pygame.key.get_pressed()
        self.model = data_model
        self.view = obj_view

    def user_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:  # this is for single press events
                if event.key == pygame.K_ESCAPE:
                    x = 1  # pause game here
                    # expected behavior:
                    # display buttons for restart, quit and maybe something else?


    # The 0.25 is the amount of the sprite that sticks out of the playable area
    # The 0.75 has the same purpose for the opposite sides
    # TODO: rename this value to something understandable and make it a constant

    def handle_user_input(self):
        if self.keys_pressed[pygame.K_w] and self.model.player.y_pos >= (0 - self.model.player.height) * 0.25:
            self.model.player.move_forward()
        if self.keys_pressed[pygame.K_s] and self.model.player.y_pos <= self.view.PLAY_AREA_HEIGHT - (self.model.player.height * 0.75):
            self.model.player.move_back()
        if self.keys_pressed[pygame.K_a] and self.model.player.x_pos >= (0 - self.model.player.width) * 0.25:
            self.model.player.move_left()
        if self.keys_pressed[pygame.K_d] and self.model.player.x_pos <= self.view.PLAY_AREA_WIDTH - (self.model.player.width * 0.75):
            self.model.player.move_right()

        if self.keys_pressed[pygame.K_SPACE]:
            x =1 # shoot
        if self.keys_pressed[pygame.K_LSHIFT]:
            x =1 # rocket/shield/bomb?

    def isRunning(self):
        return self.running

class View:
    def __init__(self):
        # window icon and text
        SHIP_ICON = pygame.image.load(os.path.join("assets", "icon 32.png"))
        pygame.display.set_icon(SHIP_ICON)
        pygame.display.set_caption("Shmup")

        self.WIDTH, self.HEIGHT = 900, 800
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))  # notice the double parenthesis


        self.PLAY_AREA_WIDTH = 600
        self.PLAY_AREA_HEIGHT = 800
        self.BORDER_ASSET = pygame.image.load(os.path.join("assets", "border 600x800.png"))
        self.BORDER = pygame.transform.scale(self.BORDER_ASSET, (self.PLAY_AREA_WIDTH, self.PLAY_AREA_HEIGHT))
        # fill the screen with a color to wipe away anything from last frame
        self.window.fill("black")

        # Display everything that changes from model here
        # render your game here
        #self.window.blit(player.ship, (player.x_pos, player.y_pos))

        #self.display_player_ship()
        #self.display_enemies()
        #self.display_attacks()


        #window.blit(NEMESIS_SHIP, (125, 15))

        # Border should always be last to make sure that its on top of everything else in playarea
        self.window.blit(self.BORDER, (0,0))
        # flip() the display to put your work on screen

    def display_enemies(self, mob):
        for enemy in mob:
            self.window.blit(enemy.ship, (enemy.x_pos, enemy.y_pos))
    
    def display_attacks(self, container):
        for item in container:
            self.window.blit(item.sprite, (item.x_pos, item.y_pos))

    def display_player_ship(self, player_sprite, player_x_pos, player_y_pos):
        self.window.blit(player_sprite, (player_x_pos, player_y_pos))
    

class Model:
    def __init__(self):
        player = Hero(100, "hero 2.png", 64, 64)



def main():
    pygame.init()

    mod = Model()
    vie = View()
    clock = pygame.time.Clock()
    
    running = True
    while running:
        FPS = 60
        clock.tick(FPS)
        # --- CONTROLLER ---
        running = Controller(mod, vie)
        
        pygame.display.flip()  # this is the refresh of the screen/window

    pygame.quit()


main()