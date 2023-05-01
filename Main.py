import pygame, sys
from Config import *

win = pygame.display.set_mode(winwidth, winheight)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()