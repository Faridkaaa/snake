import pygame
import random

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Размер окна
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

# Размер блока змейки и скорость движения
BLOCK_SIZE = 20
SPEED = 20

# Создание окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Змейка")

clock = pygame.time.Clock()

# Отображение текста
font = pygame.font.SysFont(None, 25)

def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(window, GREEN, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

def message(msg, color):
    screen_text = font.render(msg, True, color)
    window.blit(screen_text, [WINDOW_WIDTH / 6, WINDOW_HEIGHT / 3])

def gameLoop():
    game_over = False
    game_close = False

    # Начальные координаты змейки
    x = WINDOW_WIDTH / 2
    y = WINDOW_HEIGHT / 2

    # Изменение координат при движении
    x_change = 0
    y_change = 0

    # Начальная длина змейки
    snake_list = []
    length_of_snake = 1

    # Начальные координаты еды
    food_x = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:

        while game_close == True:
            window.fill(BLACK)
            message("Нажмите Пробел для начала, или Escape для выхода", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0

        # Если змейка выходит за границы экрана
        if x >= WINDOW_WIDTH or x < 0 or y >= WINDOW_HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change
        window.fill(BLACK)
        pygame.draw.rect(window, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)

        pygame.display.update()

        # Если змейка съела еду
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1

        clock.tick(SPEED)

    pygame.quit()
    quit()

gameLoop()
