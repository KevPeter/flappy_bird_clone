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
dx = 1.4        # background x-axis movement

# create class for pipe
class pipe(object):
    bottomPipeImg = pygame.image.load(os.path.join("images", "floor_pipe.png")).convert()
    topPipeImg = pygame.image.load(os.path.join("images", "ceil_pipe.png")).convert()

    def __init__(self, x, y, width, height):                # (pipe) constructor function for pipe
        self.x = x
        self.y = y
        self.yTop = y - 400
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

    # def collision(self, rect):                              # (pipe) function to check collisions


def DrawScreen():                                             # updates screen drawings
    screen.blit(backgroundImg, (backgroundX, 0))
    screen.blit(backgroundImg, (backgroundX2, 0))

    for obstacle in obstacles:
        obstacle.drawPipe(screen)       # originally pipeGame.drawPipe

    pygame.display.update()


clock = pygame.time.Clock()
pygame.time.set_timer(USEREVENT+1, 2000)
speed = 60
# obstacle is list of pipes to display on screen
obstacles = []



running = True
while running:                                          # game loop start

    DrawScreen()
    backgroundX -= dx
    backgroundX2 -= dx
    #pipeGame.x -= dx

    if backgroundX < backgroundImg.get_width() * -1:
        backgroundX = backgroundImg.get_width()
    if backgroundX2 < backgroundImg.get_width() * -1:
        backgroundX2 = backgroundImg.get_width()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT+1:
            r = random.randrange(100, 420)
            obstacles.append(pipe(600, r, 52, 320))

    clock.tick(speed)

