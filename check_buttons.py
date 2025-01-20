import pygame
from load_image import Load


class Button_check:
    def __init__(self, screen, event_pos, button_base):
        self.event_pos = event_pos
        self.sprite_base = button_base
        self.screen = screen

    def test(self):
        for i in self.sprite_base:
            if self.event_pos >= (i.rect.x, i.rect.y) and self.event_pos <= (i.rect.x + i.rect[-2], i.rect.y + i.rect[-1]) :
                #тут потом будет еще и рендер кликов но уже поздно
                return 'test 01 все верно но нужен норм возврат'
