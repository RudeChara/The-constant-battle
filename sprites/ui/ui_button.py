import pygame

from constants import FONT_NAME
from extensions import load_image, set_color


class Button(pygame.sprite.Sprite):
    def __init__(self, position, size, image, *group_sprites, group_buttons=None, text="", font_position=(0, 0),
                 font_size=40, text_color="#0a0a0a", window_button_group=None):
        super().__init__(*group_sprites)
        self.position = position
        self.size = size
        self.image = pygame.transform.scale(load_image(image), size)
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.need_change = "no"
        self.group_buttons = group_buttons
        self.window_button_group = window_button_group

        font = pygame.font.Font(FONT_NAME, font_size)
        text = font.render(text, False, pygame.Color(text_color))
        self.image.blit(text, font_position)

    def clicked(self, mouse_position_click):
        if self.rect.collidepoint(mouse_position_click):
            if self.need_change == "no":
                self.need_change = "yes"
                self.set_color()
            return True
        if self.group_buttons is None:
            return False
        else:
            for item in self.group_buttons:
                if item.rect.collidepoint(mouse_position_click):
                    return None
        return False

    def update(self, mouse_position_click, mouse_position=None):
        if mouse_position_click is not None:
            if self.clicked(mouse_position_click):
                if self.need_change == "yes":
                    self.need_change = "already"
                if self.window_button_group is not None:
                    self.window_button_group[0].draw(self.window_button_group[1])
            elif self.clicked(mouse_position_click) is None:
                pass
            else:
                if self.need_change == "already":
                    self.set_color(1)
                    self.need_change = "no"

    def add_group_button(self, buttons):
        self.group_buttons = buttons

    def set_color(self, ratio=-1):
        set_color(self.image, (20 * ratio, 20 * ratio, 20 * ratio))
