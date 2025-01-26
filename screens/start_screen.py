import pygame

from constants import WIDTH, HEIGHT
from extensions import load_image
from sprites.ui.ui_button import Button
from sprites.ui.ui_text import Text


class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.start_screen_sprites = pygame.sprite.Group()
        self.name_game = Text((50, 50), (2000, 100), self.start_screen_sprites,
                              text="The Constant Battle", font_size=100)
        self.button_play = Button((10, 900), (200, 100), "fight.png", self.start_screen_sprites, text="Play")
        self.button_edu = Button((300, 900), (210, 200), "book.png", self.start_screen_sprites, text="Обучение")
    def draw_start_screen(self, position_click_mouse):
        fon = pygame.transform.scale(load_image('fon_start_screen.jpg'), (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))

        self.start_screen_sprites.draw(self.screen)
        self.start_screen_sprites.update(position_click_mouse)
        if self.button_play.need_change == "already":
            return "fight"
        else:
            if self.button_edu.need_change == "already":
                return "edu"
            else:
                return "start"

