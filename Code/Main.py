import pygame, sys
import Config

pygame.init()

win = pygame.display.set_mode((Config.winwidth, Config.winheight))

def createGrid():
    """simply creates the Blocks to go on the grid and returns a group in a one liner B)"""
    return pygame.sprite.Group([
    [
        Block(
            0, 
            (255, 0, 0),
            Config.blockwidth,
            Config.blockheight,
            x * (Config.blockwidth + Config.boarderwidth)+Config.boarderwidth,
            y * (Config.blockheight + Config.boarderwidth)+Config.boarderwidth,
            0
        )
        for x in range(Config.gridwidth)
    ]
    for y in range(Config.gridheight)
    ])
class Block(pygame.sprite.Sprite):
    def __init__(self, number, color, width, height, x, y, score):
        super().__init__()
        self.number = number
        self.color = color
        self.width = width
        self.height = height
        self.score = score

        self.rect = pygame.rect.Rect(x, y, width, height)
        self.block = pygame.draw.rect(win, self.color, self.rect)

        # Textures for the sprite, someone needs to draw the actual blocks :\
        # I did - Logan
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

    def Draw(self):

        win.blit(self.image, self.rect)

#basically a loop through all of the game board positions, maps them to pixels,
#then creates a Block sprite to go there

blocks = createGrid()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        blocks.draw(win)
        pygame.display.update()
