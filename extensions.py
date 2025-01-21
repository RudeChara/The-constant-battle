import os
import sys

import pygame
from pygame import Surface


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


def set_color(image: Surface, color_key) -> None:
    color = image.get_colorkey()
    if color is None:
        color = (0, 0, 0)
    image.set_colorkey(((color[0] + color_key[0]) % 256, (color[1] + color_key[1]) % 256,
                        (color[2] + color_key[2]) % 256))
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            color = image.get_at((x, y))
            image.set_at((x, y), ((color[0] + color_key[0]) % 256, (color[1] + color_key[1]) % 256,
                                  (color[2] + color_key[2]) % 256))


def load_level(filename):
    filename = "data/" + filename
    if not os.path.isfile(filename):
        print(f"Файл с картой '{filename}' не найден")
        sys.exit()

    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))
