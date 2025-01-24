import sys
import pygame

from constants import WIDTH, HEIGHT, FPS
from screens.start_screen import StartScreen
from screens.fight_screen import FightScreen

dark_surface = pygame.Surface((WIDTH, HEIGHT))
dark_surface.fill((0, 0, 0))
dark_surface.set_alpha(0)  # установка прозрачности
target_alpha = 255  # max значение прозрачности
duration = 5000  # time
step = target_alpha / (duration / 100)  # шаг


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
    fight_screen = FightScreen(screen)

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
            scene = start_screen.draw_start_screen(position_click_mouse)
        elif scene == "fight":
            if dark_surface.get_alpha() < target_alpha:
                start_screen.draw_start_screen(position_click_mouse)
                current_alpha = dark_surface.get_alpha()
                current_alpha += step
                if current_alpha > target_alpha:
                    current_alpha = target_alpha
                dark_surface.set_alpha(current_alpha)
            if current_alpha == target_alpha or target_alpha == 0:
                fight_screen.draw_fight_screen()
                target_alpha = 0
                if dark_surface.get_alpha() > target_alpha:
                    current_alpha = dark_surface.get_alpha()
                    current_alpha -= 5
                    if current_alpha <= target_alpha:
                        current_alpha = target_alpha
                    dark_surface.set_alpha(current_alpha)
        screen.blit(dark_surface, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
