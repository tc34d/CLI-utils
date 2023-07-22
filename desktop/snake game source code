import pygame
import random
import sys

pygame.init()

width = 640
height = 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

snake_size = 20
snake_speed = 10
snake_x = width / 2
snake_y = height / 2
snake_dx = 0
snake_dy = 0

food_size = 20
food_x = random.randint(0, width - food_size) // food_size * food_size
food_y = random.randint(0, height - food_size) // food_size * food_size

snake_body = []
snake_length = 1

font = pygame.font.Font(None, 36)

start_time = pygame.time.get_ticks()
game_active = True
points = 0

quit_font = pygame.font.Font(None, 48)

def draw_snake():
    for segment in snake_body:
        pygame.draw.rect(window, GREEN, [segment[0], segment[1], snake_size, snake_size])

def display_info():
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    timer_text = font.render("Time: " + str(elapsed_time), True, WHITE)
    points_text = font.render("Points: " + str(points), True, WHITE)
    window.blit(timer_text, (10, 10))
    window.blit(points_text, (10, 50))

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -snake_size
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = snake_size
                snake_dy = 0
            elif event.key == pygame.K_UP:
                snake_dy = -snake_size
                snake_dx = 0
            elif event.key == pygame.K_DOWN:
                snake_dy = snake_size
                snake_dx = 0
            elif event.key == pygame.K_q:
                game_active = False

    if not game_active:
        break

    snake_x += snake_dx
    snake_y += snake_dy

    if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
        game_active = False

    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, width - food_size) // food_size * food_size
        food_y = random.randint(0, height - food_size) // food_size * food_size
        snake_length += 1
        points += 1

    snake_head = [snake_x, snake_y]
    snake_body.append(snake_head)

    if len(snake_body) > snake_length:
        del snake_body[0]

    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_active = False
            break

    window.fill(BLACK)
    pygame.draw.rect(window, RED, [food_x, food_y, food_size, food_size])
    draw_snake()
    display_info()
    pygame.display.update()

    pygame.time.Clock().tick(snake_speed)


total_time = (pygame.time.get_ticks() - start_time) // 1000

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
        elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            game_active = False

pygame.quit()
sys.exit()
