import pygame
from pygame import Surface

from constants import WIDTH, HEIGHT
from extensions import load_image
from sprites.ui.ui_text import Text


def draw_start_screen(screen: Surface) -> None:
    fon = pygame.transform.scale(load_image('fon_start_screen.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    start_screen_sprites = pygame.sprite.Group()
    name_game = Text((50, 50), (2000, 100), start_screen_sprites, text="The Constant Battle", font_size=100)
    start_screen_sprites.draw(screen)
