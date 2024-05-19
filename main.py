#!/usr/bin/venv python

import pygame
from controller import Controller
from view import View
from model import Model

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