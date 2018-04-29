from pygame import *
from math import *
from random import *
from pickle import *
from Environment import *
from Interface import *

init()

# Fonts
titleFont = font.Font("resources/text/Quantify Bold v2.6.ttf", 150)
buttonFont = font.Font("resources/text/Quantify Bold v2.6.ttf", 60)
inGameFont = font.Font("resources/text/Quantify Bold v2.6.ttf", 30)



#Screen information
WIDTH, HEIGHT = 1280, 720
screen = display.set_mode((WIDTH, HEIGHT))

backgroundList = [image.load("resources/images/background%d.png" % i).convert() for i in range(1, 2)]

menu = "main"
mainBackground = transform.scale(image.load("resources/images/menuBack.png"), (1280, 720))
mainTitle = transform.scale(titleFont.render("PUZZLY CIRCLES", False, (255, 255, 255)), (800, 150))
playButton = buttonFont.render("PLAY", False, (255, 255, 255))
playButtonP = buttonFont.render("PLAY", False, (130, 130, 130))
mainButtonList = [
    Button(Rect(550, 350, 180, 80), playButton, playButtonP, "Play")
]

levelSelectBackground = transform.scale(image.load("resources/images/levelselectBackground.png"), (1280, 720))
levelSelectTitle = transform.scale(titleFont.render("LEVEL SELECT", False, (255, 255, 255)), (800, 150))
selectButtonList = [
    Button(Rect(225 + 250*(i%4), 250 + 140*(i//4), 100, 100), buttonFont.render("%-2d" % (i+1), False, (255, 255, 255)), buttonFont.render("%-2d" % (i+1), False, (130, 130, 130)), "%d" % (i+1)) for i in range(12)
]

#Start of the loop
while True:
    leftClick = False
    keys = key.get_pressed()
    for action in event.get():
        if action.type == QUIT:
            running = False
            break

        if action.type == MOUSEBUTTONDOWN:
            if action.button == 1:
                leftClick = True
        else:
            leftClick = False

    else:
        mouseX, mouseY = mouse.get_pos()

        if menu == "main":
            screen.blit(mainBackground, (0, 0))
            screen.blit(mainTitle, (240, 50))
            for button in mainButtonList:
                button.update(screen, (mouseX, mouseY))
                if button.clicked((mouseX, mouseY), leftClick) and button.getName() == "Play":
                    menu = "levelSelect"


        elif menu == "levelSelect":
            screen.blit(levelSelectBackground, (0, 0))
            screen.blit(levelSelectTitle, (0, 0))
            for button in selectButtonList:
                button.update(screen, (mouseX, mouseY))
                if button.clicked((mouseX, mouseY), leftClick):
                    currentLevel = Level(int(button.name.strip(" ")), backgroundList[int(button.name.strip(" "))-1])
                    menu = "game"

        elif menu == "game":
            currentLevel.run(keys)
            currentLevel.update(screen)

        display.flip()
        continue

    break

quit()