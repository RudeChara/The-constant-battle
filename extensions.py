import os
import sys
import pygame
from pygame import Surface
from constants import WIDTH, HEIGHT
target_alpha = 254

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


# def light_screen(surface, duration=5000):
#     target_alpha = 255  # time
#     step = target_alpha / (duration / 100)  # шаг
#     target_alpha = 0
#     if surface.get_alpha() > target_alpha:
#         current_alpha = surface.get_alpha()
#         current_alpha -= step
#         if current_alpha <= target_alpha:
#             current_alpha = target_alpha
#         surface.set_alpha(current_alpha)

def light_screen(alpha, function_dark, dark_surface):
    global target_alpha
    alpha -= 5
    print('a', target_alpha)
    print('tg', dark_surface.get_alpha())
    function_dark()
    if alpha < target_alpha:
        alpha = 0
    dark_surface.set_alpha(alpha)


def blackout_screen(dark_surface, function_light, function_dark):
    global target_alpha
    alpha = dark_surface.get_alpha()
    fade_duration = 5000
    print(target_alpha)
    fade_step = target_alpha / (fade_duration / 100)
    if alpha < target_alpha and alpha != 0 and alpha != 255:
        alpha += fade_step
        if alpha >= target_alpha:
            alpha = 255
        dark_surface.set_alpha(alpha)
    elif alpha > target_alpha:
        target_alpha = 0
        light_screen(alpha, function_dark, dark_surface)
        alpha = dark_surface.get_alpha()
    else:
        target_alpha = 254
        function_dark()


def load_video(name, color_key=None) -> Surface:
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с видео '{fullname}' не найден")
        sys.exit()
        return ValueError
    else:
        return fullname
