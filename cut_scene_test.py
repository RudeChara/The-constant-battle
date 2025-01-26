import pygame
import cv2
from extensions import load_video


class Cut_scene:
    def __init__(self, video, screen):
        self.screen = screen
        self.cap = cv2.VideoCapture(load_video(video))

    def video_rendering(self):
        ret, frame = self.cap.read()
        if ret:
            # Конвертируем цветовую модель BGR (OpenCV) в RGB (Pygame)
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = pygame.surfarray.make_surface(frame)
            self.screen.blit(frame, (0, 0))
            pygame.display.flip()
            return True
        else:
            return False


