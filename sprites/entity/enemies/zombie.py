import pygame

from sprites.entity.entity import Entity


class Zombie(Entity):
    def __init__(self, position, *group_sprites):
        image = "zombie.png"
        name = "зомби"
        super().__init__(position, image, name, *group_sprites)

