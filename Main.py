from pygame import *
from math import *
from random import *
from pickle import *

init()

#Screen information
WIDTH, HEIGHT = 1280, 720
screen = display.set_mode((WIDTH, HEIGHT))


#Start of the loop
while True:
    for action in event.get():
        if action.type == QUIT:
            running = False
            break

    else:
        
        display.flip()
        continue
    break

quit()