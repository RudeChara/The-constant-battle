import sys
import pygame

from constants import WIDTH, HEIGHT, FPS
from extensions import load_level


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("The constant battle")

    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

