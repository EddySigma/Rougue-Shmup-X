import pygame


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.running = True        
        self.keys_pressed = pygame.key.get_pressed()
        self.user_events()

    def user_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:  # this is for single press events
                if event.key == pygame.K_ESCAPE:
                    x = 1  # pause game here
                    # expected behavior:
                    # display buttons for restart, quit and maybe something else?

    # The 0.25 is the amount of the sprite that sticks out of the playable area
    # The 0.75 has the same purpose for the opposite sides
    # TODO: rename this value to something understandable and make it a constant

    def handle_user_input(self):
        if (
            self.keys_pressed[pygame.K_w]
            and self.model.player.y_pos >= (0 - self.model.player.height) * 0.25
        ):
            self.model.player.move_forward()
        if self.keys_pressed[
            pygame.K_s
        ] and self.model.player.y_pos <= self.view.PLAY_AREA_HEIGHT - (
            self.model.player.height * 0.75
        ):
            self.model.player.move_back()
        if (
            self.keys_pressed[pygame.K_a]
            and self.model.player.x_pos >= (0 - self.model.player.width) * 0.25
        ):
            self.model.player.move_left()
        if self.keys_pressed[
            pygame.K_d
        ] and self.model.player.x_pos <= self.view.PLAY_AREA_WIDTH - (
            self.model.player.width * 0.75
        ):
            self.model.player.move_right()

        if self.keys_pressed[pygame.K_SPACE]:
            x = 1  # shoot
        if self.keys_pressed[pygame.K_LSHIFT]:
            x = 1  # rocket/shield/bomb?

    def get_player_ship(self):
        return self.model.player.IMAGE

    """
    Future functions here:
    Collision?
    Enemy tick rate and damage?
    """