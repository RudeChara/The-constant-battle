import pygame

from constants import FONT_NAME, TILE_SIZE
from extensions import load_image, set_color


class Entity(pygame.sprite.Sprite):
    def __init__(self, position, image, name, *group_sprites, hp=1, text_color="#fafafa"):
        super().__init__(*group_sprites)
        self.position = position
        self.hp = hp
        self.image = pygame.transform.scale(load_image(image), (TILE_SIZE, TILE_SIZE))
        self.rect = pygame.Rect(position[0], position[1], TILE_SIZE, TILE_SIZE)

        font = pygame.font.Font(FONT_NAME, 10)
        text = font.render(name, False, pygame.Color(text_color))
        self.image.blit(text, (5, TILE_SIZE - 10))
