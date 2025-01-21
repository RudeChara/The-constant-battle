import pygame
from check_buttons import Button_check
import sys
from pygame import Surface
from pygame.sprite import Sprite
from load_image import Load


# Это калл

def button_down(screen, event_pos, sprite):
    if sprite.sprites()[0].rect.x >= event_pos[0] and sprite.sprites()[0].rect.x[1] + 100 >= event_pos[0]:
        print('1222')


# def load_image(name, color_key=None):
#     fullname = os.path.join('data', name)
#     try:
#         image = pygame.image.load(fullname)
#     except pygame.error as message:
#         print('Не удаётся загрузить:', name)
#         raise SystemExit(message)
#     image = image.convert_alpha()
#     if color_key is not None:
#         if color_key is -1:
#             color_key = image.get_at((0, 0))
#         image.set_colorkey(color_key)
#     return image


pygame.init()
size = width, height = 800, 800
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((800, 800))
sprite_group = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
tile_width = tile_height = 50

# tile_image = {'wall': load_image('box.png'),
#               'empty': load_image('grass.png')}
# player_image = load_image('mar.png')

tile_width = tile_height = 50


def retranslator(level):
    pass


def get_all_sprites(sprite: pygame.sprite.Sprite, posi, refors=False) -> pygame.sprite.Group:
    # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()
    # Без колена не работал
    for i in range(2):
        pos = posi[i]
        x, y = pos
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
    fon = pygame.transform.scale(Load.load_image([], name='fon.jpg'), size)  # Я не вспомнил как избавиться от self
    screen.blit((fon), (0, 0))
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
    all_sprites = get_all_sprites(screen, [(100, 100), (400, 400)])

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
                print(Button_check(screen, event.pos, all_sprites.sprites()).test())
                if type(Button_check(screen, event.pos, all_sprites.sprites()).test()) == int:
                    if Button_check(screen, event.pos, all_sprites.sprites()).test() == 1:
                        start_screen()
                    all_sprites.sprites()[Button_check(screen, event.pos, all_sprites.sprites()).test()].kill()
                # я тут вроде настрроил поставил 2 кнопки и в группу их одну запихал

        screen.fill(pygame.Color('black'))
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
