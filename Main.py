from pygame import *
from math import *
from random import *
from pickle import *
from Environment import *

init()

#Screen information
WIDTH, HEIGHT = 1280, 720
screen = display.set_mode((WIDTH, HEIGHT))

l = Level(1)

#Start of the loop
while True:
    for action in event.get():
        if action.type == QUIT:
            running = False
            break



    else:
        keyPresses = key.get_pressed()
        screen.fill((255, 255, 255))
        l.run(keyPresses)
        l.update()
        display.flip()
        continue

    break

quit()