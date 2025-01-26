import sys
import pygame
from extensions import blackout_screen
from extensions import light_screen
from constants import WIDTH, HEIGHT, FPS
from screens.start_screen import StartScreen
from screens.fight_screen import FightScreen
from screens.training_screen import Training_screen

dark_surface = pygame.Surface((WIDTH, HEIGHT))
dark_surface.fill((0, 0, 0))
dark_surface.set_alpha(0)  # установка прозрачности
current_alpha = 0  # max значение прозрачности
target_alpha = 255
current_alpha_2_sec = 0
x = 0
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
    training_screen = Training_screen(screen)

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
            if current_alpha == 255:
                fight_screen.draw_fight_screen()
                target_alpha = light_screen(dark_surface)
            else:
                current_alpha = blackout_screen(dark_surface, start_screen.draw_start_screen(position_click_mouse))
        elif scene == 'edu':
            if current_alpha == 255:
                scene = training_screen.draw_fight_screen(position_click_mouse)
                light_screen(dark_surface)
            else:
                current_alpha = blackout_screen(dark_surface, start_screen.draw_start_screen(position_click_mouse))
        elif scene == 'next':#сделал через колено не понял как фиксить пререзаполнение curent_alfa и ее обнуление
            if current_alpha_2_sec == 255 or x == 1:
                fight_screen.draw_fight_screen()
                target_alpha = light_screen(dark_surface)
            else:
                current_alpha_2_sec = blackout_screen(dark_surface, training_screen.draw_fight_screen(position_click_mouse))
        screen.blit(dark_surface, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
