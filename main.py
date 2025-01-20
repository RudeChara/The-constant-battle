import pygame
import os
import sys
from pygame import Surface
from pygame.sprite import Sprite
#Это калл

def button_down(screen, event_pos, sprite):
    if sprite.sprites()[0].rect.x >= event_pos[0] and sprite.sprites()[0].rect.x[1] + 100 >= event_pos[0]:
        print('1222')


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
sprite_group = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
tile_width = tile_height = 50


def get_all_sprites(sprite: pygame.sprite.Sprite, pos, refors=False) -> pygame.sprite.Group:
    # создадим группу, содержащую все спрайты
    x, y = pos
    all_sprites = pygame.sprite.Group()
    # создадим 20 спрайтов
    for _ in range(1):
        # создадим спрайт и добавим его в группу
        sprite: Sprite = pygame.sprite.Sprite(all_sprites)
        # определим его вид
        sprite.image = pygame.image.load("data/button.png")
        sprite.image = pygame.transform.scale(sprite.image, (300, 300))
        sprite.image = pygame.transform.flip(sprite.image, refors, False)
        # и размеры
        sprite.rect = sprite.image.get_rect()
        # разместим спрайт

        sprite.rect.x = x
        sprite.rect.y = y
    return all_sprites


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('fon.jpg'), size)
    screen.blit((fon), (0, 0))
    get_all_sprites(screen, pos=(100, 100))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()


if __name__ == '__main__':
    pygame.display.set_caption('Марио')
    player = None
    ranning = True
    all_sprites = get_all_sprites(screen, pos=(100, 100))
    start_screen()
    while ranning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ranning = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_LEFT:
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(all_sprites.sprites()[0].rect.x)

        screen.fill(pygame.Color('black'))
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
