import pygame
import os


class Load:#Так проще проверять на наличие
        def load_image(self, name, color_key=None):
            fullname = os.path.join('../data', name)
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
