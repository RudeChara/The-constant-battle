import pygame

from extensions import have_way
from sprites.ui.ui_board import board_level
from sprites.entity.entity import Entity
from sprites.entity.classes.warrior import Warrior


class Zombie(Entity):
    def __init__(self, position, *group_sprites):
        image = "zombie.png"
        name = "зомби"
        super().__init__(position, image, name, *group_sprites)

    def motion(self, screen, entities, position_click_mouse):
        for entity in entities:
            if entity in [Warrior]:
                have_way(screen, board_level.get_cell(self.position), board_level.get_cell(position_click_mouse))

    def damage(self, damage):
        return self.taking_damage(damage, 'игрок')