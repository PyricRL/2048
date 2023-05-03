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


# Dictionary of images for our block class
images = {
    "2": pygame.image.load(".\\assets\\2BlueBlock.png"),
    "4": pygame.image.load(".\\assets\\4RedBlock.png"),
    "8": pygame.image.load(".\\assets\\8LightGreenBlock.png"),
    "16": pygame.image.load(".\\assets\\16PurpleBlock.png"),
    "32": pygame.image.load(".\\assets\\32YellowBlock.png"),
    "64": pygame.image.load(".\\assets\\64LightBlueBlock.png"),
    "128": pygame.image.load(".\\assets\\128OrangeBlock.png"),
}


class Block(pygame.sprite.Sprite):
    def __init__(self, number, width, height, x, y, score):
        super().__init__()
        self.number = number
        self.width = width
        self.height = height
        self.score = score
        self.images = images
        self.rect = pygame.rect.Rect(x, y, width, height)
        pygame.draw.rect(win, (255, 0, 0),self.rect)
        self.image = pygame.transform.scale(self.images["2"],(width,height))

    def draw(self):
        win.blit(self.image, self.rect)
    def change(self,im):
        self.image = pygame.transform.scale(im,(self.width,self.height))

blocks = createGrid()
win.fill(Config.boardercolor)
blocks.sprites()[5].change(images["128"])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        blocks.draw(win)  # draws the sprite group of blocks to the window
        pygame.display.update()
