#!/usr/bin/venv python

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
    con = Controller(model, view)

    clock = pygame.time.Clock()

    running = True
    while running:
        FPS = 60
        clock.tick(FPS)

        running = con.run()
        view.display_elements()

        pygame.display.flip()  # this is the refresh of the screen/window

    pygame.quit()


if __name__ == "__main__":
    main()
