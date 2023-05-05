import random
import pygame, sys
import Config

pygame.init()

win = pygame.display.set_mode((Config.winwidth, Config.winheight))
win.fill(Config.bordercolor)

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
        self.x = (x - Config.borderwidth) // (Config.blockwidth + Config.borderwidth)
        self.y = (y - Config.borderwidth) // (Config.blockheight + Config.borderwidth)
        self.number = number
        self.width = width
        self.height = height
        self.score = score
        self.rect = pygame.rect.Rect(x, y, width, height)

        if number == 0:
            number = 0
            self.image = pygame.transform.scale(images["2"], (width, height))
            self.image.fill(Config.background)
        else:
            self.image = pygame.transform.scale(images[str(number)], (width, height))

    def change(self, num):
        """Change the block's number"""
        self.number = num
        if num == 0:
            im = images["2"].copy()
            im.fill(Config.background)
            self.image = pygame.transform.scale(im, (self.width, self.height))
        else:
            im = images[str(num)].copy()
            self.image = pygame.transform.scale(im, (self.width, self.height))

    def move(self, x, y):
        """Moves the block to x,y"""
        if getBlock(x, y) != self:
            t = getBlock(x, y)
            t.change(self.number + t.number)
            self.change(0)
            return t
        return self

    def update(self, *args, **kwargs) -> None:
        # add what you want every block to do each tick here

        # checks if the block can move and moves it
        if self.number != 0:
            if event.key == pygame.K_LEFT:
                for x in range(self.x):

                    # Move Left
                    if (
                        getBlock(x, self.y).number == 0
                        or getBlock(x, self.y).number == self.number
                    ):
                        self.move(x, self.y)
                        break

            elif event.key == pygame.K_RIGHT:
                for x in range(3, self.x, -1):

                    # Move Right
                    if (
                        getBlock(x, self.y).number == 0
                        or getBlock(x, self.y).number == self.number
                    ):
                        self.move(x, self.y)
                        break

            elif event.key == pygame.K_UP:
                for y in range(self.y):

                    # Move Up
                    if (
                        getBlock(self.x, y).number == 0
                        or getBlock(self.x, y).number == self.number
                    ):
                        self.move(self.x, y)
                        break

            elif event.key == pygame.K_DOWN:
                for y in range(3, self.y, -1):

                    # Move Down
                    if (
                        getBlock(self.x, y).number == 0
                        or getBlock(self.x, y).number == self.number
                    ):
                        self.move(self.x, y)
                        break

        return super().update(*args, **kwargs)


def randomBlock():
    """Adds a random block to the game"""
    x, y = random.randint(0, 3), random.randint(0, 3)
    while getBlock(x, y).number != 0:
        x, y = random.randint(0, 3), random.randint(0, 3)
    getBlock(x, y).change(2)


def createGrid() -> pygame.sprite.Group:
    """simply creates the Blocks to go on the grid and returns a group in a one-liner B)"""
    return pygame.sprite.Group(
        [
            [
                Block(
                    0,
                    Config.blockwidth,
                    Config.blockheight,
                    x * (Config.blockwidth + Config.borderwidth) + Config.borderwidth,
                    y * (Config.blockheight + Config.borderwidth) + Config.borderwidth,
                    0,
                )
                for x in range(Config.gridwidth)
            ]
            for y in range(Config.gridheight)
        ]
    )


def getBlock(x, y) -> Block:
    """Gets the Block at the coordinates X,Y"""
    b = blocks.sprites()
    return b[y * Config.gridwidth + x]


# Dictionary of images for our block class


blocks = createGrid()
block = getBlock(0, 0)
getBlock(3, 0).change(2)
block.change(2)
blocks.draw(win)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            blocks.update()
            randomBlock()
            blocks.draw(win)  # draws the sprite group of blocks to the window
    pygame.display.update()
