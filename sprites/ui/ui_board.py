import pygame

from constants import WIDTH, HEIGHT, TILE_SIZE


class Board:
    def __init__(self, width_b, height_b, level_map):
        self.width = width_b
        self.height = height_b
        self.board = [[item for item in line] for line in level_map]
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
        return self.left + cell_coord[0] * TILE_SIZE, self.top + cell_coord[1] * TILE_SIZE

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is not None:
            self.on_click(cell)


board_level = Board(15, 15, [[[0] for _ in range(15)] for _ in range(15)])
