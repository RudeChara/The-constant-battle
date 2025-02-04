import pygame

from constants import WIDTH, HEIGHT
from extensions import load_image
from sprites.ui.ui_button import Button
from sprites.ui.ui_text import Text
from sprites.ui.ui_window import Window
from sprites.entity.classes.warrior import Warrior
from sprites.entity.skills.uniqueness import accurate, fast, master_of_armor, strong


uniqueness_roster = [accurate, fast, master_of_armor, strong]


class CreateCharacter:
    def __init__(self, screen):
        self.screen = screen
        self.create_character_screen_sprites = pygame.sprite.Group()
        self.classes = [Warrior]
        self.button_class = Button((10, 100), (200, 100), "fight.png", self.create_character_screen_sprites,
                                   text="Класс")
        self.window_class = pygame.sprite.Group()
        Window((250, 20), (400, 900), self.window_class, text="Классы")

        button_uniqueness = Button((10, 250), (200, 100), "fight.png", self.create_character_screen_sprites,
                                        text="Черты")
        self.window_uniqueness = pygame.sprite.Group()
        self.window2 = Window((250, 20), (550, 900), self.window_uniqueness, text="Черты")
        self.buttons_uniqueness = [button_uniqueness]
        for i in range(4):
            window_button_sprites = pygame.sprite.Group()
            window_button = Window((250, 700), (550, 220), window_button_sprites, text=f"{uniqueness_roster[i].name()}")
            Text((window_button.rect.x + 10, window_button.rect.y + 50), (550, 150), window_button_sprites,
                 text=uniqueness_roster[i].information(), font_size=20)
            uniqueness = Button((self.window2.rect.x + 10, self.window2.rect.y + 100 * i + 50), (500, 50),
                                "fight.png", self.window_uniqueness, group_buttons=[button_uniqueness],
                                text=f"{uniqueness_roster[i].name()}", window_button_group=(window_button_sprites, self.screen))
            self.buttons_uniqueness.append(uniqueness)
        button_uniqueness.add_group_button(self.buttons_uniqueness)

        self.button_end = Button((10, 500), (200, 100), "fight.png", self.create_character_screen_sprites,
                                 text="Завершить")

    def draw_screen(self, position_click_mouse):
        fon = pygame.transform.scale(load_image('fon_create_character_screen.jpg'), (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))

        self.create_character_screen_sprites.draw(self.screen)
        self.create_character_screen_sprites.update(position_click_mouse)
        if self.button_class.need_change == "already":
            self.window_class.draw(self.screen)
        elif self.buttons_uniqueness[0].need_change == "already":
            self.window_uniqueness.draw(self.screen)
            self.window_uniqueness.update(position_click_mouse)

        if self.button_end.need_change == "already":
            with open("./characters.txt", mode="w", encoding="utf-8") as file:
                for i in range(4):
                    if self.buttons_uniqueness[i + 1].need_change == "already":
                        file.write(str(uniqueness_roster[i]))
            return "fight"
        return "create_character"
