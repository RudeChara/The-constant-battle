import pygame

from constants import WIDTH, HEIGHT
from extensions import load_image
from sprites.ui.ui_button import Button
from sprites.ui.ui_text import Text
from sprites.ui.ui_window import Window
from sprites.entity.classes.warrior import Warrior


class CreateCharacter:
    def __init__(self, screen):
        self.screen = screen
        self.create_character_screen_sprites = pygame.sprite.Group()
        self.classes = [Warrior]
        self.button_class = Button((10, 100), (200, 100), "fight.png", self.create_character_screen_sprites,
                                   text="Класс")
        self.button_end = Button((10, 500), (200, 100), "fight.png", self.create_character_screen_sprites,
                                 text="Завершить")
        self.window_class = Window((250, 20), (400, 900), self.create_character_screen_sprites)

    def draw_start_screen(self, position_click_mouse):
        fon = pygame.transform.scale(load_image('fon_create_character_screen.jpg'), (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))

        self.create_character_screen_sprites.draw(self.screen)
        self.create_character_screen_sprites.update(position_click_mouse)
        if self.button_class.need_change == "already":
            self.window_class.draw(self.screen)
        if self.button_end.need_change == "already":
            return "fight"
        return "create_character"
