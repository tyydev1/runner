import pygame # type: ignore
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
running = True

test_surface = pygame.Surface((100, 200))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            exit() # for safety purposes

    screen.blit(test_surface, (0, 0))    

    pygame.display.update()
    clock.tick(60)