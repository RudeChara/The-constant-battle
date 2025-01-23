import sys
import pygame

from constants import WIDTH, HEIGHT, FPS
from start_screen import draw_start_screen
from sprites.ui.ui_button import Button
from sprites.ui.ui_text import Text


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("The constant battle")

    clock = pygame.time.Clock()

    all_buttons = pygame.sprite.Group()
    button = Button((10, 900), (200, 100), "fight.png", all_buttons, text="Play")

    running = True
    start_screen = True
    position_click_mouse = None

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
        if start_screen:
            draw_start_screen(screen)
        all_buttons.draw(screen)
        all_buttons.update(position_click_mouse)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
