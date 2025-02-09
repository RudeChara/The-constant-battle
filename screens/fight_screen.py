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
        self.type_of_levels = type_of_levels
        self.level = level

        self.fight_screen_sprites = pygame.sprite.Group()
        self.entities = []
        board_level.__init__(15, 15, load_level(f"levels/{type_of_levels}-{level}.txt"))
        create_level(board_level.left, board_level.top, load_level(f"levels/{self.type_of_levels}-{self.level}.txt"),
                     self.entities, self.fight_screen_sprites)
        self.motion = -1
        self.end_motion_button = Button((1500, 700), (400, 400), "fight.png", self.fight_screen_sprites,
                                        text="Закончить ход")
        self.end_motion = True
        self.texts_sprites = pygame.sprite.Group()
        self.initiatives = sorted(self.entities, key=lambda x: (x.initiative(), str(x)))
        self.start_motion()
        self.spell = 0
        self.x = 1
        self.spells = [('Кусок пицы', 1), ('Гантеля', 2), ('Военкомат', 100)]

    def draw_fight_screen(self, position_click_mouse):
        fon = pygame.transform.scale(load_image("fon_fight_screen.png"), (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))

        self.entities = []
        # create_level(board_level.left, board_level.top, load_level(f"levels/{self.type_of_levels}-{self.level}.txt"),
        #              self.entities, self.fight_screen_sprites)
        self.entities = self.initiatives

        board_level.render(self.screen)
        self.fight_screen_sprites.draw(self.screen)
        self.fight_screen_sprites.update(position_click_mouse)
        '''
        if self.entities[self.motion] in [Warrior]:
            print(True)
        else:
            self.entities[self.motion].motion(self.screen, self.entities, position_click_mouse)
            entities[0].damage(1)
        '''
        if self.end_motion_button.need_change == "already" and self.end_motion:
            self.start_motion()
            self.end_motion = False
        elif self.end_motion_button.need_change == "no":
            self.end_motion = True
        self.texts_sprites.draw(self.screen)
        return "fight"

    def start_motion(self):
        self.texts_sprites = pygame.sprite.Group()
        self.motion += 1
        self.motion = 0 if len(self.entities) == self.motion else self.motion
        for i in range(len(self.entities)):
            if self.motion != i:
                Text((1500, 50 + i * 60), (550, 150), self.texts_sprites, text=[self.entities[i].name],
                     font_size=30, text_color="#bed2f7")
            else:
                Text((1500, 50 + i * 60), (550, 150), self.texts_sprites, text=[self.entities[i].name],
                     font_size=30, text_color="#6495ed")
                self.now_name = self.entities[i].name
                # if self.entities[i].name == 'зомби':
                #     self.entities[-1].damege(10)

    def button_up(self):
        self.spell += 1
        if self.spell > 2:
            self.spell = 0
        print(self.spell)

    def button_down(self):
        self.spell -= 1
        if self.spell < 0:
            self.spell = 2
        print(self.spell)

    def pkm(self, pos, id=0):

        # if len(self.entities) == 1:
        #     Text((500, 500), (300, 300), self.texts_sprites, text="Победа",
        #          font_size=30, text_color="#6495ed")
        # else:
        self.x = 1
        self.entities[id].damage(self.spells[self.spell][1])
        self.entities.remove(self.entities[id])
        print(self.entities)
        self.start_motion()



def create_level(left, top, map_level, entities, group_sprites):
    for i in range(len(map_level)):
        for j in range(len(map_level[0])):
            position = (j * TILE_SIZE + left, i * TILE_SIZE + top)
            if map_level[i][j] == "#":
                Wall(position, "fon_fight_screen.png", group_sprites)
            elif map_level[i][j] == "p":
                name_character = "игрок"
                entities.append(Warrior(position, "fight.png", name_character, group_sprites, hp=100))
            elif map_level[i][j] == "z":
                entities.append(Zombie(position, group_sprites))
