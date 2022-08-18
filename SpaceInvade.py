import pygame
import random
import math
from pygame import mixer
pygame.init()

# I have to make a screen with variable name screen
screen = pygame.display.set_mode((627, 418))
# Adding backgroundimages on Screen
background = pygame.image.load("spaceImg.png")
# Adding background music
mixer.music.load("background.wav")
mixer.music.play(-1)
# Set title to our Pygame
pygame.display.set_caption("Space Invader")
# Set icon to our game
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

# Adding Players to our game
playerImg = pygame.image.load("spaceshipimg.png")
playerX = 249.5
playerY = 354
playerX_change = 0

# Adding Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX =10
textY =10

def show_score(x,y):
    score = font.render("Score : " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
# Function for PLayer
def player(x, y):
    screen.blit(playerImg, (x, y))


# Adding Enemy to our game
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 563)
enemyY = random.randint(0, 5)
enemyX_change = 1.5
enemyY_change = 10


# Function for enemy
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Adding Bullet to our game
bulletImg = pygame.image.load("playerBul1.png")
bulletX = 0
bulletY = 354
bulletX_change = 0
bulletY_change = 2.7
bullet_state = "ready"


# Function for player bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 10, y + 0))


def isCollision(enemyX,enemyY,bulletX,buletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False



# Initially make running = True
running = True
# make a game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 2.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    screen.blit(background, (0, 0))
    playerX += playerX_change
    # Lets add boundary to our space ship
    if playerX >= 563:
        playerX = 563
    elif playerX <= 0:
        playerX = 0
    # Lets add boundary to our enemy

    enemyX += enemyX_change

    if enemyX >= 563:
        enemyX_change = -1
        enemyY += enemyY_change
    elif enemyX <= 0:
        enemyX_change = 1
        enemyY += enemyY_change
        # Fire Bullet From player Side

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        # Fire bullet from enemy side

    if bulletY <= 0 :
        bulletY = 354
        bullet_state = "ready"
    # Collision
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        collision_sound = mixer.Sound('explosion.wav')
        collision_sound.play()
        bulletY = 354
        bullet_state = "ready"
        score_value +=1
        print(score_value)
        enemyX = random.randint(0, 563)
        enemyY = random.randint(0, 5)

    enemy(enemyX, enemyY)
    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()
