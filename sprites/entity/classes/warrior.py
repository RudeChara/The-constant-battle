import pygame

from sprites.entity.entity import Entity


class Warrior(Entity):
    def damege(self, dmg):
        self.taking_damage(dmg, 'зомби')
