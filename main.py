import sys
import pygame
from extensions import blackout_screen
# from extensions import light_screen
from constants import WIDTH, HEIGHT, FPS
from screens.start_screen import StartScreen
from screens.fight_screen import FightScreen
from screens.training_screen import Training_screen
from cut_scene_test import Cut_scene

dark_surface = pygame.Surface((WIDTH, HEIGHT))
dark_surface.fill((0, 0, 0))
dark_surface.set_alpha(1)  # установка прозрачности
current_alpha = 0  # max значение прозрачности
target_alpha = 255
current_alpha_2_sec = 0
current_alpha_3_sec = 0


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("The constant battle")
    screen.fill((255, 255, 255))

    clock = pygame.time.Clock()

    running = True
    scene = "start"
    position_click_mouse = None

    start_screen = StartScreen(screen)
    fight_screen = FightScreen(screen)
    training_screen = Training_screen(screen)
    cut_scene = Cut_scene('video.mp4', screen)

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
            blackout_screen(dark_surface, start_screen.draw_start_screen(position_click_mouse),
                            fight_screen.draw_fight_screen)# первую функцию передавать с скобками а так я  остальную часть кастрировал
        # elif scene == 'edu':
        #     if current_alpha == 255:
        #         light_screen(dark_surface, 1000)
        #         if cut_scene.video_rendering():
        #             cut_scene.video_rendering()
        #         else:
        #             if current_alpha_3_sec == 5.1:
        #                 scene = training_screen.draw_screen(position_click_mouse)
        #                 target_alpha = light_screen(dark_surface)
        #             else:
        #                 current_alpha_3_sec = blackout_screen(dark_surface,
        #                                                       cut_scene.video_rendering())
        #     else:
        #         current_alpha = blackout_screen(dark_surface, start_screen.draw_start_screen(position_click_mouse))
        #
        #
        # elif scene == 'next':  # сделал через колено не понял как фиксить пререзаполнение curent_alfa и ее обнуление
        #     if current_alpha_2_sec == 255:
        #         fight_screen.draw_fight_screen()
        #         target_alpha = light_screen(dark_surface)
        #     else:
        #         current_alpha_2_sec = blackout_screen(dark_surface,
        #                                               training_screen.draw_screen(position_click_mouse))
        screen.blit(dark_surface, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
