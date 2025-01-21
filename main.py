import sys
import pygame

from constants import WIDTH, HEIGHT, FPS
from extensions import load_level
from start_screen import draw_start_screen


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("The constant battle")

    clock = pygame.time.Clock()

    running = True
    start_screen = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        screen.fill((0, 0, 0))
        if start_screen:
            draw_start_screen(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
