import os
import sys
import pygame
from copy import deepcopy
from pygame import Surface

from constants import TILE_SIZE
from sprites.ui.ui_board import board_level


def load_image(name, color_key=None) -> Surface:
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()

    return image


def set_color(image: Surface, delta_color) -> None:
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            color = image.get_at((x, y))
            if color.a:
                image.set_at((x, y), (return_color(color[0], delta_color[0]), return_color(color[1], delta_color[1]),
                                      return_color(color[2], delta_color[2])))


def return_color(color_now, delta_color):
    color = color_now - delta_color
    if color > 255:
        color = 255
    elif color < 0:
        color = 0
    return color


def load_level(filename):
    filename = "data/" + filename
    if not os.path.isfile(filename):
        print(f"Файл с картой '{filename}' не найден")
        sys.exit()

    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def have_way(pos1, pos2, speed, board=deepcopy(board_level.board)):
    if speed > 0:
        if (abs(pos1[0] - pos2[0]) == 1 and pos1[1] - pos2[1] == 0 or abs(pos1[1] - pos2[1]) == 1
                and pos1[0] - pos2[0] == 0):
            board_level[pos2[0]][pos2[1]] = "z"
            board_level[pos2[0]][pos2[1]] = "."

