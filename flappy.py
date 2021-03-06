import pygame
from pygame.locals import *
import random
import os

# initialize python
pygame.init()

# create screen
W, H = 650, 480
screen = pygame.display.set_mode((W, H))

# title
pygame.display.set_caption("Flappy Bird")

# create background
backgroundImg = pygame.image.load(os.path.join("images", "background.png")).convert()
backgroundX = 0
backgroundX2 = backgroundImg.get_width()
dx = 2        # background x-axis movement

# create class for player
class player(object):
    riseImg = pygame.image.load(os.path.join("images", "bird-rise.png")).convert()
    fallImg = pygame.image.load(os.path.join("images", "bird-fall.png")).convert()

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rising = False
        self.hitbox = [x, y, width, height]
        self.birdVel = -9
        self.maxBirdVel = 10
        self.birdAccel = 1
        self.flapAccel = -9

    def drawBird(self, screen):
        self.y += self.birdVel
        if self.birdVel < self.maxBirdVel and not self.rising:
            self.birdVel += self.birdAccel
        if self.rising:
            self.birdVel = self.flapAccel
            self.rising = False

        self.hitbox[1] = self.y
        screen.blit(self.riseImg, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)


# create class for pipe
class pipe(object):
    bottomPipeImg = pygame.image.load(os.path.join("images", "floor_pipe.png")).convert()
    topPipeImg = pygame.image.load(os.path.join("images", "ceil_pipe.png")).convert()

    def __init__(self, x, y, width, height):                # (pipe) constructor function for pipe
        self.x = x
        self.y = y
        self.yTop = y - 450
        self.width = width
        self.height = height
        self.hitbox = [x, y, width, height]
        self.hitbox2 = [x, self.yTop, width, height]

    def drawPipe(self, screen):                             # (pipe) function to draw pipe
        self.hitbox[0] = self.x
        self.hitbox2[0] = self.x
        screen.blit(self.bottomPipeImg, (self.x, self.y))
        screen.blit(self.topPipeImg, (self.x, self.yTop))
        pygame.draw.rect(screen,(255, 0, 0), self.hitbox2, 2)
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
        self.x -= dx

    def collision(self, box):                              # (pipe) function to check collisions
        if box[0] + box[2] > self.hitbox[0] and box[0] < self.hitbox[0] + self.hitbox[2]:
            if box[1] + box[3] > self.hitbox[1]:
                endGame()
                print("bottom")
                return True

        if box[0] + box[2] > self.hitbox2[0] and box[0] < self.hitbox2[0] + self.hitbox2[2]:
            if box[1] < self.hitbox2[1] + self.hitbox2[3]:
                print("top")
                endGame()
                return True
        return False


bird = player(250, 200, 34, 24)


def drawScreen():                                             # updates screen drawings
    screen.blit(backgroundImg, (backgroundX, 0))
    screen.blit(backgroundImg, (backgroundX2, 0))
    bird.drawBird(screen)

    for obstacle in obstacles:
        obstacle.drawPipe(screen)       # originally pipeGame.drawPipe

    pygame.display.update()


def endGame():
    global obstacles
    obstacles = []
    pause = True

    while pause:
        pygame.time.delay(500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.time.delay(250)
                pause = False
                bird.y = 200
                bird.rising = True

        screen.blit(backgroundImg, (0, 0))
        font = pygame.font.SysFont('Arial', 80)
        font2 = pygame.font.SysFont('Arial', 30)
        gameOverDisplay = font.render('Game Over..', 1, (255, 255, 255))
        screen.blit(gameOverDisplay, (W / 2 - gameOverDisplay.get_width() / 2, 200))
        continueGame = font2.render('Click anywhere to continue', 1, (255, 255, 255))
        screen.blit(continueGame, (W / 2 - continueGame.get_width() / 2, 325))
        pygame.display.update()



clock = pygame.time.Clock()
pygame.time.set_timer(USEREVENT+1, 1800)
speed = 60
# obstacle is list of pipes to display on screen
obstacles = []


running = True
while running:                                          # game loop start

    for obstacle in obstacles:
        if obstacle.collision(bird.hitbox):
            print("hit")

    backgroundX -= dx
    backgroundX2 -= dx
    # pipeGame.x -= dx

    if backgroundX < backgroundImg.get_width() * -1:
        backgroundX = backgroundImg.get_width()
    if backgroundX2 < backgroundImg.get_width() * -1:
        backgroundX2 = backgroundImg.get_width()

    flapAccel = -9
    birdVel = -9
    birdAccel = 1
    maxBirdVel = 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT+1:
            r = random.randrange(160, 420)
            obstacles.append(pipe(700, r, 52, 320))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird.rising = True

    clock.tick(speed)
    drawScreen()

