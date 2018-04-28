from pygame import *
from math import *
from random import *
from pickle import *

from Interface import *

init()

#Screen information
WIDTH, HEIGHT = 1280, 720
screen = display.set_mode((WIDTH, HEIGHT))

menu = "main"


#Start of the loop
while True:
    leftClick = False
    for action in event.get():
        if action.type == QUIT:
            running = False
            break

        if action.type == KEYDOWN:
            if action.key == K_UP:
                pass
            elif action.key == K_RIGHT:
                pass
            elif action.key == K_DOWN:
                pass
            elif action.key == K_LEFT:
                pass

        if action.type == MOUSEBUTTONDOWN:
            if action.button == 1:
                leftClick = True
        else:
            leftClick = False

    else:
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()

        if menu == "main":
            mainMenuUI(screen)
            bliton = mainMenuUI.show(mainMenuUI, WIDTH, HEIGHT, mx, my, mb)
            screen.blit(bliton, (0,0))
            if mainMenuUI.getStartDimensions(mainMenuUI, WIDTH, HEIGHT).collidepoint(mx, my) and leftClick:
                menu = "inGame"

        elif menu == "inGame":
            inGameUI(screen)
            bliton = inGameUI.show(inGameUI, 20, 345)
            screen.blit(bliton, (0, 0))

        display.flip()
        continue

    break

quit()