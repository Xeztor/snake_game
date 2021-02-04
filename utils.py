import pygame
from screen import screen_init


def check_direction(key_event, snake_size):
    snake_move_x = 0
    snake_move_y = 0
    if key_event.key == pygame.K_LEFT:
        snake_move_x = -snake_size
        snake_move_y = 0
    elif key_event.key == pygame.K_RIGHT:
        snake_move_x = snake_size
        snake_move_y = 0
    elif key_event.key == pygame.K_UP:
        snake_move_x = 0
        snake_move_y = -snake_size
    elif key_event.key == pygame.K_DOWN:
        snake_move_x = 0
        snake_move_y = snake_size

    return snake_move_x, snake_move_y


def check_if_out_of_boundary(x, y):
    screen_x_border, screen_y_border = screen_init.get_size()
    if x < 0:
        x = screen_x_border
    elif x > screen_x_border:
        x = 0
    elif y < 0:
        y = screen_y_border
    elif y > screen_y_border:
        y = 0

    return x, y
