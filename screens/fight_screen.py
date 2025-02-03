import pygame

from constants import WIDTH, HEIGHT, TILE_SIZE
from extensions import load_image, load_level
from sprites.ui.ui_button import Button
from sprites.ui.ui_text import Text
from sprites.ui.ui_board import board_level
from sprites.objects.wall import Wall
from sprites.entity.classes.warrior import Warrior
from sprites.entity.enemies.zombie import Zombie


class FightScreen:
    def __init__(self, screen, type_of_levels, level):
        self.screen = screen
        self.fight_screen_sprites = pygame.sprite.Group()
        self.entities = []
        self.motion = 0
        create_level(board_level.left, board_level.top, load_level(f"levels/{type_of_levels}-{level}.txt"),
                     self.entities, self.fight_screen_sprites)
        self.end_motion_button = Button((1700, 900), (100, 50), "fight.png", self.fight_screen_sprites,
                                        text="Закончить ход")
        self.entities = sorted(self.entities, key=lambda x: (x.initiative(), str(x)))

    def draw_fight_screen(self):
        fon = pygame.transform.scale(load_image("fon_fight_screen.png"), (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))

        board_level.render(self.screen)
        self.fight_screen_sprites.draw(self.screen)


def create_level(left, top, map_level, entities, group_sprites):
    for i in range(len(map_level)):
        for j in range(len(map_level[0])):
            position = (j * TILE_SIZE + left, i * TILE_SIZE + top)
            if map_level[i][j] == "#":
                Wall(position, "fon_fight_screen.png", group_sprites)
            elif map_level[i][j] == "1":
                name_character = "Боец"
                entities.append(Warrior(position, "fight.png", name_character, group_sprites))
            elif map_level[i][j] == "z":
                entities.append(Zombie(position, group_sprites))
