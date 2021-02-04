import pygame


def init_screen():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption('Snake')

    return screen


screen_init = init_screen()
