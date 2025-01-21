import pygame
from load_image import Load


class Button_check:
    def __init__(self, screen, event_pos, button_base):
        self.event_pos = event_pos
        self.sprite_base = button_base
        self.screen = screen

    def test(self):
        for i in self.sprite_base:
            if (self.event_pos[0] >= i.rect.x and self.event_pos[1] >= i.rect.y) and (
                    self.event_pos[0] <= i.rect.x + i.rect[-2] and self.event_pos[1] <= i.rect.x + i.rect[-1]):
                # тут потом будет еще и рендер кликов но уже поздно
                # print(self.sprite_base.index(i)) это возврат с помощью id
                return self.sprite_base.index(i)
