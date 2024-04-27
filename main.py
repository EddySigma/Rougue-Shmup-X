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



def main():
    pygame.init()

    # --- MODEL ---
    # window icon and text
    SHIP_ICON = pygame.image.load(os.path.join("assets", "icon 32.png"))
    pygame.display.set_icon(SHIP_ICON)
    pygame.display.set_caption("Shmup")


    WIDTH, HEIGHT = 900, 800
    window = pygame.display.set_mode((WIDTH, HEIGHT))  # notice the double parenthesis
    clock = pygame.time.Clock()


    PLAY_AREA_WIDTH = 600
    PLAY_AREA_HEIGHT = 800
    border_asset = pygame.image.load(os.path.join("assets", "border 600x800.png"))
    border = pygame.transform.scale(border_asset, (PLAY_AREA_WIDTH, PLAY_AREA_HEIGHT))

    player = Hero(100, "hero 2.png", 64, 64)

    running = True
    while running:
        # --- CONTROLLER ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:  # this is for single press events
                if event.key == pygame.K_ESCAPE:
                    x = 1  # pause game here
                    # expected behavior:
                    # display buttons for restart, quit and maybe something else?

        # player input
        keys_pressed = pygame.key.get_pressed()
        # The 0.25 is the amount of the sprite that sticks out of the playable area
        # The 0.75 has the same purpose for the opposite sides
        # TODO: rename this value to something understandable and make it a constant

        if keys_pressed[pygame.K_w] and player.y_pos >= (0 - player.height) * 0.25:
            player.move_forward()
        if keys_pressed[pygame.K_s] and player.y_pos <= PLAY_AREA_HEIGHT - (player.height * 0.75):
            player.move_back()
        if keys_pressed[pygame.K_a] and player.x_pos >= (0 - player.width) * 0.25:
            player.move_left()
        if keys_pressed[pygame.K_d] and player.x_pos <= PLAY_AREA_WIDTH - (player.width * 0.75):
            player.move_right()

        if keys_pressed[pygame.K_SPACE]:
            x =1 # shoot
        if keys_pressed[pygame.K_LSHIFT]:
            x =1 # rocket/shield/bomb?

        # fill the screen with a color to wipe away anything from last frame
        window.fill("black")


        # --- VIEW ---
        # render your game here
        window.blit(player.ship, (player.x_pos, player.y_pos))
        #window.blit(NEMESIS_SHIP, (125, 15))

        # Border should always be last to make sure that its on top of everything else in playarea
        window.blit(border, (0,0))
        # flip() the display to put your work on screen
        pygame.display.flip()  # this is the refresh of the screen/window


        FPS = 60
        clock.tick(FPS)

    pygame.quit()


main()