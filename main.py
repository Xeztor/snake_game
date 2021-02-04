from random import randrange
import pygame
from pygame.locals import *
from screen import screen_init
from utils import check_direction, check_if_out_of_boundary
from collections import deque

KEY_ARROWS = [K_UP, K_DOWN, K_LEFT, K_RIGHT]
SNAKE_SIZE = 10

RED = (230, 0, 0)
BLACK = (0, 0, 0)
WHITE = (250, 250, 250)

# Initialise screen
screen = screen_init

# Snake info
tail = deque()
snake_x = 350
snake_y = 350
food_eaten = 0

# Snake heading vars
snake_move_x = 0
snake_move_y = 0

# Food
border = (10, 680, 10)
food = pygame.rect.Rect(randrange(*border), randrange(*border), 10, 10)
pygame.draw.rect(screen, RED, food)

# Set FPS
clock = pygame.time.Clock()

# Game Over Screen
font = pygame.font.Font(None, 72)
dialog_box = font.render('Game Over', 1, RED)
textpos = dialog_box.get_rect()
textpos.centerx, textpos.centery = screen.get_rect().centerx, screen.get_rect().centery

# Event loop
is_dead = False
is_closed = False
while not is_closed:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_closed = True
            break
        elif event.type == pygame.KEYDOWN:
            if event.key in KEY_ARROWS:
                snake_move_x, snake_move_y = check_direction(event, SNAKE_SIZE)
                break
            if event.key == K_SPACE:
                snake_x = 350
                snake_y = 350
                is_dead = False
                food_eaten = 0
                tail.clear()
                break

    snake_x += snake_move_x
    snake_y += snake_move_y
    snake_x, snake_y = check_if_out_of_boundary(snake_x, snake_y)

    screen.fill(BLACK)

    # Check if eat food
    snake = pygame.rect.Rect(snake_x, snake_y, SNAKE_SIZE, SNAKE_SIZE)
    if snake.colliderect(food):
        food_eaten += 1
        food = pygame.rect.Rect(randrange(*border), randrange(*border), SNAKE_SIZE, SNAKE_SIZE)
        tail.append((snake_x + snake_move_x, snake_y + snake_move_y))

    # Check if run over
    if tail and (snake_x, snake_y) in tail:
        screen.blit(dialog_box, textpos)
        pygame.display.update()
        snake_move_x = 0
        snake_move_y = 0
        is_dead = True

    if not is_dead:
        # Background
        pygame.draw.rect(screen, RED, food)
        # Draw Snake
        pygame.draw.rect(screen, WHITE, snake)
        if tail:
            for x, y in tail:
                pygame.draw.rect(screen, WHITE, rect=[x, y, SNAKE_SIZE, SNAKE_SIZE])
            else:
                tail.appendleft((snake_x, snake_y))
                tail.pop()
        # Render
        pygame.display.update()

        clock.tick(12)
