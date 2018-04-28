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



