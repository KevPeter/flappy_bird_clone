import pygame
# initialize python
pygame.init()
# create screen
W, H = 650, 480
screen = pygame.display.set_mode((W, H))
# title
pygame.display.set_caption("Flappy Bird")
#background
backgroundImg = pygame.image.load("background.png")
backgroundX = 0
backgroundX2 = backgroundImg.get_width()

def redisplayScreen():
    screen.blit(backgroundImg, (backgroundX, 0))
    screen.blit(backgroundImg, (backgroundX2, 0))
    pygame.display.update()

clock = pygame.time.Clock()
speed = 60

# game loop
running = True
while running:
    redisplayScreen()
    backgroundX -= 1.4
    backgroundX2 -= 1.4
    if backgroundX < backgroundImg.get_width() * -1:
        backgroundX = backgroundImg.get_width()
    if backgroundX2 < backgroundImg.get_width() * -1:
        backgroundX2 = backgroundImg.get_width()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(speed)

