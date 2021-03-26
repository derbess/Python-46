import pygame
import math
import random

pygame.init()

# set window
width = 1000
height = 700
screen = pygame.display.set_mode((width, height))
# set title for the window
pygame.display.set_caption('My first game')
# set icon for the window
# icon = pygame.image.load('icon.png')
# pygame.display.set_icon(icon)
# set font
font = pygame.font.Font('freesansbold.ttf', 32)
# init score_value
score_value = 0

player_img = pygame.image.load('pokeball.png')
player_x = 50
player_y = 420
player_x_change = 0
move_hor = []

enemy_img = []  # pygame.image.load('enemy.png')
enemy_x = []  # 50
enemy_y = []  # 50
enemy_x_change = []  # 0.5
number_of_enemies = 5

for i in range(number_of_enemies):
    enemy_img.append(pygame.image.load('square.png'))
    # enemy_img[i] = pygame.transform.scale(enemy_img, (30, 30))

    enemy_x.append(random.randint(0, width-64))
    enemy_y.append(random.randint(50, 100))
    enemy_x_change.append(0.5)


ball_img = pygame.image.load('pokeball.png')
ball_img = pygame.transform.scale(ball_img, (30, 30))

is_ball = False
ball_x = 0
ball_y = 420

fills = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
cur_fill = 0


def draw(img, x, y):
    screen.blit(img, (x, y))


def draw_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def is_collision(x1, y1, x2, y2):
    if y1 == y2:
        if x2 <= x1 <= x2 + 60:
            return True
        elif x1 <= x2 <= x1 + 14:
            return True
        else:
            return False
    else:
        return False


# Infinity loop for the game
running = True
while running:
    for event in pygame.event.get():
        # event that closes window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_hor.append('left')
            if event.key == pygame.K_RIGHT:
                move_hor.append('right')
            if event.key == pygame.K_SPACE:
                if not is_ball:
                    ball_x = player_x
                    ball_y = player_y
                    is_ball = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_hor.remove('left')
            if event.key == pygame.K_RIGHT:
                move_hor.remove('right')
    # print(move_hor)
    if len(move_hor):
        if move_hor[len(move_hor) - 1] == 'right':
            player_x_change = 1
        if move_hor[len(move_hor) - 1] == 'left':
            player_x_change = -1
    else:
        player_x_change = 0

    # draw background
    # background = pygame.image.load('background.png').convert_alpha()
    # screen.blit(background, (0, 0))
    # screen.fill((189, 129, 9))
    screen.fill(fills[cur_fill])
    # player
    player_x += player_x_change
    player_x = max(0, player_x)
    player_x = min(width - 32, player_x)
    draw(player_img, player_x, player_y)

    for i in range(number_of_enemies):
        enemy_x[i] += enemy_x_change[i]

        if enemy_x[i] < 0:
            enemy_x[i] = 0
            enemy_x_change[i] = 0.5
        if enemy_x[i] > width - 64:
            enemy_x[i] = width - 64
            enemy_x_change[i] = -0.5

        if is_collision(ball_x, ball_y, enemy_x[i], enemy_y[i]):
            score_value += 1

            enemy_x[i] = random.randint(0, width-64)
            enemy_y[i] = random.randint(50, 100)

            is_ball = False

        draw(enemy_img[i], enemy_x[i], enemy_y[i])

    # ball
    if is_ball:
        ball_y -= 1
        draw(ball_img, ball_x, ball_y)
    if ball_y < 0:
        is_ball = False

    # update display
    draw_score(0, 0)
    pygame.display.update()
