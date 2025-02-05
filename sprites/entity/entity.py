import pygame
from random import randint

from constants import FONT_NAME, TILE_SIZE
from extensions import load_image, set_color, have_way
from chat import messages
from sprites.ui.ui_button import Button

class Entity(pygame.sprite.Sprite):
    def __init__(self, position, image, name, *group_sprites, hp=1, speed=2, text_color="#fafafa"):
        super().__init__(*group_sprites)
        self.position = position
        self.max_hp = self.hp = hp
        self.speed = speed
        self.name = name
        self.initiative_bonus = 0
        self.skills = {}
        # self.image = Button((1500, 900), (400, 50), image, group_sprites,)
        self.image = pygame.transform.scale(load_image(image), (TILE_SIZE, TILE_SIZE))
        self.rect = pygame.Rect(position[0], position[1], TILE_SIZE, TILE_SIZE)

        font = pygame.font.Font(FONT_NAME, 10)
        text = font.render(name, False, pygame.Color(text_color))
        self.image.blit(text, (5, TILE_SIZE - 10))

    def initiative(self):
        return randint(1, 20) + self.initiative_bonus

    def __str__(self):
        return self.name

    def taking_damage(self, damage, sender):
        messages.append(f"{self.name} получил(а) {damage} от {sender}.")
        self.hp -= damage
        set_color(self.image, (0, -50, -50))
        pygame.time.delay(500)
        set_color(self.image, (0, 50, 50))
        if self.hp <= 0:
            self.death(sender)

    def death(self, sender):
        messages.append(f"{self.name} умер(ла) от рук {sender}.")
        self.kill()
