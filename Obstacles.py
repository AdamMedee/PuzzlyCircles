from pygame import *
from math import *
from random import *
from pickle import *

class Block:
    def __init__(self, xPos, yPos, image):
        self.rect = Rect(xPos, yPos, 40, 40)
        self.image = image

    def update(self, screen):
        screen.blit(self.image, self.rect)

class Magma:
    def __init__(self, xPos, yPos, imageList):
        self.rect = Rect(xPos, yPos, 40, 40)
        self.imageList = imageList
        self.timer = 0

    def update(self, screen):
        screen.blit(self.imageList[(self.timer%240)//80], self.rect)

class BounceBlock:
    def __init__(self, xPos, yPos, image):
        self.rect = Rect(xPos, yPos, 40, 40)
        self.imageList = image

    def update(self, screen):
        screen.blit(self.image. self.rect)

class PortalEnds:
    def __init__(self, xPos, yPos, image):
        self.rect = Rect(xPos, yPos, 40, 40)
        self.image = image

    def update(self, screen):
        screen.blit(self.image, self.rect)

class Projectile:
    def __init__(self, xVel, yVel, xPos, yPos, radius, type, slowAmount):
        self.xVel = xVel
        self.yVel = yVel
        self.xPos = xPos
        self.yPos = yPos
        self.radius = radius
        self.type = type
        self.slowAmount = slowAmount
        self.dead = False
        self.rect = Rect(self.xPos - radius, self.yPos - radius, radius*2, radius*2)

    def move(self):
        self.xPos += self.xVel
        self.yPos += self.yVel

    def getType(self):
        return self.type()

    def getSlowAmount(self):
        return self.slowAmount

    def update(self, screen):
        if type == "kill":
            draw.circle(screen, (255, 0, 0), (self.xPos, self.yPos), self.radius, 0)
        elif type == "slow":
            draw.circle(screen, (160, 160, 255), (self.xPos, self.yPos), self.radius, 0)
        draw.circle(screen, (0, 0, 0), (self.xPos, self.yPos), self.radius, 2)

