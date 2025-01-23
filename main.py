import sys
import pygame

from constants import WIDTH, HEIGHT, FPS
from start_screen import StartScreen


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("The constant battle")

    clock = pygame.time.Clock()

    running = True
    scene = "start"
    position_click_mouse = None

    start_screen = StartScreen(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position_click_mouse = event.pos
        screen.fill((0, 0, 0))
        if scene == "start":
            start_screen.draw_start_screen(position_click_mouse)
        elif scene == "fight":
            pass
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
