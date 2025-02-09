import cv2
import pygame

from constants import WIDTH, HEIGHT, TILE_SIZE
from extensions import load_image
from sprites.ui.ui_button import Button
from sprites.ui.ui_text import Text

class Training_screen:
    def __init__(self, screen):
        self.screen = screen
        self.cap = cv2.VideoCapture('edu_snd.mp3')
        self.edu_screen_sprites = pygame.sprite.Group()
        # self.name_game = Text((50, 50), (2000, 100), self.edu_screen_sprites,
        #                       text="Обучение", font_size=100, text_color='#ffffff')

    def draw_screen(self, position_click_mouse):
        fon = pygame.transform.scale(load_image('fon_fight_screen.png'), (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))

        self.edu_screen_sprites.draw(self.screen)
        self.edu_screen_sprites.update(position_click_mouse)
        ret, frame = self.cap.read()
        if ret:
            # Конвертируем цветовую модель BGR (OpenCV) в RGB (Pygame)
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = pygame.surfarray.make_surface(frame)
            self.screen.blit(frame, (500, 0))
            return 'edu'
        else:
            return 'fight'