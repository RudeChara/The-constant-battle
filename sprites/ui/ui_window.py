import pygame

from constants import FONT_NAME


class Window(pygame.sprite.Sprite):
    def __init__(self, position, size, *group_sprites, text="", color1="#f5c37d", color2="#ffb366",
                 text_color="#0a0a0a"):
        super().__init__(*group_sprites)
        self.position = position
        self.size = size
        self.image = pygame.Surface(size)
        self.image.fill(color2)
        self.image.fill(color1, pygame.Rect(3, 3, size[0] - 6, size[1] - 6))
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])

        font = pygame.font.Font(FONT_NAME, 30)
        text = font.render(text, False, pygame.Color(text_color))
        self.image.blit(text, (5, 5))
