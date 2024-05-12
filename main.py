#!/usr/bin/venv python

import pygame
from Controller import Controller
from View import View
from Model import Model

def main():
    pygame.init()

    model = Model()
    view = View()
    con = Controller(model, view)

    clock = pygame.time.Clock()
    FPS = 60

    running = True
    while running:
        clock.tick(FPS)
        running = con.run()
        view.display_elements()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()