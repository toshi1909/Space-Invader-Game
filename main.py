import pygame
import random
import math

# initialise the pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('001-project.png')
pygame.display.set_icon(icon)

collision = False

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)


def show_score(x, y):
    scoreshow = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(scoreshow, (x, y))


# Player
playerimg = pygame.image.load('001-battleship.png')
playerx = 370
playery = 480
movex = 0

# Enemy
enemyimg = []
enemyy = []
enemyx = []
enemychangex = []
enemychangey = []
numofenemy = 10

for i in range(numofenemy):
    enemyimg.append(pygame.image.load('001-space-invaders.png'))
    enemyx.append(random.randint(0, 736))
    enemyy.append(random.randint(50, 150))
    enemychangex.append(0.6)
    enemychangey.append(40)

# Bullet
bulletimg = pygame.image.load('001-bullet.png')
bulletx = playerx
bullety = playery
bulletchangex = 0
bulletchangey = 2
bulletstate = "ready"
# Ready= you cant see the bullet
# fire= you fire the bullet

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def fiirebullet(x, y):
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


def isCollision(ex, ey, bx, by):
    distance = math.sqrt(((ex-bx)*(ex-bx))+((ey-by)*(ey-by)))
    if distance < 27:
        return True
    else:
        return False


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movex = -0.4
            if event.key == pygame.K_RIGHT:
                movex = 0.4
            if event.key == pygame.K_SPACE:
                if bulletstate == "ready":
                    bulletx = playerx
                    fiirebullet(bulletx, bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movex = 0

    # RGB- Red, blue, green
    screen.fill((0, 0, 30))

    playerx += movex

    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    for i in range(numofenemy):
        # Game Over
        if enemyy[i] > 450:
            for j in range(numofenemy):
                enemyy[j] = 2000
            game_over_text()
            break

        enemy(enemyx[i], enemyy[i], i)
        enemyx[i] += enemychangex[i]
        if enemyx[i] <= 0:
            enemychangex[i] = 0.6
            enemyy[i] += 40
        elif enemyx[i] >= 736:
            enemychangex[i] = -0.6
            enemyy[i] += 40
        collision = isCollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            bullety = 480
            bulletstate = "ready"
            score += 1
            print(score)
            enemyx[i] = random.randint(0, 800)
            enemyy[i] = random.randint(50, 150)

    if bullety <= 0:
        bullety = 480
        bulletstate = "ready"

    if bulletstate is "fire":
        fiirebullet(bulletx, bullety)
        bullety -= 1.8

    player(playerx, playery)
    show_score(10, 10)

    pygame.display.update()
