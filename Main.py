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

# Screen information
WIDTH, HEIGHT = 1280, 720
screen = display.set_mode((WIDTH, HEIGHT))

background = image.load("resources/images/background1.png").convert()

mixer.music.load("resources/music/music1.mp3")
mixer.music.play(-1)

storyBG = transform.scale(image.load("resources/images/storylineBG.png"), (1280, 720))
manualBG = transform.scale(image.load("resources/images/manual.png"), (1280, 820))

menu = "main"
mainBackground = transform.scale(image.load("resources/images/menuBack.png"), (1280, 720))
mainTitle = transform.scale(titleFont.render("PUZZLY CIRCLES", False, (220, 220, 255)), (800, 150))
playButton = buttonFont.render("PLAY", False, (220, 220, 255))
playButtonP = buttonFont.render("PLAY", False, (130, 130, 130))
storyButton = buttonFont.render("STORY", False, (255, 255, 255))
storyButtonP = buttonFont.render("STORY", False, (130, 130, 130))
manualButton = buttonFont.render("MANUAL", False, (255, 255, 255))
manualButtonP = buttonFont.render("MANUAL", False, (130, 130, 130))
backButton = buttonFont.render("BACK", False, (255, 255, 255))
backButtonP = buttonFont.render("BACK", False, (130, 130, 130))
BackButton = Button(Rect(20, 20, 150, 70), backButton, backButtonP, "Back")
mainButtonList = [
    Button(Rect(550, 270, 180, 80), playButton, playButtonP, "Play"),
    Button(Rect(540, 400, 200, 80), storyButton, storyButtonP, "Story"),
    Button(Rect(500, 530, 280, 80), manualButton, manualButtonP, "Manual")
]
resumeButton = Button(Rect(525, 300, 230, 80), buttonFont.render("RESUME", False, (220, 220, 255)),
                      buttonFont.render("RESUME", False, (130, 130, 130)), "game")
quitButton = Button(Rect(545, 420, 190, 80), buttonFont.render("QUIT", False, (220, 220, 255)),
                    buttonFont.render("QUIT", False, (130, 130, 130)), "levelSelect")

levelSelectBackground = transform.scale(image.load("resources/images/levelselectBackground.png"), (1280, 720))
levelSelectTitle = transform.scale(titleFont.render("LEVEL SELECT", False, (255, 255, 255)), (800, 150))
selectButtonList = [
                       Button(Rect(225 + 250 * (i % 4), 250 + 140 * (i // 4), 100, 100),
                              buttonFont.render("%-2d" % (i + 1), False, (220, 220, 255)),
                              buttonFont.render("%-2d" % (i + 1), False, (130, 130, 130)), "%d" % (i + 1)) for i in
                       range(12)
                   ] + [BackButton]

winBackground = transform.scale(image.load("resources/images/winBack.png"), (1280, 720))

storyTitle = transform.scale(titleFont.render("BACKSTORY", False, (255, 255, 255)), (800, 150))
clock = time.Clock()
# Start of the loop
while True:
    leftClick = False
    rightClick = False
    keys = key.get_pressed()
    for action in event.get():
        if action.type == QUIT:
            running = False
            break

        if action.type == MOUSEBUTTONDOWN:
            if action.button == 1:
                leftClick = True
            if action.button == 3:
                rightClick = True
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
                elif button.clicked((mouseX, mouseY), leftClick) and button.getName() == "Story":
                    menu = "story"
                elif button.clicked((mouseX, mouseY), leftClick) and button.getName() == "Manual":
                    menu = "manual"

        elif menu == "levelSelect":
            screen.blit(levelSelectBackground, (0, 0))
            screen.blit(levelSelectTitle, (240, 50))
            for button in selectButtonList:
                button.update(screen, (mouseX, mouseY))
                if button.clicked((mouseX, mouseY), leftClick):
                    if button.name == "Back":
                        menu = "main"
                    else:
                        currentLevel = Level(int(button.name.strip(" ")), background)
                        menu = "game"

        elif menu == "game":
            currentLevel.run(keys, [leftClick, rightClick], [mouseX, mouseY], Rect(0, 0, WIDTH, HEIGHT))
            lose = currentLevel.update(screen)
            win = currentLevel.winAnimation(screen)
            pauseButton = Button(Rect(20, 20, 100, 30), buttonFont.render("PAUSE", False, (220, 220, 255)),
                                 buttonFont.render("PAUSE", False, (130, 130, 130)), "pause")
            pauseButton.update(screen, (mouseX, mouseY))
            if pauseButton.clicked((mouseX, mouseY), leftClick):
                menu = "pause"
            if lose:
                menu = "lose"
                restartButton = Button(Rect(540, 300, 200, 80), buttonFont.render("NEW LEVEL", False, (220, 220, 255)),
                                       buttonFont.render("NEW LEVEL", False, (130, 130, 130)), "Restart")
                playagainButton = Button(Rect(560, 450, 160, 80), buttonFont.render("AGAIN", False, (220, 220, 255)),
                                         buttonFont.render("AGAIN", False, (130, 130, 130)), "Restart")
            elif win:
                menu = "win"
                timeText = transform.scale(
                    buttonFont.render("TIME: %d" % currentLevel.timePassed, False, (220, 220, 255)), (230, 100))
                restartButton = Button(Rect(840, 400, 230, 80), buttonFont.render("NEW LEVEL", False, (220, 220, 255)),
                                       buttonFont.render("NEW LEVEL", False, (130, 130, 130)), "Restart")
                playagainButton = Button(Rect(860, 550, 190, 80), buttonFont.render("AGAIN", False, (220, 220, 255)),
                                         buttonFont.render("AGAIN", False, (130, 130, 130)), "Restart")


        elif menu == "lose":
            restartButton.update(screen, (mouseX, mouseY))
            playagainButton.update(screen, (mouseX, mouseY))
            if restartButton.clicked((mouseX, mouseY), leftClick):
                menu = "levelSelect"
            elif playagainButton.clicked((mouseX, mouseY), leftClick):
                menu = "game"
                currentLevel = Level(currentLevel.number, background)

        elif menu == "win":
            screen.blit(winBackground, (0, 0))
            screen.blit(timeText, (840, 260))
            restartButton.update(screen, (mouseX, mouseY))
            playagainButton.update(screen, (mouseX, mouseY))
            if restartButton.clicked((mouseX, mouseY), leftClick):
                menu = "levelSelect"
            elif playagainButton.clicked((mouseX, mouseY), leftClick):
                menu = "game"
                currentLevel = Level(currentLevel.number, background)

        elif menu == "story":
            screen.blit(storyBG, (0, 0))
            BackButton.update(screen, (mouseX, mouseY))
            screen.blit(storyTitle, (240, 50))
            if BackButton.clicked((mouseX, mouseY), leftClick):
                menu = "main"

        elif menu == "manual":
            screen.blit(manualBG, (0, 0))
            BackButton.update(screen, (mouseX, mouseY))
            if BackButton.clicked((mouseX, mouseY), leftClick):
                menu = "main"

        elif menu == "pause":
            resumeButton.update(screen, (mouseX, mouseY))
            quitButton.update(screen, (mouseX, mouseY))
            if resumeButton.clicked((mouseX, mouseY), leftClick):
                menu = "game"
            if quitButton.clicked((mouseX, mouseY), leftClick):
                menu = "levelSelect"

        clock.tick(50)
        display.flip()
        continue

    break

quit()
