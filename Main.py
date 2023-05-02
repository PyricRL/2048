from typing import Any
import pygame, sys
import Config

pygame.init()

win = pygame.display.set_mode((Config.winwidth, Config.winheight))


def createGrid() -> pygame.sprite.Group:
    """simply creates the Blocks to go on the grid and returns a group in a one-liner B)"""
    return pygame.sprite.Group(
        [
            [
                Block(
                    0,
                    (255, 0, 0),
                    Config.blockwidth,
                    Config.blockheight,
                    x * (Config.blockwidth + Config.boarderwidth) + Config.boarderwidth,
                    y * (Config.blockheight + Config.boarderwidth)
                    + Config.boarderwidth,
                    0,
                )
                for x in range(Config.gridwidth)
            ]
            for y in range(Config.gridheight)
        ]
    )


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
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

    def Draw(self):
        win.blit(self.image, self.rect)


blocks = createGrid()
blocks.sprites()[0].image.fill( # example of changing the color of one of the blocks to blue
    (0, 0, 255)
) 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        blocks.draw(win)  # draws the sprite group of blocks to the window
        pygame.display.update()
