import pygame

from extensions import load_image, set_color
from constants import FONT_NAME


class Button(pygame.sprite.Sprite):
    def __init__(self, position, size, image, *group_sprites, text="", font_position=(0, 0), font_size=40):
        super().__init__(*group_sprites)
        self.position = position
        self.size = size
        self.image = pygame.transform.scale(load_image(image), size)
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])

        font = pygame.font.Font(FONT_NAME, font_size)
        text = font.render(text, False, pygame.Color("#0a0a0a"))
        self.image.blit(text, font_position)

    def clicked(self, mouse_position):
        if self.rect.collidepoint(mouse_position):
            return True
        return False

    def update(self, mouse_position):
        if mouse_position is not None:
            if self.clicked(mouse_position):
                set_color(self.image, pygame.Color("red"))
            else:
                set_color(self.image, pygame.Color("blue"))
