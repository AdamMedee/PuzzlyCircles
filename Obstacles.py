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
        self.timer += 1
        screen.blit(self.imageList[(self.timer%240)//80], self.rect)

class BounceBlock:
    def __init__(self, xPos, yPos, image, imageP):
        self.rect = Rect(xPos, yPos, 40, 40)
        self.imageList = image
        self.stepped = 50
        self.image = image
        self.imageP = imageP

    def update(self, screen):
        self.stepped += 1
        if self.stepped < 50:
            screen.blit(self.imageP, self.rect)
        else:
            screen.blit(self.image, self.rect)
            self.stepped = 50

class PortalBlock:
    def __init__(self, rect):
        self.rect = rect
        self.image = image.load("resources/images/portalSpot.png")

    def update(self, screen):
        screen.blit(self.image, self.rect)

class Portal:
    def __init__(self):
        self.portal1 = None
        self.portal2 = None
        self.image1 = image.load("resources/images/portal1.png").subsurface((40, 0, 40, 40))
        self.image2 = image.load("resources/images/portal2.png").subsurface((40, 0, 40, 40))
        self.portalshot1 = None
        self.vel = 5
        self.shot1velX = 0
        self.shot1velY = 0
        self.portalshot2 = None
        self.shot2velX = 0
        self.shot2velY = 0

    def shoot(self, bulletNum, playerCoords, mousePos):
        angle = atan2(mousePos[1] - playerCoords[1], mousePos[0] - playerCoords[0])
        if bulletNum == 1 and not self.portalshot1:
            self.portalshot1 = playerCoords
            self.shot1velX = self.vel * cos(angle)
            self.shot1velY = self.vel * sin(angle)
            portal1 = None
        if bulletNum == 2 and not self.portalshot2:
            self.portalshot2 = playerCoords
            self.shot2velX = self.vel * cos(angle)
            self.shot2velY = self.vel * sin(angle)
            portal2 = None

    def move(self):
        if self.portalshot1:
            self.portalshot1[0] += self.shot1velX
            self.portalshot1[1] += self.shot1velY
        if self.portalshot2:
            self.portalshot2[0] += self.shot2velX
            self.portalshot2[1] += self.shot2velY

    def kill(self, blockList, magmaList, bounceList, enemyList, screen):
        if self.portalshot1:
            for b in blockList + magmaList + bounceList + enemyList:
                if b.rect.collidepoint(self.portalshot1):
                    self.portalshot1 = None
                    break
        if self.portalshot2:
            for b in blockList + magmaList + bounceList + enemyList:
                if b.rect.collidepoint(self.portalshot2):
                    self.portalshot2 = None
                    break


    def collidePortal(self, portalList):
        for portal in portalList:
            if self.portalshot1 and portal.rect.collidepoint(self.portalshot1) and self.portal2 != portal.rect:
                self.portal1 = portal.rect
                self.portalshot1 = None
            if self.portalshot2 and portal.rect.collidepoint(self.portalshot2) and self.portal1 != portal.rect:
                self.portal2 = portal.rect
                self.portalshot2 = None

    def update(self, screen):
        if self.portal1:
            screen.blit(self.image1, self.portal1)
        if self.portal2:
            screen.blit(self.image2, self.portal2)
        if self.portalshot1:
            draw.circle(screen, (255, 0, 255), [int(i) for i in self.portalshot1], 5, 0)
            draw.circle(screen, (0, 0, 0), [int(i) for i in self.portalshot1], 5, 2)
        if self.portalshot2:
            draw.circle(screen, (255, 100, 100), [int(i) for i in self.portalshot2], 5, 0)
            draw.circle(screen, (0, 0, 0), [int(i) for i in self.portalshot2], 5, 2)

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
        self.rect = Rect(self.xPos - self.radius, self.yPos - self.radius, self.radius * 2, self.radius * 2)

    def kill(self, blockList, magmaList, bounceList):
        for b in blockList + magmaList + bounceList:
            if b.rect.collidepoint((self.xPos, self.yPos)):
                self.dead = True
                break

    def getType(self):
        return self.type

    def getSlowAmount(self):
        return self.slowAmount

    def update(self, screen):
        if self.type == "kill":
            draw.circle(screen, (255, 0, 0), (int(self.xPos), int(self.yPos)), self.radius, 0)
            draw.circle(screen, (0, 0, 0), (int(self.xPos), int(self.yPos)), self.radius, 2)
        elif self.type == "slow":
            draw.circle(screen, (160, 160, 255), (int(self.xPos), int(self.yPos)), self.radius, 0)
            draw.circle(screen, (0, 0, 0), (int(self.xPos), int(self.yPos)), self.radius, 2)

