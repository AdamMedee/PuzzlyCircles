from pygame import *
from math import *
from random import *
from pickle import *
from Obstacles import *
from Characters import *

blockImg = image.load("resources/images/block.png")
backgroundList = [image.load("resources/images/background%d.png" % i) for i in range(1, 2)]

levelList = []
for i in range(1):
    levelList.append([])
    with open("resources/levels/L%d.txt" % (i+1), "r") as file:
        for j in range(18):
            levelList[i].append(file.readline().strip("\n"))

class Level:
    def __init__(self, number):
        self.number = number
        self.blockList = []
        self.bounceList = []
        self.enemyList = []
        self.projectileList = []
        self.score = 0
        self.player = Player(100, 100)
        self.levelCode = levelList[number - 1]
        for row in range(18):
            for col in range(32):
                if self.levelCode[row][col] == "B":
                    self.blockList.append(Block(col*40, row*40, blockImg))

    def run(self, keyPresses):
        self.player.control(keyPresses)
        self.player.move()
        self.player.collideBlock(self.blockList)





    def update(self, screen):
        #screen.blit(backgroundList[self.number-1], (0, 0))
        self.player.update(screen)
        for block in self.blockList:
            block.update(screen)

