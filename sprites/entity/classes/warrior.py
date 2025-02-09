import pygame

from sprites.entity.entity import Entity


class Warrior(Entity):
    def damage(self, dmg):
        self.taking_damage(dmg, 'зомби')
