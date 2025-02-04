import pygame

from constants import FONT_NAME


class Text(pygame.sprite.Sprite):
    def __init__(self, position, size, *group_sprites, text="", font_position=(0, 0), font_size=40,
                 text_color="#0a0a0a"):
        super().__init__(*group_sprites)
        self.position = position
        self.size = size
        self.image = pygame.Surface(size)
        self.image.set_colorkey(pygame.Color("black"))
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])

        font = pygame.font.Font(FONT_NAME, font_size)
        text = [text] if type(text) is str else text
        for item in text:
            text_one = font.render(item, False, pygame.Color(text_color))
            self.image.blit(text_one, font_position)
            font_position = (font_position[0], font_position[1] + font_size)
