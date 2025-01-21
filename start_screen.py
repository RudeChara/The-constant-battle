import pygame
from pygame import Surface

from constants import WIDTH, HEIGHT, FONT_NAME
from extensions import load_image


def draw_start_screen(screen: Surface) -> None:
    fon = pygame.transform.scale(load_image('fon_start_screen.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    name_game = "The Constant Battle"
    font = pygame.font.Font(FONT_NAME, 100)
    text = font.render(name_game, False, pygame.Color("#0a0a0a"))
    screen.blit(text, (50, 50))
