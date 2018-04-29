from pygame import *
from math import *
from random import *
from pickle import *
from Obstacles import *
from Characters import *

init()

blockImg = image.load("resources/images/block.png")
magmaImgList = [image.load("resources/images/lava.png").subsurface(Rect(i * 40, 0, 40, 40)) for i in range(3)]


levelList = []
for i in range(2):
    levelList.append([])
    with open("resources/levels/L%d.txt" % (i+1), "r") as file:
        for j in range(18):
            levelList[i].append(file.readline().strip("\n"))

class Level:
    def __init__(self, number, background):
        self.number = number
        self.blockList = []
        self.bounceList = []
        self.enemyList = []
        self.projectileList = []
        self.magmaList = []
        self.portalList = []
        self.score = 0
        self.player = Player(100, 100)
        self.levelCode = levelList[number - 1]
        self.background = background
        self.timePassed = 0
        self.portals = Portal()
        for row in range(18):
            for col in range(32):
                if self.levelCode[row][col] == "B":
                    self.blockList.append(Block(col*40, row*40, blockImg))
                elif self.levelCode[row][col] == "M":
                    self.magmaList.append(Magma(col*40, row*40, magmaImgList))
                elif self.levelCode[row][col] == "P":
                    self.portalList.append(PortalBlock(Rect(col*40, row*40, 40, 40)))

    def run(self, keyPresses, mousePresses, mousePos, screen):
        self.timePassed += 0.02
        self.player.control(keyPresses)
        #self.player.move()
        self.player.collideBlock(self.blockList)
        self.player.collidePortal((self.portals.portal1, self.portals.portal2))
        self.portals.move()
        self.portals.collidePortal(self.portalList)

        self.portals.kill(self.blockList, self.magmaList, self.bounceList, screen)
        s = 0
        if mousePresses[0]:
            s = 1
        if mousePresses[1]:
            s = 2
        self.portals.shoot(s, [self.player.xPos+16, self.player.yPos+33], mousePos)

    def update(self, screen):
        screen.blit(self.background, (0, 0))
        self.player.update(screen)
        for block in self.blockList:
            block.update(screen)
        for magma in self.magmaList:
            magma.update(screen)
        for portal in self.portalList:
            portal.update(screen)
        self.portals.update(screen)
        return self.player.getDead()

