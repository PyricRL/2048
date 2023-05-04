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
        self.number = number
        self.width = width
        self.height = height
        self.score = score
        self.rect = pygame.rect.Rect(x, y, width, height)
        pygame.draw.rect(win, (255, 0, 0), self.rect)
        if number == 0:
            number = 0
            self.image = pygame.transform.scale(images["2"], (width, height))
            self.image.fill(Config.background)
        else:
            self.image = pygame.transform.scale(images[str(number)], (width, height))

    def draw(self):
        win.blit(self.image, self.rect)

    def change(self, num):
        self.number = num
        if num == 0:
            im = images["2"].copy()
            im.fill(Config.background)
            self.image = pygame.transform.scale(im, (self.width, self.height))
        else:
            im = images[str(num)].copy()
            self.image = pygame.transform.scale(im, (self.width, self.height))
    def check_collision(self): #test
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= Config.winwidth:
            self.rect.right = Config.winwidth
        if self.rect.bottom <= Config.winheight:
            self.rect.bottom = Config.winheight
        if self.rect.top <= 0:
            self.rect.top = 0
    #does this fricking work


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
# getBlock(0,0).change(2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
            elif event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN:
                pass
        blocks.draw(win)  # draws the sprite group of blocks to the window
        pygame.display.update()
