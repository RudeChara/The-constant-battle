import pygame

from constants import WIDTH, HEIGHT, TILE_SIZE
from extensions import load_image
from sprites.ui.ui_button import Button
from sprites.ui.ui_text import Text


class Board:
    def __init__(self, width_b, height_b):
        self.width = width_b
        self.height = height_b
        self.board = [["-"] * self.width for _ in range(self.height)]
        self.left = (WIDTH - self.width * TILE_SIZE) // 6
        self.top = (HEIGHT - self.height * TILE_SIZE) // 2
        self.cell_size = TILE_SIZE
        self.transparent = pygame.Surface((self.width * self.cell_size, self.height * self.cell_size))
        self.transparent.set_alpha(150)
        self.transparent.fill(pygame.Color("#0a0a0a"))

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen_b):
        screen_b.blit(self.transparent, (self.left, self.top))
        for i in range(self.left, self.width * self.cell_size + self.left, self.cell_size):
            for j in range(self.top, self.height * self.cell_size + self.top, self.cell_size):
                pygame.draw.rect(screen_b, pygame.Color("#f5f5f5"), (i, j, self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        x, y = None, None
        for i in range(self.width):
            if i * self.cell_size + self.left <= mouse_pos[0] < (i + 1) * self.cell_size + self.left:
                x = i
                break
        for i in range(self.height):
            if i * self.cell_size + self.top <= mouse_pos[1] < (i + 1) * self.cell_size + self.top:
                y = i
                break
        if x is None or y is None:
            return None
        return x, y

    def on_click(self, cell_coord):
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is not None:
            self.on_click(cell)


class FightScreen:
    def __init__(self, screen):
        self.screen = screen
        self.fight_screen_sprites = pygame.sprite.Group()
        self.board = Board(15, 15)

    def draw_fight_screen(self):
        fon = pygame.transform.scale(load_image('fon_fight_screen.png'), (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))

        self.board.render(self.screen)
        self.fight_screen_sprites.draw(self.screen)
