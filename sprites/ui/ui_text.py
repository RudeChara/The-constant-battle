import pygame

from extensions import load_image, set_color
from constants import FONT_NAME


class Text(pygame.sprite.Sprite):
    def __init__(self, position, size, text="", font_position=(0, 0), font_size=40, text_color="#0a0a0a", *group_sprites):
        super().__init__(*group_sprites)
        self.position = position
        self.size = size
        self.image = pygame.Surface(size)
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])

        font = pygame.font.Font(FONT_NAME, font_size)
        text = font.render(text, False, pygame.Color(text_color))
        self.image.blit(text, font_position)
