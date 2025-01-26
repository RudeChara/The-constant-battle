import pygame

from constants import WIDTH, HEIGHT, TILE_SIZE
from extensions import load_image
from sprites.ui.ui_button import Button
from sprites.ui.ui_text import Text


class Training_screen:
    def __init__(self, screen):
        self.screen = screen
        self.edu_screen_sprites = pygame.sprite.Group()
        # self.name_game = Text((50, 50), (2000, 100), self.edu_screen_sprites,
        #                       text="Обучение", font_size=100, text_color='#ffffff')
        self.button_next = Button((1700, 500), (200, 200), "right_arrow.png", self.edu_screen_sprites, text="next",
                                  text_color='#ffffff')

    def draw_fight_screen(self, position_click_mouse):
        fon = pygame.transform.scale(load_image('fon_fight_screen.png'), (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))

        self.edu_screen_sprites.draw(self.screen)
        self.edu_screen_sprites.update(position_click_mouse)
        if self.button_next.need_change == "already":
            return 'next'
        else:
            return 'edu'
