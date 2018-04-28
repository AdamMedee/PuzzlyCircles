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
        self.yVel = 0
        self.accel = 3
        self.gravity = 1.189207
        self.jumpVel = 17.448
        self.frame = 0
        self.onGround = False
        self.rect = Rect(self.xPos, self.yPos, self.width, self.height)
        self.spriteSheet = image.load("resources/images/charSprites.png")
        #0 is stand, 1 is run1, 2 is run2, 3 is fall
        self.imageList = [self.spriteSheet.subsurface(Rect(i*32, 0, 32, 70)) for i in range(4)]
        self.imageListR = [transform.flip(self.imageList[i], True, False) for i in range(4)]

    def control(self, keyPresses):
        if self.onGround:
            if keyPresses[K_a]:
                self.xVel = -self.accel
            if keyPresses[K_d]:
                self.xVel = self.accel
            if keyPresses[K_w] and self.onGround:
                self.yVel = -self.jumpVel
            if self.xVel:
                self.frame += 1
                if self.frame > 100:
                    self.frame = 0

    def updateRect(self):
        self.rect.x = int(round(self.xPos)+0.1)
        self.rect.y = int(round(self.yPos)+0.1)

    def updatePos(self):
        self.xPos = self.rect.x
        self.yPos = self.rect.y

    def collideBlock(self, blockList):
        self.xPos += self.xVel
        self.updateRect()
        for block in blockList:
            if block.rect.colliderect(self.rect):
                if self.xVel > 0:
                    self.rect.right = block.rect.left
                elif self.xVel < 0:
                    self.rect.left = block.rect.right
        self.xVel = 0

        if not self.onGround:
            self.yVel += self.gravity
        self.onGround = False
        self.yPos += self.yVel
        self.updateRect()
        for block in blockList:
            if block.rect.colliderect(self.rect):
                if self.yVel > 0:
                    self.onGround = True
                    self.rect.bottom = block.rect.top
                    self.yVel = 0
                elif self.yVel < 0:
                    self.rect.top = block.rect.bottom
                    self.yVel = 0
        self.updatePos()
        self.updateRect()

    def update(self, screen):
        if not self.xVel and self.onGround:
            screen.blit(self.imageList[0], self.rect)
        elif not self.onGround and self.yVel > 0:
            screen.blit(self.imageList[3], self.rect)
        elif not self.onGround:
            if self.xVel < 0:
                screen.blit(self.imageList[2], self.rect)
            else:
                screen.blit(self.imageList[1], self.rect)
        elif self.xVel > 0:
            if self.frame < 25:
                screen.blit(self.imageList[1], self.rect)
            elif self.frame < 50:
                screen.blit(self.imageList[0], self.rect)
            elif self.frame < 75:
                screen.blit(self.imageList[2], self.rect)
            elif self.frame < 100:
                screen.blit(self.imageList[0], self.rect)
        elif self.xVel < 0:
            if self.frame < 25:
                screen.blit(self.imageListR[1], self.rect)
            elif self.frame < 50:
                screen.blit(self.imageListR[0], self.rect)
            elif self.frame < 75:
                screen.blit(self.imageListR[2], self.rect)
            elif self.frame < 100:
                screen.blit(self.imageListR[0], self.rect)
        #draw.rect(screen, (255, 100, 100), self.rect)