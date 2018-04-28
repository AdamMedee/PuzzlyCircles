from pygame import *
from math import *
from random import *

init()
buttonFont = font.Font("Quantify Bold v2.6.ttf", 60)
inGameFont = font.Font("Quantify Bold v2.6.ttf", 30)

class mainMenuUI:
    def __init__(self, screen, width, height, mx, my):
        self.screen = screen
        self.width = width
        self.height = height
        self.mx = mx
        self.my = my

    def show(self):
        mainMenu = Surface((1280, 720))
        mainMenu.fill((255,255,255))

        title = buttonFont.render("Whomst've'ly'yaint'ed'i'es'y'es", 0 , (0,0,0,255))
        mainMenu.blit(title, (self.width//2 - title.get_width()//2, 20))

        start_text = buttonFont.render("Start", 0, (0,0,0,255))
        start_rect = Rect(self.width//2 - start_text.get_width()//2 - 5, 2 * self.height // 3 - 5, start_text.get_width() + 10, start_text.get_height() + 10)
        mainMenu.blit(start_text, (self.width//2 - start_text.get_width()//2, 2 * self.height // 3))

        levelSelect_text = buttonFont.render("Level Select", 0, (0, 0, 0, 255))
        levelSelect_rect = Rect(self.width // 2 - levelSelect_text.get_width() // 2, 2 * self.height // 3 + 70, levelSelect_text.get_width() + 10, levelSelect_text.get_height() + 10)
        mainMenu.blit(levelSelect_text, (self.width // 2 - levelSelect_text.get_width() // 2, 2 * self.height // 3 + 70))

        if start_rect.collidepoint(self.mx, self.my):
            start_text = buttonFont.render("Start", 0, (100, 100, 100, 255))
            mainMenu.blit(start_text, (self.width // 2 - start_text.get_width() // 2, 2 * self.height // 3))
        elif levelSelect_rect.collidepoint(self.mx, self.my):
            levelSelect_text = buttonFont.render("Level Select", 0, (100, 100, 100, 255))
            mainMenu.blit(levelSelect_text, (self.width // 2 - levelSelect_text.get_width() // 2, 2 * self.height // 3 + 70))

        self.screen.blit(mainMenu, (0,0))

    def getStartDimensions(self):
        start_text = buttonFont.render("Start", 0, (0, 0, 0, 255))
        return Rect(self.width//2 - start_text.get_width()//2 - 5, 2 * self.height // 3 - 5, start_text.get_width() + 10, start_text.get_height() + 10)

    def getLevelSelectDimensions(self):
        levelSelect_text = buttonFont.render("Level Select", 0, (0, 0, 0, 255))
        return Rect(self.width // 2 - levelSelect_text.get_width() // 2, 2 * self.height // 3 + 70, levelSelect_text.get_width() + 10, levelSelect_text.get_height() + 10)


class inGameUI:
    def __init__(self, screen, score, timeleft):
        self.screen = screen
        self.score = score
        self.timeleft = timeleft

    def show(self):
        gameScreen = Surface((1280, 720))
        gameScreen.fill((255, 255, 255))

        score = min(self.score, 99999)

        scoreword = inGameFont.render('Score:', 0, (0, 0, 0))
        gameScreen.blit(scoreword, (gameScreen.get_size()[0] - (scoreword.get_width() + 10), 70))
        scoretext = inGameFont.render('%05d' % (score), 0, (0, 0, 0))
        gameScreen.blit(scoretext, (gameScreen.get_size()[0] - (scoreword.get_width() + 10), 100))

        timetext = inGameFont.render('Time', 0, (0,0,0))
        gameScreen.blit(timetext, (gameScreen.get_size()[0] - (scoreword.get_width() + 10), 10))
        timelefttext = inGameFont.render('%d:%02d' % (self.timeleft // 60, self.timeleft % 60), 0, (0,0,0))
        gameScreen.blit(timelefttext, (gameScreen.get_size()[0] - (scoreword.get_width() + 10), 40))

        self.screen.blit(gameScreen, (0, 0))

class levelSelectUI:
    def __init__(self, screen, width, height, mx, my, names):
        self.screen = screen
        self.width = width
        self.height = height
        self.mx = mx
        self.my = my
        self.names = names

    def show(self):
        levelSelectScreen = Surface((1280, 720))
        levelSelectScreen.fill((255, 255, 255))

        currentname = 0

        levelSelect_text = buttonFont.render("Level Select", 0, (0,0,0,255))
        levelSelectScreen.blit(levelSelect_text, (self.width//2 - levelSelect_text.get_width()//2, 30))

        for i in range(4):
            for j in range(3):
                level_text = buttonFont.render(self.names[currentname], 0 , (0,0,0))
                levelSelectScreen.blit(level_text, (80+ 300*i, 220 + 130*j))
                currentname += 1

        self.screen.blit(levelSelectScreen, (0,0))