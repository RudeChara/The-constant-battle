import pygame

from constants import TILE_SIZE
from extensions import load_image


class Wall(pygame.sprite.Sprite):
    def __init__(self, position, image, *group_sprites):
        super().__init__(*group_sprites)
        self.position = position
        self.image = pygame.transform.scale(load_image(image), (TILE_SIZE, TILE_SIZE))
        self.rect = pygame.Rect(position[0], position[1], TILE_SIZE, TILE_SIZE)
