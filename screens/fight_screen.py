import pygame

from constants import WIDTH, HEIGHT
from extensions import load_image
from sprites.ui.ui_button import Button
from sprites.ui.ui_text import Text


class FightScreen:
    def __init__(self, screen):
        self.screen = screen
        self.fight_screen_sprites = pygame.sprite.Group()

    def draw_fight_screen(self):
        fon = pygame.transform.scale(load_image('fon_fight_screen.png'), (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))

        self.fight_screen_sprites.draw(self.screen)
