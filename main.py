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
from Controller import Controller
from View import View
from Model import Model

def main():
    pygame.init()

    model = Model()
    view = View()
    clock = pygame.time.Clock()

    running = True
    while running:
        FPS = 60
        clock.tick(FPS)

        running = Controller(model, view)
        
        pygame.display.flip()  # this is the refresh of the screen/window

    pygame.quit()


if __name__ == "__main__":
    main()