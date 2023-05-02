import pygame, sys
import Config
pygame.init()

win = pygame.display.set_mode((Config.winwidth, Config.winheight))

class Block():
    def __init__(self,number,color,width,height):
        pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #this is a test if i can see it in github

        pygame.display.update()

        #this is another test

        #this is a third test