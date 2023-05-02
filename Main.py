import pygame, sys
import Config
pygame.init()

win = pygame.display.set_mode((Config.winwidth, Config.winheight))

class Block():
    def __init__(self,number,color,width,height):
        self.number = number
        self.color = color
        self.width = width
        self.height = height
    
    def Draw():
        pass

    def Update():
        pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.update()