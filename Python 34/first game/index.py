import pygame
import random
pygame.init()

WIDTH = 500
HEIGHT = 300
COLOR = (134, 117, 209)

square_img = []
square_x = []
square_y = []
square_dir = []
square_cnt = 4

for i in range(square_cnt):
    square_img.append(pygame.image.load('square.png'))
    square_img[i] = pygame.transform.scale(square_img[i], (30, 30))
    square_x.append(random.randint(0, WIDTH-30))
    square_y.append(random.randint(0, HEIGHT-30))
    square_dir.append(0.1)

# square_img = pygame.image.load('square.png')
# square_img = pygame.transform.scale(square_img, (30, 30))
# square_x = 0
# square_y = 0
# square_dir = 'right'

player_img = pygame.image.load('pokeball.png')
player_img = pygame.transform.scale(player_img, (32, 32))
player_width = 32
player_heigh = 32
player_x = 50
player_y = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def draw(img, x, y):
    screen.blit(img, (x, y))


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 40
            if event.key == pygame.K_RIGHT:
                player_x += 40
            if event.key == pygame.K_UP:
                player_y -= 40
            if event.key == pygame.K_DOWN:
                player_y += 40

    for i in range(square_cnt):
        square_x[i] += square_dir[i]
        if square_x[i] > WIDTH - 30:
            square_x[i] = WIDTH - 30
            square_dir[i] = -0.1
        if square_x[i] < 0:
            square_x[i] = 0
            square_dir[i] = 0.1


    # if square_dir == 'left':
    #     square_x -= 0.1
    # else:
    #     square_x += 0.1
        
    # if square_x < 0:
    #     square_x = 0
    #     square_dir = 'right'
    #     square_y += 10
    # if square_x + 30 > WIDTH:
    #     square_x = WIDTH - 30
    #     square_dir = 'left'
    #     square_y += 10
    # if square_y < 0:
    #     square_y = 0
    # if square_y > HEIGHT:
    #     square_y = HEIGHT - 30

    if player_x < 0:
        player_x = 0
    if player_x + player_width > WIDTH:
        player_x = WIDTH - player_width
    if player_y < 0:
        player_y = 0
    if player_y + player_heigh > HEIGHT:
        player_y = HEIGHT - player_heigh



    for i in range(square_cnt):
        if square_x[i] + 30 > player_x and square_x[i] < player_x:
            if square_y[i] + 30 > player_y and square_y[i] < player_y:
                print("Hit")
                player_x = 0
                player_y = 0

        if square_x[i] + 30 > player_x and square_x[i] < player_x:
            if square_y[i] + 30 > player_y + 30 and square_y[i] < player_y + 30:
                print("Hit")
                player_x = 0
                player_y = 0

        if square_x[i] + 30 > player_x + 30 and square_x[i] < player_x + 30:
            if square_y[i] + 30 > player_y and square_y[i] < player_y:
                print("Hit")
                player_x = 0
                player_y = 0

        if square_x[i] + 30 > player_x + 30 and square_x[i] < player_x + 30:
            if square_y[i] + 30 > player_y + 30 and square_y[i] < player_y + 30:
                print("Hit")
                player_x = 0
                player_y = 0

    screen.fill(COLOR)
    for i in range(square_cnt):
        draw(square_img[i], square_x[i], square_y[i])
    draw(player_img, player_x, player_y)

    pygame.display.flip()

