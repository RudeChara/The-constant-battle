import sys
import pygame
from extensions import blackout_screen, light_screen, load_level
from constants import WIDTH, HEIGHT, FPS
from screens.start_screen import StartScreen
from screens.fight_screen import FightScreen

dark_surface = pygame.Surface((WIDTH, HEIGHT))
dark_surface.fill((0, 0, 0))
dark_surface.set_alpha(0)  # установка прозрачности
current_alpha = 0  # max значение прозрачности


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
    fight_screen = None

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
            if fight_screen is None:
                fight_screen = FightScreen(screen, 1, 1)
            if current_alpha == 255:
                fight_screen.draw_fight_screen()
                target_alpha = light_screen(dark_surface)
            else:
                current_alpha = blackout_screen(dark_surface, start_screen.draw_start_screen(position_click_mouse))

        screen.blit(dark_surface, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
