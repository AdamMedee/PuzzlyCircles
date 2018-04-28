from pygame import *
from math import *
from random import *
from pickle import *
from Obstacles import *
from Characters import *

blockImg = image.load("")
backgroundList = [
    image.load("")
]

levelList = []
for i in range(1):
    levelList.append([])
    with open("L%d" % (i+1), "r") as file:
        levelList[i].append(file.readline())

class Level:
    def __init__(self, number):
        self.number = number
        self.blockList = []
        self.enemyList = []
        self.projectileList = []
        self.player = Player(100, 100)
        self.levelCode = levelList[number - 1]
        for row in range(18):
            for col in range(32):
                if self.levelCode[row][col] == "B":
                    self.blockList.append(Block(row*40, col*40, blockImg))

    def run(self, keyPresses):
        self.player.control(keyPresses)
        self.player.move()

    def update(self, screen):
        screen.blit(backgroundList[self.number-1])
        self.player.update()
        for block in self.blockList:
            block.update(screen)

