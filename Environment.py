from pygame import *
from math import *
from random import *
from pickle import *
from Obstacles import *
from Characters import *

init()

blockImg = image.load("resources/images/block.png")
magmaImgList = [image.load("resources/images/lava.png").subsurface(Rect(i * 40, 0, 40, 40)) for i in range(3)]
enemyImg = [
            [image.load("resources/images/groundEnemy.png").subsurface(Rect(i * 40, 0, 40, 40)) for i in range(2)],
            [image.load("resources/images/flyingEnemy.png").subsurface(Rect(i * 40, 0, 40, 40)) for i in range(2)]
            ]
bounceImg = image.load("resources/images/trampoline.png").subsurface(Rect(0, 0, 40, 40))
bounceImg1  = image.load("resources/images/trampoline.png").subsurface(Rect(40, 0, 40, 40))

levelList = []
for i in range(12):
    levelList.append([])
    with open("resources/levels/L%d.txt" % (i+1), "r") as file:
        for j in range(18):
            levelList[i].append(file.readline().strip("\n"))

enemyList = []
for i in range(12):
    with open("resources/levels/L%dE.txt" % (i+1), "r") as file:
        enemies = int(file.readline().strip("\n"))
        enemyList.append([])
        for j in range(enemies):

            #startX, startY, endX, endY, vel, imageList, shoots, rate, bulletType, SlowS, angle
            v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11 = file.readline().strip("\n").split(" ")
            print(i, len(enemyList), v6, len(enemyImg))
            enemyList[i].append(Enemy(int(v1), int(v2), int(v3), int(v4), int(v5), enemyImg[int(v6)], bool(v7), int(v8), int(v9), int(v10), float(v11)))

class Level:
    def __init__(self, number, background):
        self.number = number
        self.blockList = []
        self.bounceList = []
        self.enemyList = enemyList[number - 1]
        self.projectileList = []
        self.magmaList = []
        self.portalList = []
        self.score = 0
        self.endPic = image.load("resources/images/rocketship.png")
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
                elif self.levelCode[row][col] == "S":
                    self.player = Player(col*40, row*40)
                elif self.levelCode[row][col] == "E":
                    self.endpos = (col*40, row*40)
                elif self.levelCode[row][col] == "C":
                    self.bounceList.append(BounceBlock(col*40, row*40, bounceImg, bounceImg1))

    def run(self, keyPresses, mousePresses, mousePos, screen):
        self.timePassed += 0.02
        self.player.control(keyPresses)
        self.player.collideBlock(self.blockList, self.bounceList)
        self.player.collideMagma(self.magmaList)
        self.player.collideEnemy(self.enemyList)
        self.player.collideProjectile(self.projectileList)
        self.player.collidePortal((self.portals.portal1, self.portals.portal2))
        self.portals.move()
        self.portals.collidePortal(self.portalList)
        for projectile in self.projectileList:
            projectile.move()
            projectile.kill(self.blockList, self.bounceList, self.magmaList)
        for i in range(len(self.projectileList)-1, -1, -1):
            if self.projectileList[i].dead:
                del self.projectileList[i]

        for enemy in self.enemyList:
            enemy.move()
            tmpProj = enemy.shoot()
            if tmpProj:
                self.projectileList.append(tmpProj)

        self.portals.kill(self.blockList, self.magmaList, self.bounceList, self.enemyList, screen)

        s = 0
        if mousePresses[0]:
            s = 1
        if mousePresses[1]:
            s = 2
        self.portals.shoot(s, [self.player.xPos+16, self.player.yPos+33], mousePos)

    def winAnimation(self, screen):
        if self.player.rect.colliderect(self.endpos[0], self.endpos[1], 40, 80):
            return True
        else:
            return False

    def update(self, screen):
        screen.blit(self.background, (0, 0))
        self.player.update(screen)
        screen.blit(self.endPic, self.endpos)
        for enemy in self.enemyList:
            enemy.update(screen)
        for block in self.blockList:
            block.update(screen)
        for magma in self.magmaList:
            magma.update(screen)
        for portal in self.portalList:
            portal.update(screen)
        for projectile in self.projectileList:
            projectile.update(screen)
        for bounce in self.bounceList:
            bounce.update(screen)
        self.portals.update(screen)
        return self.player.getDead()

