import pygame # type: ignore
from sys import exit

########################################
# PYGAME SETUP
########################################

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')

LOCKED_FPS = 60 # CHANGE THIS LINE FOR FPS 
running = True

########################################
# CLASSES
########################################

class Debug:
    def __init__(self):
        self.numOfFrames = 0
        self.frameCycles = 0

    def update(self):
        if self.numOfFrames != LOCKED_FPS:
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

skySurface = pygame.image.load('graphics/Sky.png').convert()
groundSurface = pygame.image.load('graphics/ground.png').convert()
textSurface = testFont.render("My game", False, 'Black')

snailSurface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snailRect = snailSurface.get_rect(bottomright = (600, 300))

playerSurf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
playerRect = playerSurf.get_rect(midbottom = (80, 300))

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
    
    snailRect.x -= 4
    if snailRect.right <= 0: snailRect.left = 800
    screen.blit(snailSurface, snailRect)
    screen.blit(playerSurf, playerRect)

    pygame.display.update()
    clock.tick(LOCKED_FPS)
    debug.update()
    print(f"[DEBUG] frame/cycle indicator: {debug.numOfFrames}, {debug.frameCycles}")