import pygame # type: ignore
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
running = True

testSurface = pygame.image.load('graphics/Sky.png')
testSurface.fill('Red')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            exit() # for safety purposes

    screen.blit(testSurface, (0, 0))    

    pygame.display.update()
    clock.tick(60)