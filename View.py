import pygame
import os


class View:
    def __init__(self):
        self.title_bar_information()

        self._WIDTH = 900
        self._HEIGHT = 800
        self.window = pygame.display.set_mode(
            (self._WIDTH, self._HEIGHT)  # notice the double parenthesis
        )

        self.RED = (204, 0, 0)
        self.GREEN = (0, 230, 0)
        self.WHITE = (255, 255, 255)
        self.LAVANDER = (230, 230, 255)
        self.GREY = (54, 85, 112)
        self.LIGHT_GREY = (84, 115, 142)

        self.display_queue = []
        self.display_information = {}
        self.PLAY_AREA_WIDTH = 600
        self.PLAY_AREA_HEIGHT = 800
        self.viewable_boxes = False
        self.title_font = pygame.font.Font(
            os.path.join("fonts", "FFFFORWA.TTF"), size=20
        )
        self.data_font = pygame.font.Font(
            os.path.join("fonts", "FFFFORWA.TTF"), size=12
        )

    def title_bar_information(self):
        pygame.display.set_icon(
            pygame.image.load(os.path.join("assets", "icon 32.png"))
        )
        pygame.display.set_caption("Shmup")

    def display_elements(self):
        self.window.fill(
            "black"
        )  # fill the screen with a color to wipe away anything from last frame
        self.display_all_sprites()
        self.border_setup_and_display()
        self.draw_information_panel()
        pygame.display.flip()

    def visible_boxes(self):
        self.viewable_boxes = True

    def invisible_boxes(self):
        self.viewable_boxes = False

    def add_to_display_queue(self, payload):
        self.display_queue.extend(payload)

    def display_all_sprites(self):
        for item in self.display_queue:
            self.window.blit(item.image, item.rect)

            if self.viewable_boxes:
                color = (0, 0, 0)
                if item.category == "hero":
                    color = (0, 0, 255)  # blue
                elif item.category == "enemy":
                    color = (255, 0, 0)  # red
                elif item.category == "bullet":
                    color = (160, 32, 240)  # purple

                pygame.draw.rect(self.window, color, item.rect, width=2)

        self.display_queue.clear()

    def border_setup_and_display(self):
        self.BORDER_ASSET = pygame.image.load(
            os.path.join("assets", "border 600x800.png")
        )
        self.BORDER = pygame.transform.scale(
            self.BORDER_ASSET, (self.PLAY_AREA_WIDTH, self.PLAY_AREA_HEIGHT)
        )
        self.window.blit(self.BORDER, (0, 0))  # Border should always be at the end

    def draw_information_panel(self):
        pygame.draw.rect(self.window, self.GREY, [600, 0, 300, 800])

        self.display_game_title()

        self.display_player_health_bar(
            self.display_information["current_player_hp"],
            self.display_information["total_player_hp"],
        )

        self.display_game_level("Stage 1: Sector 1")
        self.display_upgrades()

    def display_game_title(self):
        game_name = self.data_font.render("Rouge Shmup X", True, self.WHITE)
        self.window.blit(game_name, (610, 10))

    def display_player_health_bar(self, current_player_hp, total_player_hp):
        health_bar_space = 280
        actual_health_space = (current_player_hp / total_player_hp) * health_bar_space
        red_health_bar = pygame.Rect(610, 35, health_bar_space, 10)  # does not change
        green_health_bar = pygame.Rect(610, 35, actual_health_space, 10)  # changes

        pygame.draw.rect(self.window, self.RED, red_health_bar)
        pygame.draw.rect(self.window, self.GREEN, green_health_bar)
        health_text = (
            str(self.display_information["current_player_hp"])
            + "/"
            + str(self.display_information["total_player_hp"])
        )
        health = self.data_font.render(health_text, True, self.WHITE)
        self.window.blit(health, (610, 55))

    def display_game_level(self, level: str):
        level_label = self.data_font.render(level, True, self.WHITE)
        self.window.blit(level_label, (610, 150))

    def display_upgrades(self):
        assest = [
            "attack core 256.png",
            "explosive core 256.png",
            "multi core 256.png",
            "spread core 256.png",
            "twin core 256.png",
            "unstable core 256.png",
        ]
        x = 600
        y = 515
        gap = 5
        upgrade_width = 150
        upgrade_height_spacing = 95

        self.place_upgrade(x, y, "Thing thing", "unknown core 256.png", 0)

        self.place_upgrade(
            x, y + upgrade_height_spacing, "Thing thing", "unknown core 256.png", 0
        )
        self.place_upgrade(
            x + 145,
            y + upgrade_height_spacing,
            "Thing thing",
            "unknown core 256.png",
            0,
        )

        self.place_upgrade(
            x,
            y + (upgrade_height_spacing * 2),
            "Attack level",
            "unknown core 256.png",
            900,
        )
        self.place_upgrade(
            x + 145,
            y + (upgrade_height_spacing * 2),
            "Secondary type",
            "unknown core 256.png",
            0,
        )

    def place_upgrade(self, x: int, y: int, type: str, asset_name: str, count: int):
        upgrade_border = pygame.Rect(x, y, 150, 90)
        pygame.draw.rect(self.window, self.LIGHT_GREY, upgrade_border, width=4)

        label = self.data_font.render(type, True, self.WHITE)
        self.window.blit(label, (x + 15, y + 10))

        upgrade_img = pygame.image.load(os.path.join("assets", asset_name))
        upgrade = pygame.transform.scale(upgrade_img, (64, 64))
        self.window.blit(upgrade, (x + 20, y + 25))

        pick_up_count = self.data_font.render("x  " + str(count), True, self.WHITE)
        self.window.blit(pick_up_count, (x + 90, y + 50))
