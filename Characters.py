from pygame import *
from math import *
from random import *
from pickle import *

class Player:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.width = 32
        self.height = 72
        self.xVel = 0
        self.yPos = 0
        self.accel = 1
        self.gravity = 0.02378414
        self.jumpVel = 17.448
        self.onGround = True
        self.rect = Rect(self.xPos, self.yPos, self.width, self.height)
        self.image = image.load("")

    def control(self, keyPresses):
        if self.onGround:
            if keyPresses[K_a]:
                self.xVel -= self.accel
            if keyPresses[K_d]:
                self.xVel += self.accel
            if keyPresses[K_w]:
                self.yVel = self.jumpVel

    def move(self):
        self.xPos += self.xVel
        self.yPos += self.yVel
        onGround = False

    def updateRect(self):
        self.rect.x = int(self.xPos)
        self.rect.y = int(self.yPos)

    def updatePos(self):
        self.xPos = self.rect.x
        self.yPos = self.rect.y

    def collideBlock(self, blockList):
        for block in blockList:
            if block.rect.colliderect(self.rect):
                if block.rect.top <= self.rect.bottom:
                    onGround = True
                    self.rect.bottom = block.rect.top
                    self.yVel = 0
                if block.rect.bottom > self.rect.top:
                    self.rect.top = block.rect.bottom
                    self.yVel = 0
                if block.rect.right >= self.rect.left:
                    self.rect.left = block.rect.y
                    self.xVel = 0
                if block.rect.left <= self.rect.right:
                    self.rect.right = block.rect.left
                    self.xVel = 0

        self.updatePos()


    def update(self, screen):
        screen.blit(self.graphic, (self.xPos, self.yPos))