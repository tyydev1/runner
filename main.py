import pygame # type: ignore
from sys import exit

########################################
# PYGAME SETUP
########################################

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
running = True

########################################
# CLASSES
########################################

class Debug:
    def __init__(self):
        self.numOfFrames = 0
        self.frameCycles = 0

    def update(self):
        if self.numOfFrames != 60:
            self.numOfFrames += 1
            return self.numOfFrames
        self.numOfFrames = 0
        self.frameCycles += 1
        return self.numOfFrames
    
    def get_numOfFrames(self):
        return self.numOfFrames
    
    def get_frameCycles(self):
        return self.frameCycles

########################################
# GAME SETUP
########################################

clock = pygame.time.Clock()
testFont = pygame.font.Font('font/Pixeltype.ttf', 50)

skySurface = pygame.image.load('graphics/Sky.png')
groundSurface = pygame.image.load('graphics/ground.png')
textSurface = testFont.render("My game", False, 'Black')
debug = Debug()

def quit():
    pygame.quit()
    running = False
    exit() # for safety purposes

########################################
# GAME LOOP
########################################

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.blit(skySurface, (0, 0))
    screen.blit(groundSurface, (0, 300))
    screen.blit(textSurface, (300, 50))

    pygame.display.update()
    clock.tick(60)
    debug.update()
    print(f"[DEBUG] frame/cycle indicator: {debug.numOfFrames}, {debug.frameCycles}")